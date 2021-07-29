import pytest

import listchaining


def test_simple_every():
    def every_func(el):
        return el > 10

    test_array = [78, 14, 98, 45, 32, 71, 9 + 4]
    result = True

    assert test_array.every(every_func) == result


def test_every_method_based_on_array_index():
    def every_func(el, index):
        return el > index

    test_array = [67, 13, 23, 7, 34, 96, 11, 9, 232, 8, 15]
    result = False

    assert test_array.every(every_func) == result


# When the array is empty, the every method (like the 'all' function in python) always returns True
def test_every_method_on_empty_array():
    def every_func(el):
        return el is not None

    test_array = []
    result = True

    assert test_array.every(every_func) == result


def test_every_method_with_type_error():
    def every_func(el):
        return len(el) > 5

    test_array = [range(10), (5, 7, 9, 1, 4, 3), 67, {98, "str", "test", 4, 12}]
    result_error_string = "object of type 'int' has no len()"

    with pytest.raises(TypeError) as error_info:
        test_array.every(every_func)

    assert result_error_string in str(error_info.value)


def test_every_method_based_on_all_array():
    def every_func(el, _, array):
        mid = array[len(array) // 2]
        return el >= mid

    test_array = [55, 44, 13, 85, 89]
    result = True

    assert test_array.every(every_func) == result


def test_every_method_on_complex_array():
    def every_func(el, index):
        return el.get('server') and el['server'].get('id') and el['server']['id'] > index

    test_array = [{'server': {'id': 1, 'status': 'off', 'owner': 'Theo'}}, {'server': 'broken'}]
    result_error_string = "'str' object has no attribute 'get'"

    with pytest.raises(AttributeError) as error_info:
        test_array.every(every_func)

    assert result_error_string in str(error_info.value)
