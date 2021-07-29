import pytest

import listchaining


def test_simple_last_index():
    test_array = [2, 4, 8, 16, 19, 4, 19, 45, 974, "str", 2 + 2, 11]
    result_index = 10

    assert test_array.last_index_of(4) == 10


def test_last_index_with_negative_from_index_parameter():
    test_array = [2, 4, 8, 16, 19, 4, 19, 45, 974, "str", 2 + 2, 11]
    from_index = -3
    result_index = 5

    assert test_array.last_index_of(4, from_index) == result_index


def test_last_index_with_positive_from_index_parameter():
    test_array = [2, 4, 8, 16, 19, 4, 19, 45, 974, "str", 2 + 2, 11]
    from_index = 4
    result_index = 1

    assert test_array.last_index_of(4, from_index) == result_index


def test_last_index_without_searched_element():
    test_array = [56, 73, 14, 135, 94, 82, 40, 38, 11, 58]
    searched_value = 27
    result_error_string = f"{searched_value} is not in list"

    with pytest.raises(ValueError) as error_info:
        test_array.last_index_of(searched_value)

    assert result_error_string in str(error_info.value)


def test_last_index_with_negative_from_index_parameter_out_array_bounds():
    test_array = [2, 4, 904, "test", 13, "test", 76, 11]
    searched_value = "test"
    from_index = -10000
    result_error_string = f"'{searched_value}' is not in list"

    with pytest.raises(ValueError) as error_info:
        test_array.last_index_of(searched_value, from_index)

    assert result_error_string in str(error_info.value)


def test_last_index_with_positive_from_index_parameter_out_array_bounds():
    test_array = [2, 4, 904, "test", 13, "test", 76, 11]
    searched_value = "test"
    from_index = 10000
    result_index = 5

    assert test_array.last_index_of(searched_value, from_index) == result_index


def test_last_index_without_searched_value():
    test_array = [*range(2, 10)]
    result_error_string = "last_index_of_method() missing 1 required positional argument: 'element'"

    with pytest.raises(TypeError) as error_info:
        test_array.last_index_of()

    assert result_error_string in str(error_info.value)


def test_last_index_on_complex_array():
    test_array = [7, [list(range(2, 5)) for _ in range(10)], {'a': 'b'}, f"test{55 + 14}", {7, 8, 14}, str(8.8),
                  (89, "str", [78, [13, 0], enumerate]), range, set, 45, "test", range, 14, 4, 66, range(3), int("11")]
    searched_element = range
    result_index = 11

    assert test_array.last_index_of(searched_element) == result_index
