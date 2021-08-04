import random

import listchaining
from random import randint


def test_simple_reversed():
    test_array = [6, 9, "str", 8, 19, "test"]
    result_array = ["test", 19, 8, "str", 9, 6]

    assert test_array.reversed() == result_array


def test_reversed_random_array():
    random_array = [randint(54354, 6458668) for _ in range(100000)]
    result_array = list(reversed(random_array))

    assert random_array.reversed() == result_array


def test_reversed_empty_array():
    test_array = []
    result_array = []

    assert test_array.reversed() == result_array


def test_reversed_complex_array():
    test_array = [14, 1, [88, 99, 909, [98, 11]], "str", 34, ["str2", "str1", [list("str3"), 13, ["14", [19, 20], 16]]]]
    result_array = list(reversed(test_array))

    assert test_array.reversed() == result_array


def test_reversed_compare_to_reverse_with_cycle():
    test_array = [randint(36456, 475665) for _ in range(100000)]
    result_array = []
    for index in range(len(test_array) - 1, -1, -1):
        result_array.append(test_array[index])

    assert test_array.reversed() == result_array
