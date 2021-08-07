import listchaining
from time import time
from random import randint
from .utils import check_result_of_multiple_runs, get_percentage_difference

random_array = [randint(54454, 5443543557) for _ in range(randint(400000, 1000000))]


def get_entries_execution_time(array: list) -> float:
    start_time = time()
    _ = array.entries()
    entries_execution_time = time() - start_time

    return entries_execution_time


@check_result_of_multiple_runs(number_of_runs=100)
def test_compare_entries_performance_to_enumerate() -> bool:
    entries_execution_time = get_entries_execution_time(random_array)

    start_time = time()
    _ = list(enumerate(random_array))
    enumerate_execution_time = time() - start_time

    is_entries_method_faster_than_enumerate = enumerate_execution_time > entries_execution_time
    are_entries_method_speed_and_enumerate_speed_comparable = \
        get_percentage_difference(enumerate_execution_time, entries_execution_time) < 20

    return is_entries_method_faster_than_enumerate or are_entries_method_speed_and_enumerate_speed_comparable


@check_result_of_multiple_runs(number_of_runs=100)
def test_compare_entries_performance_to_cycle() -> bool:
    entries_execution_time = get_entries_execution_time(random_array)

    start_time = time()
    entries: list[tuple] = []
    for i in range(len(random_array)):
        entries.append((i, random_array[i]))
    cycle_execution_time = time() - start_time

    return cycle_execution_time > entries_execution_time
