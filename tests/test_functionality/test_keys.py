import random

import listchaining


def test_keys_compare_with_list_comprehension():
    test_array = [random.randint(3353, 64456565) for _ in range(100000)]
    result_array = [i for i in range(len(test_array))]

    assert test_array.keys() == result_array


def test_keys_compare_with_cycle():
    test_array = [random.randint(3353, 64456565) for _ in range(100000)]
    result_array = []
    for i in range(len(test_array)):
        result_array.append(i)

    assert test_array.keys() == result_array


def test_keys_compare_with_list_call():
    test_array = [random.randint(3353, 64456565) for _ in range(100000)]
    result_array = list(range(len(test_array)))

    assert test_array.keys() == result_array
