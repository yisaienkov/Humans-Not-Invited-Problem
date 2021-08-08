"""
Data Converters.
"""
import pandas as pd
from typing import List, Tuple, Dict


def create_image_tag_df(result: List[Tuple[str, List[str]]]) -> pd.DataFrame:
    """Convert tag - image ids pairs to frequency DataFrame.

    Parameters
    ----------
    result : List[Tuple[str, List[str]]]
        Tag - image ids pairs.

    Returns
    -------
    pd.DataFrame
        The frequency DataFrame.
    """
    count_image_tag: Dict[str, Dict[str, int]] = {}
    for tag, image_ids in result:
        tmp_tag = count_image_tag.get(tag, {})
        for image_id in image_ids:
            tmp_tag[image_id] = tmp_tag.get(image_id, 0) + 1
        count_image_tag[tag] = tmp_tag
    df = pd.DataFrame(count_image_tag)
    df = df.fillna(0)
    return df


def create_tags2images_dict(df: pd.DataFrame) -> Dict[str, List[str]]:
    """Convert frequency DataFrame to tags2images dict.

    Parameters
    ----------
    df : pd.DataFrame
        The frequency DataFrame.

    Returns
    -------
    Dict[str, List[str]]
        tags2images dict.
    """
    tags = list(df.columns)
    images = list(df.index)
    image2tag = list(
        df.values.argmax(
            axis=1,
        )
    )

    tags2images: Dict[str, List[str]] = {}
    for i_tag, tag in enumerate(tags):
        tags2images[tag] = []
        for image_id, image_tag in zip(images, image2tag):
            if image_tag == i_tag:
                tags2images[tag].append(image_id)

    return tags2images
