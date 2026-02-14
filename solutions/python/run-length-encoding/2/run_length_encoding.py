def decode(string: str) -> str:
    """Decodes a run-length encoded string.

    Args:
        string (str): The run-length encoded string to decode.

    Returns:
        str: The decoded string.
    """
    repetitions_str = ""
    decoded_string = ""

    for char in string:
        if char.isdigit():
            repetitions_str += char

        if char.isalpha() or char == " ":
            repetitions_int = int(repetitions_str) if repetitions_str else 1
            decoded_string += char * repetitions_int
            repetitions_str = ""

    return decoded_string


def encode(string: str) -> str:
    """Encodes a string using run-length encoding.

    Args:
        string (str): The string to encode.

    Returns:
        str: The run-length encoded string.
    """
    if not string:
        return ""

    encoded_string = ""
    current_char = string[0]
    char_repetitions = 1

    # The '#' symbol marks the end of the string.
    for char in string[1:] + "#":
        if char != current_char or char == "#":
            encoded_string += (
                f"{char_repetitions if char_repetitions > 1 else ''}{current_char}"
            )
            current_char = char
            char_repetitions = 0

        char_repetitions += 1

    return encoded_string
