import random

import jsmethods


def test_simple_entries():
    test_array = [0, 6, 934, "test"]
    result_entries = [(0, 0), (1, 6), (2, 934), (3, "test")]

    assert test_array.entries() == result_entries


def test_entries_compare_to_enumerate():
    test_array = ["str", (4, 5), "ul", 84, 1]
    result_entries = list(enumerate(test_array))

    assert test_array.entries() == result_entries


def test_entries_on_empty_array():
    test_array = []

    assert test_array.entries() == []


def test_entries_on_random_array():
    test_array = [random.randint(3443, 576677) for _ in range(100000)]
    result_entries = list(enumerate(test_array))

    assert test_array.entries() == result_entries
