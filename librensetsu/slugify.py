"""Module for slugifying the text"""

import re

from .transliterate import transliterate_no_accent

def slugify(text: str, non_alphanum_as_dash: bool = False, transliterate: bool = True) -> str:
    """
    Slugify the text

    :param text: The text to be slugified
    :type text: str
    :param non_alphanum_as_dash: Replace non-alphanumeric characters with dash, defaults to False
    :type non_alphanum_as_dash: bool, optional
    :param transliterate: Transliterate the text, defaults to True
    :type transliterate: bool, optional
    :return: The slugified text
    :rtype: str
    """

    naad = non_alphanum_as_dash
    """Alias for non_alphanum_as_dash"""

    lower = text.lower().strip()
    if transliterate:
        lower = transliterate_no_accent(lower)
    drop = re.sub(r"[^\w\s]", "-" if naad else "", lower)
    dash = re.sub(r"[\s_\-]+", "-", drop)
    trim_corner = re.sub(r"^-+|-+$", "", dash)
    return trim_corner