"""
Collectors.
"""
import time
import asyncio
import logging
from typing import List, Tuple, Dict

import aiohttp

from .re_parsers import find_all_image_urls, find_tag
from .loaders import load_page, load_image
from .utils import save_json, load_json
from .data_converters import create_image_tag_df, create_tags2images_dict


logger = logging.getLogger(__name__)


async def collect_dataset(
    n_iterations: int, n_parallel_tasks: int
) -> List[Tuple[str, List[str]]]:
    """Collect tag and image hashes pairs using info from the site.

    Parameters
    ----------
    n_iterations : int
        The number of parsing iterations.
    n_parallel_tasks : int
        The number of parallel jobs in one iteration.

    Returns
    -------
    List[Tuple[str, List[str]]]
        The list with tags and image ids for some tag.
    """
    result = []

    time_full_start = time.time()
    i_iteration = 1
    while i_iteration <= n_iterations:
        try:
            time_current_start = time.time()

            async with aiohttp.ClientSession() as session:
                tasks = [load_page(session) for _ in range(n_parallel_tasks)]

                result.extend(await asyncio.gather(*tasks))

            current_time = time.time() - time_current_start
            total_time = time.time() - time_full_start
            logger.info(
                "iteration: {}/{}; batch time: {:.2f}s; total time: {:.2f}s".format(
                    i_iteration, n_iterations, current_time, total_time
                )
            )

            i_iteration += 1

        except aiohttp.ServerDisconnectedError as error:
            logger.warning(str(error))
            time.sleep(2)

    return result


async def run_collection_process(n_iterations: int, n_parallel_tasks: int) -> None:
    """Create result json with tag to images info.

    Parameters
    ----------
    n_iterations : int
        The number of parsing iterations.
    n_parallel_tasks : int
        The number of parallel jobs in one iteration.
    """
    result = await collect_dataset(n_iterations, n_parallel_tasks)
    df = create_image_tag_df(result)
    tags2images = create_tags2images_dict(df)
    save_json(tags2images)


async def get_correct_images_by_content(content: str) -> None:
    """Get correct answer for some html content.

    Parameters
    ----------
    content : str
        The content from html page.
    """
    tags2images = load_json()
    hashes = []
    new_images = find_all_image_urls(content)
    new_tag = find_tag(content)

    async with aiohttp.ClientSession() as session:
        for img in new_images:
            hashes.append(await load_image(session, img))

    print("GRID:\n| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")
    print("SELECT NEXT IMAGES:")
    for ind, _hash in enumerate(hashes, 1):
        if _hash in tags2images[new_tag]:
            print(ind)
