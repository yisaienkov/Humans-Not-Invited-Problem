"""
Loaders.
"""
import asyncio
from typing import List, Tuple

import hashlib
from aiohttp import ClientSession

from .re_parsers import find_all_image_urls, find_tag


BASE_URL = "http://www.humansnotinvited.com/"


async def load_image(session: ClientSession, image_url: str) -> str:
    """Load image and get hash of this image.

    Parameters
    ----------
    session : ClientSession
        The aiohttp.ClientSession object.
    image_url : str
        The image url.

    Returns
    -------
    str
        The image hash.
    """
    async with session.get(BASE_URL + image_url, allow_redirects=True) as response:
        data = await response.read()
    _hash = hashlib.md5(data).hexdigest()

    return _hash


async def load_page(session: ClientSession) -> Tuple[str, List[str]]:
    """Load page and images.

    Parameters
    ----------
    session : ClientSession
        The aiohttp.ClientSession object.

    Returns
    -------
    Tuple[str, List[str]]
        Tag and image hashes of the page.
    """
    async with session.get(BASE_URL, allow_redirects=True) as response:
        data = await response.read()

    image_urls = find_all_image_urls(data)
    tasks = []
    for image_url in image_urls:
        tasks.append(asyncio.create_task(load_image(session, image_url)))

    tag = find_tag(data)
    return tag, await asyncio.gather(*tasks)
