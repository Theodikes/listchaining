import listchaining


def test_to_string_simple_array():
    test_array = [*range(2, 10, 2)]
    result_string = "2,4,6,8"

    assert test_array.to_string() == result_string


def test_to_string_nested_arrays():
    test_array = [5, [7, [list(range(5)), 8], 90], [9, 4, [55, 4]], 6]
    result_string = "5,7,0,1,2,3,4,8,90,9,4,55,4,6"

    assert test_array.to_string() == result_string


def test_to_string_empty_array():
    test_array = []
    result_string = ''

    assert test_array.to_string() == result_string


def test_to_string_complex_array():
    test_array = [15, "str", range, range(2), {'a': 'b'}, 25, (6, (66, 66), -6), 0.134]
    result_string = "15,str,<class 'range'>,range(0, 2),{'a': 'b'},25,(6, (66, 66), -6),0.134"

    assert test_array.to_string() == result_string
