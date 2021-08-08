import string

import pytest

import listchaining
from random import randint, choice, choices
from time import time
from .utils import check_result_of_multiple_runs, get_percentage_difference
from typing import List, Any


random_array = [randint(1, 600000) for _ in range(randint(4000000, 6000000))]
random_strings_array = [choices(string.ascii_letters, k=1500) for _ in range(100000)]


def get_last_index_of_execution_time(array: List, element: Any) -> float:
    start_time = time()
    _ = array.last_index_of(element)
    last_index_of_execution_time = time() - start_time

    return last_index_of_execution_time


def get_element_from_array_beginning(array: List):
    return array[randint(0, max(10, len(array) // 10))]


@check_result_of_multiple_runs(number_of_runs=100)
def test_compare_last_index_method_performance_to_builtin_index_with_reversed_array() -> bool:
    searched_element = choice(random_array)
    last_index_of_execution_time = get_last_index_of_execution_time(random_array, searched_element)

    start_time = time()
    _ = len(random_array) - random_array[-1::-1].index(searched_element) - 1
    builtin_index_method_on_reversed_array_execution_time = time() - start_time

    is_last_index_method_faster = builtin_index_method_on_reversed_array_execution_time > last_index_of_execution_time

    return is_last_index_method_faster


@check_result_of_multiple_runs(number_of_runs=50)
def test_compare_last_index_method_performance_to_reversed_enumerate() -> bool:
    searched_element = choice(random_array)
    last_index_of_execution_time = get_last_index_of_execution_time(random_array, searched_element)

    start_time = time()
    _ = -1
    for index, element in reversed(list(enumerate(random_array))):
        if element == searched_element:
            _ = index
            break
    reversed_enumerate_execution_time = time() - start_time

    is_last_index_method_faster = reversed_enumerate_execution_time > last_index_of_execution_time

    return is_last_index_method_faster


@check_result_of_multiple_runs(number_of_runs=50)
def test_compare_last_index_method_performance_to_cycle_performance_of_large_strings_array():
    searched_element = get_element_from_array_beginning(random_strings_array)
    last_index_of_execution_time = get_last_index_of_execution_time(random_strings_array, searched_element)

    start_time = time()
    _ = -1
    for index in range(len(random_strings_array) - 1, -1, -1):
        if random_strings_array[index] == searched_element:
            _ = index
            break
    cycle_execution_time = time() - start_time

    is_last_index_method_faster = cycle_execution_time > last_index_of_execution_time
    are_last_index_method_execution_speed_and_cycle_execution_speed_comparable = \
        get_percentage_difference(cycle_execution_time, last_index_of_execution_time) < 15

    return is_last_index_method_faster or are_last_index_method_execution_speed_and_cycle_execution_speed_comparable
