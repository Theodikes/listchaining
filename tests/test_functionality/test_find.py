import jsmethods


def test_simple_find():
    def find_func(el):
        return type(el) is str

    test_array = [5, 8, 1, "test", 19, 0]
    result = "test"

    assert test_array.find(find_func) == result


def test_find_nothing():
    def find_func(el):
        pass

    test_array = [5, 8, 1, "test", 19, 0, {'a': 'b'}, {5, 8, "s"}]
    result = None

    assert test_array.find(find_func) == result


def test_find_by_index():
    def find_func(_, index):
        return index > 10

    test_array = list(range(15))
    result = 11

    assert test_array.find(find_func) == result


def test_find_by_all_array():
    def find_func(el, index, array):
        if index > 0 and index > len(array) // 2 and el > array[index - 1]:
            return True
        return False

    test_array = [55, 67, 97, 56, 11,  12, 8, 0, 98]
    result = 12

    assert test_array.find(find_func) == result


def test_find_on_strings_array():
    test_array = ['str', "Test", "tEST", 'Mexico', "ENGlISH", 'PEPSI-COLA', "USA"]
    result = "PEPSI-COLA"

    assert test_array.find(str.isupper) == result
