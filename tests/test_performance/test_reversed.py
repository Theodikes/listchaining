import listchaining
from random import randint
from time import time
from typing import Union
from .utils import check_result_of_multiple_runs, get_percentage_difference


random_array = [randint(53454, 6565656) for _ in range(randint(1000000, 2000000))]


def get_reversed_method_execution_time(array: list) -> Union[int, float]:
    start_time = time()
    _ = array.reversed()
    reverse_time_result = time() - start_time

    return reverse_time_result


@check_result_of_multiple_runs(number_of_runs=20)
def test_compare_performance_reversed_method_with_cycle() -> bool:
    reversed_method_execution_time = get_reversed_method_execution_time(random_array)

    start_time = time()
    copy = []
    for x in range(len(random_array) - 1, -1, -1):
        copy.append(x)
    cycle_time = time() - start_time

    return cycle_time > reversed_method_execution_time


@check_result_of_multiple_runs(number_of_runs=50)
def test_compare_performance_reversed_method_with_builtin_reversed() -> bool:
    reversed_method_execution_time = get_reversed_method_execution_time(random_array)

    start_time = time()
    _ = list(reversed(random_array))
    builtin_reversed_execution_time = time() - start_time

    is_reversed_method_faster_than_builtin = builtin_reversed_execution_time > reversed_method_execution_time
    are_reversed_method_speed_and_builtin_reversed_speed_comparable = \
        get_percentage_difference(reversed_method_execution_time, builtin_reversed_execution_time) < 10

    return is_reversed_method_faster_than_builtin or are_reversed_method_speed_and_builtin_reversed_speed_comparable


@check_result_of_multiple_runs(number_of_runs=50)
def test_compare_performance_reversed_method_with_list_reverse_on_big_array() -> bool:
    reversed_method_execution_time = get_reversed_method_execution_time(random_array)

    start_time = time()
    copy = random_array.copy()
    copy.reverse()
    list_reverse_execution_time = time() - start_time

    return list_reverse_execution_time > reversed_method_execution_time


@check_result_of_multiple_runs(number_of_runs=20)
def test_compare_performance_reversed_method_with_list_comprehension() -> bool:
    reversed_method_execution_time = get_reversed_method_execution_time(random_array)

    start_time = time()
    _ = [element for element in reversed(random_array)]
    list_comprehension_with_builtin_reversed_execution_time = time() - start_time

    start_time = time()
    _ = [random_array[index] for index in range(len(random_array) - 1, -1, -1)]
    list_comprehension_with_indexing_by_range_execution_time = time() - start_time

    is_reversed_method_faster_than_comprehension = min(list_comprehension_with_builtin_reversed_execution_time,
                                                       list_comprehension_with_indexing_by_range_execution_time,
                                                       reversed_method_execution_time) == reversed_method_execution_time

    return is_reversed_method_faster_than_comprehension
