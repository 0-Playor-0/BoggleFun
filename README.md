# BoggleFun

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A command-line Boggle game: search a randomly generated letter grid for words by chaining together adjacent tiles, before the clock runs out.

## How it plays

- You choose the grid size (n×n).
- Words are formed by connecting adjacent letters — horizontally, vertically, or diagonally — without reusing a tile within the same word.
- You have **2 minutes** to find as many valid words as possible.
- Each word is checked against a ~4,000-word dictionary before it counts.
- Score is the total number of letters across all valid words found.

## Install

Requires Python 3.9+. No external dependencies for the game itself.

```bash
git clone https://github.com/0-Playor-0/BoggleFun.git
cd BoggleFun
```

## Run

```bash
python3 main.py
```

You'll be asked for a grid size, then prompted to enter coordinates for each letter in a word, in `x,y` format (0-indexed), one at a time. Type `done` or `no` to submit the word, or `exit` at any prompt to quit.

Example:

```
How big would you like the grid to be? 4
 ___ ___ ___ ___
| C | A | T | S |
 ...
Would you like to continue? yes
First letter (x,y): 0,0
Second letter (x,y): 0,1
Next letter (x,y), or "done" to submit: 0,2
Next letter (x,y), or "done" to submit: done
Nice! "CAT" added (3 points).
```

## Run the tests

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
python -m pytest
```

## Tech stack

- Python 3, standard library only (`csv`, `random`, `time`) for the game itself
- `pytest` for tests

## Why I built this

A small project to practice grid/graph traversal, input validation, and CLI game design — a classic word game re-implemented from scratch on the command line.

## Ideas for later (not implemented)

- Difficulty presets (grid size + time limit bundled together, e.g. Easy/Medium/Hard)
- A "show all possible words" solver to reveal what you missed after time runs out
- Persistent high-score tracking across sessions

## License

[MIT](LICENSE)
