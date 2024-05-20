from pluralizer import Pluralizer

plr = Pluralizer()

uncountables = [
    "anime",
    "manga",
]

for word in uncountables:
    plr.addUncountableRule(word)


def pluralize(count: int, word: str) -> str:
    """
    Backwards-compatible wrapper for the pluralizer module.
    :param count: The count.
    :type count: int
    :param word: The word to pluralize.
    :type word: str
    :return: The pluralized word, e.g. "1 day" or "2 days".
    :rtype: str
    """
    word = str(plr.pluralize(word, count, True))  # type: ignore
    if count > 0:
        return word
    return ""
