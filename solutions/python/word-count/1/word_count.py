import re


def count_words(sentence: str) -> dict[str, int]:
    """Counts the occurrences of each word in a given sentence.

    - Words are defined as a sequence of letters and digits, optionally containing an
    apostrophe (') if it is followed by a letter.
    - The function ignores case and punctuation, treating words as the same regardless
    of their capitalization or surrounding punctuation.

    Args:
        sentence: A string containing the sentence to analyze.

    Returns:
        A dictionary with words as keys and their respective counts as values.
    """
    matches: list[str] = re.findall(
        r"((?:[a-zA-Z|\d](?:'[a-zA-Z])?)+)", sentence, re.IGNORECASE
    )

    words_count: dict[str, int] = {}
    for match in matches:
        match = match.lower()
        words_count.setdefault(match, 0)
        words_count[match] += 1

    return words_count
