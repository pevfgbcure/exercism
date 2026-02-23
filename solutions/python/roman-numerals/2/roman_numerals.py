ROMAN_NUMERALS = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
}


def roman(number: int) -> str:
    """Convert an integer to a Roman numeral.

    Args:
        number (int): The integer to convert.

    Returns:
        str: The Roman numeral representation of the integer.
    """
    if number == 0:
        return ""

    for value in ROMAN_NUMERALS:
        if number >= value:
            return ROMAN_NUMERALS[value] + roman(number - value)
