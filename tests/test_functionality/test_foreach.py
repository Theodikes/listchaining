import jsmethods


def test_simple_foreach(capfd):
    def foreach_func(el):
        print(el, end=" ")

    test_array = [1, 5, 7, 19, "str", None]
    test_array.foreach(foreach_func)
    test_result, err = capfd.readouterr()
    result = "1 5 7 19 str None"

    assert test_result.strip() == result


def test_objects_print_foreach(capfd):
    def foreach_func(el):
        print(el, end=" ")

    test_array = [(7, 8, 6), [{'a': 'test'}, ("b", 22)], [90, False, 100]]
    test_array.foreach(foreach_func)
    test_result, err = capfd.readouterr()
    result = "(7, 8, 6) [{'a': 'test'}, ('b', 22)] [90, False, 100]"

    assert test_result.strip() == result


def test_foreach_with_stringify_objects(capfd):
    def foreach_func(el):
        print(str(el), end=" ")

    test_array = [(7, 8, 6), [{'a': 'test'}, ["b", 22]], [90, False, 100]]
    test_array.foreach(foreach_func)
    test_result, err = capfd.readouterr()
    result = "(7, 8, 6) [{'a': 'test'}, ['b', 22]] [90, False, 100]"

    assert test_result.strip() == result


def test_foreach_based_on_array_index(capfd):
    def foreach_func(el, i):
        print(el + i * 2, end=" ")

    test_array = [15, 19, 5, 3, 2676, 76]
    test_array.foreach(foreach_func)
    test_result, err = capfd.readouterr()
    result = "15 21 9 9 2684 86"

    assert test_result.strip() == result


def test_foreach_based_on_all_array(capfd):
    def foreach_func(el, i, arr):
        print(el + i + len(arr) + arr[len(arr) // 2], end=" ")

    test_array = [15, 19, 5, 3, 2676, 76]
    test_array.foreach(foreach_func)
    test_result, err = capfd.readouterr()
    result = "24 29 16 15 2689 90"

    assert test_result.strip() == result
