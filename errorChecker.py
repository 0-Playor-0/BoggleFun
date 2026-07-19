import wordPlay


def in_bounds(coord, n):
    x, y = coord
    return 0 <= x < n and 0 <= y < n


def is_adjacent(a, b):
    return a != b and abs(a[0] - b[0]) <= 1 and abs(a[1] - b[1]) <= 1


def has_duplicates(coords):
    return len(coords) != len(set(coords))


def path_to_word(grid, coords):
    return "".join(grid[x][y] for x, y in coords)


def validate(coords, grid, n, found_paths):
    """Validate a candidate path and return the word it spells, or None."""
    for coord in coords:
        if not in_bounds(coord, n):
            print("One of your coordinates is off the board. Try again.")
            return None

    for a, b in zip(coords, coords[1:]):
        if not is_adjacent(a, b):
            print("Those letters aren't adjacent on the board. Try again.")
            return None

    if has_duplicates(coords):
        print("You can't reuse the same tile twice in one word. Try again.")
        return None

    if coords in found_paths:
        print("You've already claimed that exact path. Try again.")
        return None

    word = path_to_word(grid, coords)
    if not wordPlay.is_english_word(word):
        print(f'"{word}" is not in the word list. Try again.')
        return None

    return word
