import jsmethods
import pytest


def test_simple_filter():
    def filter_func(el):
        return el > 10

    test_array = [2, 4, 5, 10, 17, 18, 19]
    result_array = [17, 18, 19]

    assert test_array.filter(filter_func) == result_array


def test_index_based_filter():
    def filter_func(_, index):
        return index % 2

    test_array = [2, 4, 5, 10, 17, 18, 19, 14, 98, 0]
    result_array = [4, 10, 18, 14, 0]

    assert test_array.filter(filter_func) == result_array


def test_filter_based_on_all_array():
    # We leave those elements that are inside an ascending sequence, that is,
    # elements that are larger than the previous one and less than the next
    def filter_func(el, index, array):
        if 0 < index < len(array) - 1:
            return array[index - 1] < el < array[index + 1]
        if index == 0:
            return el < array[index + 1]
        return el > array[index - 1]

    test_array = [2, 4, 3, 10, 17, 18, 19, 14, 98, 104]
    result_array = [2, 10, 17, 18, 98, 104]

    assert test_array.filter(filter_func) == result_array


def test_filter_on_complex_elements():
    def filter_func(el, index):
        if el.get('test') and el['test'].get('id') and el['test']['id'] >= index:
            return True
        return False

    test_array = [{'test': {}, 'empty': True}, {"test": {'id': 0, "payload": "password"}, 'empty': False},
                  {'test': {'id': 14, "payload": "login"}, 'skip': 1}, {'next': True}]
    result_array = [{'test': {'id': 14, "payload": "login"}, 'skip': 1}]

    assert test_array.filter(filter_func) == result_array


def test_filter_on_empty_array():
    def filter_func(el, idx):
        return bool(el + idx)

    test_array = []
    result_array = []

    assert test_array.filter(filter_func) == result_array


def test_filter_returning_nothing():
    def filter_func(el):
        pass

    test_array = [2, 4, 5, 10, 17, 18, 19]
    result_array = []

    assert test_array.filter(filter_func) == result_array


def test_filter_error_with_many_arguments():
    def filter_func(el, index, array, one_more_index):
        return el + index + one_more_index > len(array)

    test_array = [1, 55, 67, 99, 14, 82, "str"]
    result_error_string = "Invalid number of positional arguments in the mapping function"

    with pytest.raises(ValueError) as error_info:
        test_array.map(filter_func)

    assert result_error_string in str(error_info.value)


def test_filter_compare_type_error():
    def filter_func(el, _, array):
        return el > array[-1]

    test_array = [5, 55, 555, "5555", 755, 134, 0, 876]
    result_error_string = "not supported between instances of 'str' and 'int'"

    with pytest.raises(TypeError) as error_info:
        test_array.filter(filter_func)

    assert result_error_string in str(error_info.value)
