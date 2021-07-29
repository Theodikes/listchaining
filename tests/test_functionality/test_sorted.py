import random

import pytest

import listchaining


def test_simple_sorted():
    test_array = [8, 134, 8.3, 0, 45, -1, 34]
    result_array = [-1, 0, 8, 8.3, 34, 45, 134]

    assert test_array.sorted() == result_array


def test_sorted_not_modify_array_itself():
    test_array = [56, 74575, 243, 757, 3443, 24]

    assert test_array.sorted() is not test_array


def test_sorted_non_numeric_values():
    test_array = ["str1", "test", "str2", "first", "last?", "str3"]
    result_array = ["first", "last?", "str1", "str2", "str3", "test"]

    assert test_array.sorted() == result_array


def test_sorted_random_array():
    test_array = [random.randint(32453, 435454353) for _ in range(10000)]
    result_array = test_array.copy()
    result_array.sort()

    assert test_array.sorted() == result_array


def test_sorted_with_reverse_parameter():
    test_array = [random.randint(32453, 435454353) for _ in range(10000)]
    result_array = test_array.copy()
    result_array.sort()

    assert test_array.sorted(reverse=True) == list(reversed(result_array)) == result_array[::-1]


def test_sorted_with_key_parameter():
    test_array = [{'name': "Russia", 'population': 146}, {'name': "Japan", 'population': 127},
                  {'name': "Israel", 'population': 9}, {'name': "USA", 'population': 328}]
    key_func = lambda country: country['population']
    result_array = [{'name': "Israel", 'population': 9}, {'name': "Japan", 'population': 127},
                    {'name': "Russia", 'population': 146}, {'name': "USA", 'population': 328}]

    assert test_array.sorted(key=key_func) == result_array


def test_sorted_with_wrong_named_parameters():
    test_array = [54, 76, 435, 34, 655, 11, 46, 0, 5.7]
    result_error_string = "'sort_func' is an invalid keyword argument"

    with pytest.raises(TypeError) as error_info:
        test_array.sorted(sort_func=lambda x, y: x - y)

    assert result_error_string in str(error_info.value)


def test_sorted_array_with_not_comparable_elements():
    test_array = [45, "55", 6, (1, 4, 3), 554]
    result_error_string = "'<' not supported between instances of 'str' and 'int'"

    with pytest.raises(TypeError) as error_info:
        test_array.sorted()

    assert result_error_string in str(error_info.value)


def test_sorted_empty_array():
    test_array = []

    assert test_array.sorted(key=lambda el: el['some_key_not_exist']) == []
