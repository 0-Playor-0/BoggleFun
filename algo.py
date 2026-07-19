import sys
import time

import errorChecker

TIME_LIMIT_SECONDS = 120
MIN_WORD_LENGTH = 3


def parse_coord(raw):
    parts = raw.split(",")
    if len(parts) != 2:
        raise ValueError(f"'{raw}' is not in x,y format")
    return (int(parts[0]), int(parts[1]))


def prompt_coord(label):
    raw = input(f"{label} (x,y): ").strip()
    if raw.lower() == "exit":
        sys.exit("You exited the game.")
    return raw


def play_round(grid, n, found_words, found_paths, deadline):
    """Play one word-guessing round. Returns False if time has run out."""
    if time.time() >= deadline:
        print("\nTime's up!\n")
        return False

    coords_raw = [prompt_coord("First letter"), prompt_coord("Second letter")]
    while True:
        if time.time() >= deadline:
            print("\nTime's up!\n")
            return False
        raw = input('Next letter (x,y), or "done" to submit: ').strip()
        if raw.lower() in ("done", "no"):
            break
        coords_raw.append(raw)

    if len(coords_raw) < MIN_WORD_LENGTH:
        print(f"Words need at least {MIN_WORD_LENGTH} letters. Try again.")
        return True

    try:
        coords = [parse_coord(raw) for raw in coords_raw]
    except ValueError:
        print("Coordinates must look like 'x,y' with whole numbers. Try again.")
        return True

    word = errorChecker.validate(coords, grid, n, found_paths)
    if word:
        found_words.append(word)
        found_paths.append(coords)
        print(f'Nice! "{word}" added ({len(word)} points).')

    return True
