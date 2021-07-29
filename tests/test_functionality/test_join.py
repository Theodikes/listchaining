import pytest

import jsmethods


def test_simple_join():
    test_array = ["str1", "str2", "test", "string3", "teststring"]
    result = 'str1 str2 test string3 teststring'

    assert test_array.join(' ') == result


def test_join_on_splitted_string():
    test_string = f"tip game life remove submit wear moon share company forum like pudding run useful prefer str{4 + 5}"
    test_array = test_string.split(' ')

    assert test_array.join(' ') == test_string


def test_join_on_int_value_without_cast_types():
    test_array = ["str", "4", 44, 78, "test"]
    result_error_string = "expected str instance, int found"

    with pytest.raises(TypeError) as error_info:
        test_array.join(' ')

    assert result_error_string in str(error_info.value)


def test_join_on_int_values_with_cast_types():
    test_array = ["str", "4", 44, 78, "test"]
    result_string = "str 4 44 78 test"

    assert test_array.join(' ', cast_types=True) == result_string


def test_join_with_complex_delimiter():
    test_array = ["Russia", "Ukraine", "UK", "USA", "Taiwan", "China"]
    delimiter = "\nNext country: "
    result = """Russia
Next country: Ukraine
Next country: UK
Next country: USA
Next country: Taiwan
Next country: China"""

    assert test_array.join(delimiter) == result


def test_join_array_with_cast_types():
    test_array = [range(5), [4, 14, 8], {8, 0, 5}, "str", 99, {'a': 'b'}]
    result_string = "range(0, 5); [4, 14, 8]; {8, 0, 5}; str; 99; {'a': 'b'}"

    assert test_array.join("; ", cast_types=True) == result_string


def test_join_empty_array():
    test_array = []
    result_string = ''

    assert test_array.join(", ") == result_string
