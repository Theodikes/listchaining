import pytest

import jsmethods
import random


def test_simple_slice():
    test_array = [2, 6, 4, 99, "str", 75, "test"]
    result_array = [4, 99, "str"]

    assert test_array.slice(2, 5) == result_array


def test_slice_without_end_parameter():
    test_array = [784, 355, (7, "str test", 88), {'a': "undefined"}, False, 90]
    result_array = [{'a': "undefined"}, False, 90]

    assert test_array.slice(3) == result_array


def test_slice_returning_copy():
    test_array = [784, 355, (7, "str test", 88), {'a': "undefined"}, False, 90]
    test_array_copy = test_array.copy()

    assert test_array.slice() == test_array_copy and test_array.slice() is not test_array


def test_slice_with_float_parameters():
    test_array = [89, 45, 13, *list(range(5))]
    result_error_string = "slice indices must be integers or None"

    with pytest.raises(TypeError) as error_info:
        test_array.slice(2.5, 4.3)

    assert result_error_string in str(error_info.value)


def test_slice_out_of_array_bounds():
    test_array = [7, "test", 454, 466, 11, 4]

    assert test_array.slice(0, 544545) == test_array


def test_slice_start_bigger_than_end():
    test_array = [random.randint(4554, 65656) for i in range(32232)]

    assert test_array.slice(200, 100) == []
