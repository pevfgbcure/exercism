def egg_count(display_value: int) -> int:
    """Calculate the number of eggs in the display case.
    - The display case is a binary representation of the number of eggs it contains.
      For example, if the display value is 5 (which is 101 in binary), it means there
      are 2 eggs in the display case.

    Args:
        display_value (int): The value shown on the display case.

    Returns:
        int: The number of eggs in the display case.
    """
    number_of_eggs = 0
    while display_value > 0:
        number_of_eggs += display_value % 2
        display_value //= 2

    return number_of_eggs
