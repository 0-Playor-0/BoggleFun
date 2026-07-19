import random

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_grid_size():
    """Ask the player for a grid size, re-prompting until it's valid."""
    while True:
        raw = input("How big would you like the grid to be? ")
        try:
            n = int(raw)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if n > 100:
            print("You cannot have a grid that big, it must be less than 100.")
        elif n < 3:
            print("You cannot have a grid that small, it must be greater than 2.")
        else:
            return n


def make_grid(n):
    return [[random.choice(ALPHABET) for _ in range(n)] for _ in range(n)]


def show_grid(grid):
    n = len(grid)
    border = " " + "___ " * n
    for row in grid:
        print(border)
        print("| " + " | ".join(row) + " |")
    print(" " + "--- " * n)
