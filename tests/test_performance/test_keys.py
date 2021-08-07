import random
import string

import listchaining
from time import time
from typing import Union
from .utils import get_percentage_difference, check_result_of_multiple_runs


def get_keys_method_execution_time(array: list) -> Union[int, float]:
    start_time = time()
    _ = array.keys()
    keys_time_result = time() - start_time

    return keys_time_result


@check_result_of_multiple_runs(number_of_runs=20)
def test_compare_keys_performance_with_list_comprehension() -> bool:
    test_array = [89] * 5000000

    start_time = time()
    _ = [i for i in range(len(test_array))]
    comprehension_time_result = time() - start_time

    return get_keys_method_execution_time(test_array) < comprehension_time_result


@check_result_of_multiple_runs(number_of_runs=20)
def test_compare_keys_performance_with_cycle() -> bool:
    test_array = [random.randint(243, 5445)] * 5000000

    start_time = time()
    result_array = []
    for i in range(len(test_array)):
        result_array.append(i)
    cycle_time_result = time() - start_time

    return get_keys_method_execution_time(test_array) < cycle_time_result


@check_result_of_multiple_runs(number_of_runs=100)
def test_compare_keys_performance_to_call_list_function() -> bool:
    test_array = [random.choice(string.ascii_lowercase)] * 1000000

    keys_time = get_keys_method_execution_time(test_array)

    start_time = time()
    _ = list(range(len(test_array)))
    list_call_time = time() - start_time

    '''
    In fact, expanding an iterable using the '*' operator and explicitly converting to a list using the 'list()' call 
    take approximately the same time, so the difference between the execution time of the method and the expanding 
    should not exceed 20% of the total time.
    '''
    return list_call_time > keys_time or get_percentage_difference(keys_time, list_call_time) < 20
