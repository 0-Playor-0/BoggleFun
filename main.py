import time

import basicui
import points
from algo import TIME_LIMIT_SECONDS, play_round


def main():
    n = basicui.get_grid_size()
    grid = basicui.make_grid(n)
    basicui.show_grid(grid)

    found_words = []
    found_paths = []
    deadline = time.time() + TIME_LIMIT_SECONDS

    while time.time() < deadline:
        remaining = int(deadline - time.time())
        print(f"\n{remaining} seconds left.")
        cont = input("Would you like to continue? ").strip().lower()
        if cont == "no":
            break
        if not play_round(grid, n, found_words, found_paths, deadline):
            break

    print("\nWords found:", found_words)
    points.calculate_total(found_words)


if __name__ == "__main__":
    main()
