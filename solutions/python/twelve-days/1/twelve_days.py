def recite(start_verse: int, end_verse: int) -> list[str]:
    """Recite the song "The Twelve Days of Christmas" from `start_verse` to `end_verse` inclusive.

    Args:
        start_verse (int): The verse number to start reciting from (1-based index).
        end_verse (int): The verse number to stop reciting at (1-based index).

    Returns:
        list[str]: A list of strings, where each string is a verse of the song corresponding to the verse
        numbers from `start_verse` to `end_verse`.
    """
    song = []
    for verse_number in range(start_verse - 1, end_verse):
        song.append(create_verse(verse_number))

    return song


def create_verse(verse_number: int) -> str:
    """Create a verse of "The Twelve Days of Christmas" corresponding to the given verse number.

    Args:
        verse_number (int): The verse number to create (0-based index).

    Returns:
        str: A string representing the verse of the song corresponding to the given verse number.
    """
    verses = [
        ("first", "a Partridge in a Pear Tree"),
        ("second", "two Turtle Doves"),
        ("third", "three French Hens"),
        ("fourth", "four Calling Birds"),
        ("fifth", "five Gold Rings"),
        ("sixth", "six Geese-a-Laying"),
        ("seventh", "seven Swans-a-Swimming"),
        ("eighth", "eight Maids-a-Milking"),
        ("ninth", "nine Ladies Dancing"),
        ("tenth", "ten Lords-a-Leaping"),
        ("eleventh", "eleven Pipers Piping"),
        ("twelfth", "twelve Drummers Drumming"),
    ]

    cardinal = verses[verse_number][0]
    complete_verse = f"On the {cardinal} day of Christmas my true love gave to me: "

    if verse_number == 0:
        return complete_verse + f"{verses[verse_number][1]}."

    for i, verse in enumerate(reversed(verses[0 : verse_number + 1])):
        complete_verse += f"{verse[1]}, " if i != verse_number else f"and {verse[1]}."

    return complete_verse
