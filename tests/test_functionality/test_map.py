import pytest

import listchaining
from random import randint


def test_map_standard():
    def map_func(el):
        return el * 3

    test_array = [2, 4, 5, 8, 9]
    result_array = [6, 12, 15, 24, 27]

    assert test_array.map(map_func) == result_array


def test_map_with_index():
    def map_func(el, index):
        return el + index

    test_array = [2, 4, 5, 8, 9]
    result_array = [2, 5, 7, 11, 13]

    assert test_array.map(map_func) == result_array


def test_map_with_array():
    def map_func(el, index, array):
        return el + index + array[(len(array) - 1) // 2]

    test_array = [2, 4, 5, 8, 9]
    result_array = [7, 10, 12, 16, 18]

    assert test_array.map(map_func) == result_array


def test_map_with_random_array():
    def map_func(el, index, array):
        return el + index + array[(len(array) - 1) // 2]

    random_array = [randint(1432, 4657677) for _ in range(100000)]
    mid_element = random_array[(len(random_array) - 1) // 2]
    result_array = list(map(lambda el, i, mid: el + i + mid, random_array, range(len(random_array)),
                            [mid_element for _ in range(len(random_array))]))

    assert random_array.map(map_func) == result_array


def test_map_with_strings():
    test_array = ["STR", "TeStStRinG", "GuN", "USA"]
    result_array = ["str", "teststring", "gun", "usa"]

    assert test_array.map(str.lower) == result_array


def test_map_with_complex_structure_array():
    def map_func(el):
        return el.get('payload') or False

    test_array = [{'id': 1, 'payload': "yuj.ioh"}, {'id': 448}, {'id': 3, 'payload': "teststring"}, {'id': 2}]
    result_array = ["yuj.ioh", False, "teststring", False]

    assert test_array.map(map_func) == result_array


def test_map_error_with_many_arguments():
    def map_func(el, index, array, one_more_index):
        return el + index + len(array) + one_more_index

    test_array = [1, 55, 67, 99, 14, 82, "str"]
    result_error_string = "Invalid number of positional arguments in the mapping function"

    with pytest.raises(ValueError) as error_info:
        test_array.map(map_func)

    assert result_error_string in str(error_info.value)


def test_map_argument_order_error():
    def map_func(index, el, array):
        return el + array[index]

    test_array = [7, 10, 6, 8, 4, 0, 4, 1, 3, 5, 11, 6, "str", 13, 2, 3, 1, 1, 1, 0]
    result_error_string = "list indices must be integers or slices, not str"

    with pytest.raises(TypeError) as error_info:
        test_array.map(map_func)

    assert result_error_string in str(error_info.value)


def test_map_modifiyng_self():
    def map_func(el):
        return el + 15

    test_array = [randint(435, 65567) for _ in range(100000)]
    test_array_copy = test_array.copy()
    test_array.map(map_func)

    assert test_array == test_array_copy
