def line_up(name: str, number: int) -> str:
    """Format a string to show the customer's name and their position in the line.

    Args:
        name (str): The customer's name.
        number (int): The customer's position in the line.

    Returns:
        str: A string formatted as "{name}, you are the {ordinal} customer we serve today. Thank you!"
    """
    ordinal = str(number)

    if ordinal.endswith("1") and not ordinal.endswith("11"):
        ordinal += "st"
    elif ordinal.endswith("2") and not ordinal.endswith("12"):
        ordinal += "nd"
    elif ordinal.endswith("3") and not ordinal.endswith("13"):
        ordinal += "rd"
    else:
        ordinal += "th"

    return f"{name}, you are the {ordinal} customer we serve today. Thank you!"
