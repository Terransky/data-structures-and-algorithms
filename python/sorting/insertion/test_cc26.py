from cc26 import insertion_sort

example1 = [8, 4, 23, 42, 16, 15]
reverse = [20, 18, 12, 8, 5, -2]
uniques = [5, 12, 7, 5, 5, 7]
nearly = [2, 3, 5, 7, 13, 11]


def test_exists():
    assert insertion_sort


def test_basic():
    actual = insertion_sort(example1)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_reverse():
    actual = insertion_sort(reverse)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


def test_uniques():
    actual = insertion_sort(uniques)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_nearly():
    actual = insertion_sort(nearly)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected


def test_empty():
    actual = insertion_sort([])
    expected = []
    assert actual == expected


def test_invalid_type():
    actual = insertion_sort(4)
    expected = "Please input a list"
    assert actual == expected

