import pytest

import listchaining


def test_simple_fill_full_array():
    test_array = [*range(10)]
    result_array = [1] * 10

    assert test_array.fill(1) == result_array


def test_fill_from_start_to_end():
    test_array = [5, 6, 1, "str", 8, 10]
    result_array = ["filled", "filled", "filled", "str", 8, 10]

    assert test_array.fill("filled", 0, 3) == result_array


def test_fill_without_end_parameter():
    test_array = [98, (5, 4, "y"), "x", 0, 1618, 13, *range(2, 5)]
    result_array = [98, (5, 4, "y"), "x", 55, 55, 55, 55, 55, 55]

    assert test_array.fill(55, 3) == result_array


def test_fill_empty_array():
    test_array = []

    assert test_array.fill("filled") == []


def test_fill_array_out_of_bounds():
    test_array = ["str", 18, 77, 65, 81, 9, 4]
    result_array = ["str", 18, 77, 65, 88, 88, 88]

    assert test_array.fill(88, 4, 8888) == result_array


def test_fill_array_start_index_is_greater_than_end():
    test_array = [77, 456, 65457, 2435, 244, "test", 11]

    assert test_array.fill(88, 4, 2) == test_array.copy()


def test_fill_not_modify_array_itself():
    test_array = list(range(2, 15, 2))
    test_array_copy = test_array.copy()

    assert test_array.fill(88) is not test_array and test_array == test_array_copy


def test_fill_without_value():
    test_array = [766, "test", *(5, 6, 3), 14, 9654]
    result_error_string = "missing 1 required positional argument: 'value'"

    with pytest.raises(TypeError) as error_info:
        test_array.fill()

    assert result_error_string in str(error_info.value)
