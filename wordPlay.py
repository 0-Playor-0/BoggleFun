import csv
from pathlib import Path

_WORDLIST_PATH = Path(__file__).parent / "4000-words.csv"


def _load_words(path=_WORDLIST_PATH):
    with open(path, newline="") as word_file:
        return {row[0].upper() for row in csv.reader(word_file) if row}


WORDS = _load_words()


def is_english_word(word):
    """Case-insensitive lookup against the word list."""
    return word.upper() in WORDS
