import random

import pytest

import jsmethods


def test_simple_reduce():
    def reduce_func(acc, current_element):
        return acc + int(current_element)

    test_array = [1, "55", 4 + 2, len(list(range(20))), 89]
    result = 171

    assert test_array.reduce(reduce_func) == result


def test_reduce_with_initial_value():
    def reduce_func(acc, current_el):
        return acc - int(current_el)

    test_array = [565, 11, 34, f"5{7+2}", 94]
    initial_value = 10000
    result = 9237

    assert test_array.reduce(reduce_func, initial_value=initial_value) == result


def test_reduce_based_on_index():
    def reduce_func(acc, element, index):
        return acc + element + index

    test_array = [5, 14, 3, 28, 11, 0]
    result = 76

    assert test_array.reduce(reduce_func) == result


def test_reduce_based_on_all_array():
    def reduce_func(acc, element, _, array):
        mid_elem = array[len(array) // 2]
        return f"{acc} {mid_elem} {element}"

    test_array = ["str1", "str2", "test", "str3", f"str{2 + 2}"]
    result = "str1 test str2 test test test str3 test str4"

    assert test_array.reduce(reduce_func) == result


def test_reduce_insufficient_number_of_callback_parameters():
    def reduce_func(acc):
        return acc + 1

    test_array = [1, 4, 78, int("5"), 14]
    result_error_string = "Invalid number of positional arguments in 'reduce' function."

    with pytest.raises(ValueError) as error_info:
        test_array.reduce(reduce_func)

    assert result_error_string in str(error_info.value)


def test_complex_reduce():
    def reduce_func(acc, el):
        if not el.get('country') or not el['country'].get('population'):
            return acc

        acc['population'] += el['country']['population']
        return acc

    test_array = [{id: 1, 'country': {'name': 'Afganistan', 'population': 37171921}}, {id: 2, "status": "no info"},
                  {id: 3, 'country': {'name': 'Armenia', 'population': 2951745}}, {id: 3, 'country':
            {'name': 'Kazakhstan', 'population': 18319618}}, {id: 4, 'country':
            {'name': 'Kyrgyzstan', 'population': 6304030}}, {id: 5, 'country': {'name': "Tajikistan"}, "status": None}]
    initial_dict = {'Region': 'SNG-Asia', 'population': 0}
    test_result = test_array.reduce(reduce_func, initial_dict)
    result_population = 64747314

    assert test_result['population'] == result_population


def test_reduce_on_empty_array_with_initial_value():
    def reduce_func(acc, el):
        return acc + el

    test_array = []
    initial_value = 10

    assert test_array.reduce(reduce_func, initial_value) == initial_value


def test_reduce_on_empty_array_without_initial_value():
    def reduce_func(acc, el):
        return acc + el

    test_array = []
    result_error_string = "Reduce of empty array with no initial value."

    with pytest.raises(ValueError) as error_info:
        test_array.reduce(reduce_func)

    assert result_error_string in str(error_info.value)


def test_reduce_right():
    def reduce_right_func(acc, el):
        return acc - el

    test_array = [14, 15, 3, 4, 8, int('45'), 12]
    result = -77

    assert test_array.reduce_right(reduce_right_func) == result


def test_reduce_right_empty_array_with_initial_value():
    def reduce_right_func(acc, el):
        return acc + el

    test_array = []
    initial_value = 10

    assert test_array.reduce_right(reduce_right_func, initial_value) == initial_value


def test_reduce_on_random_array():
    def reduce_func(acc, el):
        return acc + el

    test_array = [random.randint(52454, 46787882) for _ in range(100000)]
    result = sum(test_array)

    assert test_array.reduce(reduce_func) == result


def test_reduce_equivalent_to_reduce_right():
    def reduce_func(acc, el):
        return acc + el

    test_array = [random.randint(52454, 46787882) for _ in range(100000)]

    assert test_array.reduce(reduce_func) == test_array.reduce_right(reduce_func)
