import listchaining
import math


def test_standard_flat():
    test_array = [1, 2, {"Content-type": "application/json"}, ['str1', "str2", f"str{3}"], [2, [2, 3]], list(range(5))]
    result_array = [1, 2, {"Content-type": "application/json"}, "str1", "str2", "str3", 2, [2, 3], 0, 1, 2, 3, 4]
    assert test_array.flat() == result_array


def test_flat_with_depth_parameter():
    depth = 2
    test_array = [1, "1", [4, 5, [0, 2, list(range(5)), 8, 8], 99, 5], 77,
                  [56, 44, [14, 13, [12, 0]]]]
    result_array = [1, "1", 4, 5, 0, 2, list(range(5)), 8, 8, 99, 5, 77, 56, 44, 14, 13, [12, 0]]
    assert test_array.flat(depth) == result_array


def test_flat_deep_nesting():
    test_array = [14, 1, [88, 99, 909, [98, 11]], "str", 34, ["str2", "str1", [list("str3"), 13, ["14", [19, 20], 16]]]]
    result_array = [14, 1, 88, 99, 909, 98, 11, "str", 34, "str2", "str1", "s", "t", "r", "3", 13, "14", 19, 20, 16]
    assert test_array.flat(math.inf) == result_array


# The flat method should not "expand" other iterables - only lists
def test_flat_with_other_iterable():
    test_array = [1, (4, 5, 6), 89, 41, {3, 4, 5}, [77, 55, 5], 5, {4: 6, 8: 9}, 90]
    result_array = [1, (4, 5, 6), 89, 41, {3, 4, 5}, 77, 55, 5, 5, {4: 6, 8: 9}, 90]

    assert test_array.flat() == result_array


# Float value must be rounded down to the nearest integer
def test_flat_with_float_depth_parameter():
    depth = 2.5
    test_array = [1, "1", [4, 5, [0, 2, list(range(5)), 8, 8], 99, 5], 77,
                  [56, 44, [14, 13, [12, 4, ["str", 0, 9]], 88, "test"]], 11]
    result_array = [1, "1", 4, 5, 0, 2, list(range(5)), 8, 8, 99, 5, 77, 56, 44, 14, 13,
                    [12, 4, ["str", 0, 9]], 88, "test", 11]

    assert test_array.flat(depth) == result_array
