import pytest

import listchaining


def test_simple_some():
    def some_func(el):
        return el > 10

    test_array = [9, 0, 90, 90, 90, 50]
    result = True

    assert test_array.some(some_func) == result


def test_some_error():
    def some_func(el):
        return el > 10

    test_array = [9, 0, "teststring", 14, 78, [9, 44, 19]]
    result_error_string = "not supported between instances of 'str' and 'int'"

    with pytest.raises(TypeError) as exception_info:
        test_array.some(some_func)

    assert result_error_string in str(exception_info.value)


def test_some_based_on_index():
    def some_func(el, index):
        return el + index > 100

    test_array = [99, 50, 14, 54, 98, 16, 23]
    result = True

    assert test_array.some(some_func) == result


def test_some_without_suitable_elements_in_array():
    def some_func(el):
        return len(el) > 10

    test_array = [range(5), "test", "string", [1, 5, 6, 94355], dict.values({1: 2, 4: 5, 'a': None})]
    result = False

    assert test_array.some(some_func) == result


def test_some_based_on_all_array():
    def some_func(el, _, array):
        return el > array[-1]

    test_array = [5, 89, 14, 9, 13, 1546, int("67"), 1346 + 500]
    result = False

    assert test_array.some(some_func) == result


def test_some_complex_array():
    def some_func(el, index):
        return index and el['country']['population'] > 15

    test_array = [{'id': 110, "country": {'name': 'Russia', 'population': 146}, "test": False},
                  {'id': 1, "country": {'name': 'Singapore', 'population': 5}}, {"country": {'population': 10}}]
    result = False

    assert test_array.some(some_func) == result


def test_some_complex_array_error():
    def some_func(el):
        return el['country']['population'] > 15

    test_array = [{'id': 1, "country": {'name': 'Singapore', 'population': 5}}, {"country": {'population': 10}},
                  {'id': 11, "country": {'name': "USA"}}]
    result_error_field = 'population'

    with pytest.raises(KeyError) as error_info:
        test_array.some(some_func)

    assert result_error_field in str(error_info.value)


def test_some_complex_array_returning_without_error():
    def some_func(el):
        return el['country']['population'] > 15

    test_array = [{'id': 1, "country": {'name': 'Singapore', 'population': 5}}, {"country": {'population': 20}},
                  {'id': 11, "country": {'name': "USA"}}]
    result = True

    assert test_array.some(some_func) == result


def test_some_method_on_empty_array():
    def some_func(el):
        return el is None

    test_array = []
    result = False

    assert test_array.some(some_func) == result