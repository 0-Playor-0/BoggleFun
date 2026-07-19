import points
import errorChecker
import wordPlay

GRID = [["C", "A", "T"], ["X", "X", "X"], ["X", "X", "X"]]
N = 3


def test_calculate_total_sums_word_lengths():
    assert points.calculate_total(["CAT", "AT"]) == 5


def test_calculate_total_empty():
    assert points.calculate_total([]) == 0


def test_validate_accepts_real_word():
    word = errorChecker.validate([(0, 0), (0, 1), (0, 2)], GRID, N, [])
    assert word == "CAT"


def test_validate_rejects_out_of_bounds():
    assert errorChecker.validate([(0, 0), (0, 1), (3, 2)], GRID, N, []) is None


def test_validate_rejects_non_adjacent():
    assert errorChecker.validate([(0, 0), (2, 2), (0, 1)], GRID, N, []) is None


def test_validate_rejects_reused_tile():
    assert errorChecker.validate([(0, 0), (0, 0), (0, 1)], GRID, N, []) is None


def test_validate_rejects_repeated_path():
    path = [(0, 0), (0, 1), (0, 2)]
    assert errorChecker.validate(path, GRID, N, [path]) is None


def test_validate_rejects_word_not_in_list():
    grid = [["Z", "Q", "X"]]
    assert errorChecker.validate([(0, 0), (0, 1)], grid, 3, []) is None


def test_is_english_word_case_insensitive():
    assert wordPlay.is_english_word("cat")
    assert wordPlay.is_english_word("CAT")
    assert not wordPlay.is_english_word("zzqx")
