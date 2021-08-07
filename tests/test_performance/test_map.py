import listchaining
from typing import Union, Callable
from random import randint, choices
from string import ascii_lowercase
from time import time
from .utils import check_result_of_multiple_runs, get_percentage_difference

random_array = [randint(144, 565666) for _ in range(randint(400000, 1000000))]

complex_random_array = [{"id": 2, "country": {"name": ''.join(choices(ascii_lowercase, k=randint(3, 8))), "population":
                                       randint(1434434, 56676778)}, "gone": False}
                        for _ in range(randint(400000, 1000000))]


def standard_map_func(element: int):
    return element ** 2 + 1


def map_func_based_on_element_index(element: int, index: int):
    return element + index * 2


def map_func_based_on_all_array(element: int, index: int, array: list[int]):
    return element + index + (array[index - 1] if index else 0)


def map_func_for_complex_array(element: dict):
    country_name = element['country']['name']
    element['country']['name'] = country_name[::-1]
    element['country']['length'] = len(country_name)

    return element


def get_map_method_execution_time(array: list, function: Callable) -> Union[float, int]:
    start_time = time()
    _ = array.map(function)
    map_method_execution_time = time() - start_time

    return map_method_execution_time


@check_result_of_multiple_runs(number_of_runs=50)
def test_compare_performance_map_method_to_cycle_simple_mapping() -> bool:
    map_method_execution_time = get_map_method_execution_time(random_array, standard_map_func)

    start_time = time()
    copy = []
    for element in random_array:
        copy.append(standard_map_func(element))
    simple_array_cycle_mapping_execution_time = time() - start_time

    is_map_method_faster = simple_array_cycle_mapping_execution_time > map_method_execution_time
    are_map_method_speed_and_cycle_speed_comparable = \
        get_percentage_difference(simple_array_cycle_mapping_execution_time, map_method_execution_time) < 15

    return is_map_method_faster or are_map_method_speed_and_cycle_speed_comparable


@check_result_of_multiple_runs(number_of_runs=50)
def test_compare_performance_map_method_with_indexes_to_cycle_mapping() -> bool:
    map_method_execution_time = get_map_method_execution_time(random_array, map_func_based_on_element_index)

    start_time = time()
    copy = []
    for index, element in enumerate(random_array):
        copy.append(map_func_based_on_element_index(element, index))
    cycle_mapping_based_on_element_index_execution_time = time() - start_time

    is_map_method_faster = cycle_mapping_based_on_element_index_execution_time > map_method_execution_time
    are_map_method_speed_and_cycle_speed_comparable = \
        get_percentage_difference(cycle_mapping_based_on_element_index_execution_time, map_method_execution_time) < 15

    return is_map_method_faster or are_map_method_speed_and_cycle_speed_comparable


@check_result_of_multiple_runs(number_of_runs=50)
def test_compare_performance_map_method_based_on_all_array_to_cycle_mapping() -> bool:
    map_method_execution_time = get_map_method_execution_time(random_array, map_func_based_on_all_array)

    start_time = time()
    copy = []
    for index, element in enumerate(random_array):
        copy.append(map_func_based_on_all_array(element, index, random_array))
    cycle_mapping_based_on_all_array_execution_time = time() - start_time

    is_map_method_faster = cycle_mapping_based_on_all_array_execution_time > map_method_execution_time
    are_map_method_speed_and_cycle_speed_comparable = \
        get_percentage_difference(cycle_mapping_based_on_all_array_execution_time, map_method_execution_time) < 15

    return is_map_method_faster or are_map_method_speed_and_cycle_speed_comparable


@check_result_of_multiple_runs(number_of_runs=50)
def test_compare_simple_map_method_performance_to_list_comprehension_mapping() -> bool:
    map_method_execution_time = get_map_method_execution_time(random_array, standard_map_func)

    start_time = time()
    _ = [standard_map_func(element) for element in random_array]
    list_comprehension_mapping_execution_time = time() - start_time

    is_map_method_faster = list_comprehension_mapping_execution_time > map_method_execution_time
    are_map_method_speed_and_list_comprehension_speed_comparable = \
        get_percentage_difference(list_comprehension_mapping_execution_time, map_method_execution_time) < 25

    return is_map_method_faster or are_map_method_speed_and_list_comprehension_speed_comparable


@check_result_of_multiple_runs(number_of_runs=50)
def test_compare_performance_map_method_with_indexes_to_list_comprehension_mapping() -> bool:
    map_method_execution_time = get_map_method_execution_time(random_array, map_func_based_on_element_index)

    start_time = time()
    _ = [map_func_based_on_element_index(element, index) for index, element in enumerate(random_array)]
    list_comprehension_mapping_indexes_execution_time = time() - start_time

    is_map_method_faster = list_comprehension_mapping_indexes_execution_time > map_method_execution_time
    are_map_method_speed_and_list_comprehension_speed_comparable = \
        get_percentage_difference(list_comprehension_mapping_indexes_execution_time, map_method_execution_time) < 15

    return is_map_method_faster or are_map_method_speed_and_list_comprehension_speed_comparable


@check_result_of_multiple_runs(number_of_runs=50)
def test_compare_performance_map_method_based_on_all_array_to_builtin_map() -> bool:
    map_method_execution_time = get_map_method_execution_time(random_array, map_func_based_on_all_array)

    start_time = time()
    _ = list(map(map_func_based_on_all_array, random_array, range(len(random_array)),
            [random_array for _ in range(len(random_array))]))
    builtin_map_execution_time = time() - start_time

    is_map_method_faster = builtin_map_execution_time > map_method_execution_time
    are_map_method_speed_and_builtin_map_speed_comparable = \
        get_percentage_difference(builtin_map_execution_time, map_method_execution_time) < 15

    return is_map_method_faster or are_map_method_speed_and_builtin_map_speed_comparable


@check_result_of_multiple_runs(number_of_runs=50)
def test_compare_map_method_to_cycle_on_complex_array():
    map_method_execution_time = get_map_method_execution_time(complex_random_array, map_func_for_complex_array)

    start_time = time()
    copy = []
    for element in complex_random_array:
        copy.append(map_func_for_complex_array(element))
    simple_array_cycle_mapping_execution_time = time() - start_time

    is_map_method_faster = simple_array_cycle_mapping_execution_time > map_method_execution_time
    are_map_method_speed_and_cycle_speed_comparable = \
        get_percentage_difference(simple_array_cycle_mapping_execution_time, map_method_execution_time) < 15

    return is_map_method_faster or are_map_method_speed_and_cycle_speed_comparable


@check_result_of_multiple_runs(number_of_runs=50)
def test_compare_map_method_to_list_comprehension_on_complex_array():
    map_method_execution_time = get_map_method_execution_time(complex_random_array, map_func_for_complex_array)

    start_time = time()
    _ = [map_func_for_complex_array(element) for element in complex_random_array]
    list_comprehension_mapping_execution_time = time() - start_time

    is_map_method_faster = list_comprehension_mapping_execution_time > map_method_execution_time
    are_map_method_speed_and_list_comprehension_speed_comparable = \
        get_percentage_difference(list_comprehension_mapping_execution_time, map_method_execution_time) < 15

    return is_map_method_faster or are_map_method_speed_and_list_comprehension_speed_comparable
