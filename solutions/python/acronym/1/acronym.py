def abbreviate(words: str) -> str:
    """Convert a phrase to its acronym.

    Args:
        words: A phrase to convert, e.g. "Portable Network Graphics"

    Returns:
        The acronym of the phrase, e.g. "PNG"
    """
    abbr = [words[0]]

    is_word_start = False
    for char in words[1:]:
        if char in [" ", "-"]:
            is_word_start = True
            continue

        if is_word_start and char.isalpha():
            abbr.append(char)
            is_word_start = False

    return "".join(abbr).upper()
