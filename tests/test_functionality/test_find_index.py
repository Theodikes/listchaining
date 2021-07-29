import listchaining


def test_find_index_simple():
    def find_index_func(el):
        return el > 10

    test_array = [1, 9, 4, 14, 8, 19]
    result_index = 3

    assert test_array.find_index(find_index_func) == result_index


def test_find_index_on_array_with_no_searched_element():
    def find_index_func(el):
        return type(el) is set

    test_array = [1, 5, "str", {'a': "b"}, 66, 7, (1, 3, 4), range(1, 5, 2), "test", [8, 9, {9, 0}]]
    result_index = -1

    assert test_array.find_index(find_index_func) == result_index


def test_compare_find_index_with_builtin_index_function():
    def find_index_func(el):
        return el == "test"

    test_array = ["str1", "find_index", 14, 1667, "TEst", [1, 3, 4], "test", 18, "teststring"]
    result_index = test_array.index("test")

    assert test_array.find_index(find_index_func) == result_index


def test_find_index_on_complex_strictures():
    def find_index_func(el):
        return type(el.get('userinfo')) == dict and el['userinfo'].get("login") == "Theo"

    test_array = [{id: 14, "userinfo": "undefined"}, {id: 1, "userinfo": {"login": "lancelot", "password": "qwerty"}},
                  {id: 5, "userinfo": {"login": "Theo", "password": "pwd"}}, {'empty': True, "userinfo": None}]
    result_index = 2

    assert test_array.find_index(find_index_func) == result_index


def test_find_index_based_on_element_index():
    def find_index_func(el, index):
        return el + index > 15

    test_array = [15, 14, 13, 2, 10, 11, 19, 98]
    result_index = 5

    assert test_array.find_index(find_index_func) == result_index


def test_find_index_based_on_all_array():
    def find_index_func(el, index, array):
        if index > 0 and el > array[index - 1]:
            return True
        return False

    test_array = [55, 18, 9, 56, 11, 12, 8, 0, 98]
    result_index = 3

    assert test_array.find_index(find_index_func) == result_index


def test_find_index_on_empty_array():
    def find_index_func(el, index):
        return el + index > 10

    test_array = []
    result_index = -1

    assert test_array.find_index(find_index_func) == result_index
