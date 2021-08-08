"""
Parsers.
"""
import re
from typing import List, Union


def find_all_image_urls(content: Union[str, bytes]) -> List[str]:
    """Find image urls from some content.

    Parameters
    ----------
    content : Union[str, bytes]
        The content.

    Returns
    -------
    List[bytes]
        Image urls.
    """
    return re.findall("captcha/image.php\\?image_name=.*?&id=.", str(content))


def find_tag(content: Union[str, bytes]) -> str:
    """Find the content tag.

    Parameters
    ----------
    content : Union[str, bytes]
        The content.

    Returns
    -------
    str
        The content tag.
    """
    return re.findall('value="(.*?)" name="category"', str(content))[0]
