import jsmethods


def test_copy_within_simple_array():
    test_array = ['a', 'b', 'c', 'd', 'e']
    result_array = ["d", "b", "c", "d", "e"]

    assert test_array.copy_within(0, 3, 4) == result_array


def test_copy_within_without_start_parameter():
    test_array = [65, 43, "str", 4, 7]
    result_array = [65, 43, "str", 65, 43]

    assert test_array.copy_within(3) == result_array


def test_copy_within_intersecting_gaps():
    test_array = [65, 43, "str", 4, 7]
    result_array = [65, "str", 4, 4, 7]

    assert test_array.copy_within(1, 2, 4) == result_array


def test_copy_within_out_of_array_bounds():
    test_array = [65, 43, "str", 4, 7]
    result_array = [65, 65, 43, "str", 4]

    assert test_array.copy_within(1, 0, 1000) == result_array


def test_copy_within_not_modify_array_itself():
    test_array = [135, 45, 4, 3, 5]
    test_array_copy = test_array.copy()

    assert test_array.copy_within(3) is not test_array and test_array == test_array_copy
