import random

import jsmethods


def test_concat_not_modifiyng_self_array():
    test_array = [14, "str", jsmethods.__file__, (1, 4, 5), 13, "test"]
    test_array_copy = test_array.copy()
    test_array.concat([35, 242, 78, 90], [78, "teststring", {'a': 'b'}, 17], [[[15]]])

    assert test_array == test_array_copy


def test_concat_one_array():
    test_array = [67, 13, 4, 89, 56, 23, 90]
    array_to_concatenate = [89, 13, 67, "gorilla", range(5)]
    result = [67, 13, 4, 89, 56, 23, 90, 89, 13, 67, "gorilla", range(5)]

    assert test_array.concat(array_to_concatenate) == result


def test_concat_multiple_arrays():
    test_array = ["test", 17, 19, (4, 5, 6)]
    a1, a2, a3 = list(range(4)), [{'a': 'b'}, 15], ["str", int("14"), 16.2]
    result = ["test", 17, 19, (4, 5, 6), 0, 1, 2, 3, {'a': 'b'}, 15, "str", 14, 16.2]

    assert test_array.concat(a1, a2, a3) == result


def test_concat_empty_array():
    test_array = []
    array_to_concatenate = [576, 12, 15, "str"]

    assert test_array.concat(array_to_concatenate) == array_to_concatenate


def test_concat_with_empty_arrays():
    test_array = [random.randint(1343, 57687856) for _ in range(100000)]
    a1, a2, a3 = [], [], []

    assert test_array.concat(a1, a2, a3) == test_array


def test_concat_with_random_arrays():
    test_array = [[random.randint(1343, 57687856) for _ in range(100000)]]
    a1, a2, a3 = [[random.randint(1343, 57687856) for _ in range(100000)] for _ in range(3)]
    result_array = [*test_array, *a1, *a2, *a3]

    assert test_array.concat(a1, a2, a3) == result_array


def test_concat_with_not_array_args():
    test_array = list(range(1, 10, 2))
    arg1, arg2, arg3, arg4 = [5, 4, 4], "str test", (5, 6, 3), 14
    result_array = [1, 3, 5, 7, 9, 5, 4, 4, "str test", 5, 6, 3, 14]

    assert test_array.concat(arg1, arg2, arg3, arg4) == result_array


def test_concat_with_other_iterable():
    test_array = [6, 1, 5, "test"]
    args = [range(3), enumerate(range(2, 6)), {'a': 'some_info_not_added'}, ["test", "str"], (5, 8, 1)]
    result = [6, 1, 5, "test", 0, 1, 2, (0, 2), (1, 3), (2, 4), (3, 5), 'a', "test", "str", 5, 8, 1]

    assert test_array.concat(*args) == result


def test_concat_with_string_expanding():
    test_array = [5, "str"]
    args = ["str2", "test"]
    result = [5, "str", "s", "t", "r", "2", "t", "e", "s", "t"]

    assert test_array.concat(*args, expand_strings=True) == result
