def slices(series: str, length: int) -> list[str]:
    """Produces all the contiguous substrings of a string of digits that are of a given length.

    Args:
        series (str): A string of digits.
        length (int): The length of the substrings to produce.

    Returns:
        list[str]: A list of all contiguous substrings of the given length.

    Raises:
        ValueError: If the length is zero or negative, if the series is empty, or if the length is greater than the length of the series.
    """
    if length == 0:
        raise ValueError("slice length cannot be zero")

    if length < 0:
        raise ValueError("slice length cannot be negative")

    if not series:
        raise ValueError("series cannot be empty")

    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    return [series[i : i + length] for i in range(0, len(series) - length + 1)]
