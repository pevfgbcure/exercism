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
    roman_conversion = ""
    for value, representation in ROMAN_NUMERALS.items():
        if value_repetitions := number // value:
            roman_conversion += f"{representation * value_repetitions}"
            if (number := number - value_repetitions * value) == 0:
                break

    return roman_conversion
