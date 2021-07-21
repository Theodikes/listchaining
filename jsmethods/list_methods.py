import functools

from .utils import get_function_positional_arguments_count


def map_method(self, function):
    mapping_function_arguments_count = get_function_positional_arguments_count(function)

    if mapping_function_arguments_count == 0 or mapping_function_arguments_count > 3:
        raise ValueError("Invalid number of positional arguments in the mapping function")

    if mapping_function_arguments_count == 1:
        return list(map(function, self))
    elif mapping_function_arguments_count == 2:
        return list(map(function, self, range(len(self))))
    elif mapping_function_arguments_count == 3:
        return [function(el, i, self) for i, el in enumerate(self)]


def filter_method(self, function):
    filter_function_arguments_count = get_function_positional_arguments_count(function)

    if filter_function_arguments_count == 0 or filter_function_arguments_count > 3:
        raise ValueError("Invalid number of positional arguments in the filter function")

    if filter_function_arguments_count == 1:
        return list(filter(function, self))
    elif filter_function_arguments_count == 2:
        return [function(el, i) for i, el in enumerate(self)]
    elif filter_function_arguments_count == 3:
        return [function(el, i, self) for i, el in enumerate(self)]


def foreach_method(self, function):
    foreach_function_arguments_count = get_function_positional_arguments_count(function)

    if foreach_function_arguments_count == 0 or foreach_function_arguments_count > 3:
        raise ValueError("Invalid number of positional arguments in the foreach function")

    if foreach_function_arguments_count == 1:
        for element in self:
            function(element)
    elif foreach_function_arguments_count == 2:
        for index, element in enumerate(self):
            function(element, index)
    elif foreach_function_arguments_count == 3:
        for index, element in enumerate(self):
            function(element, index, self)

    return None


def find_method(self, function):
    find_function_arguments_count = get_function_positional_arguments_count(function)

    if find_function_arguments_count == 0 or find_function_arguments_count > 3:
        raise ValueError("Invalid number of positional arguments in the 'find' function. The passed callback function"
                         " can have three positional arguments: the current element of the array, the index of the"
                         " current element, and the entire array.")

    if find_function_arguments_count == 1:
        for element in self:
            if function(element):
                return element

    elif find_function_arguments_count == 2:
        for index, element in enumerate(self):
            if function(element, index):
                return element

    elif find_function_arguments_count == 3:
        for index, element in enumerate(self):
            if function(element, index, self):
                return element

    return None


def find_index_method(self, function):
    find_index_function_arguments_count = get_function_positional_arguments_count(function)

    if find_index_function_arguments_count not in (2, 3):
        raise ValueError("Invalid number of positional arguments in the 'find_index' function. The passed callback"
                         " function can have three positional arguments: the current element of the array, the index"
                         " of the current element, and the entire array.")

    if find_index_function_arguments_count == 2:
        for index, element in enumerate(self):
            if function(element, index):
                return index

    elif find_index_function_arguments_count == 3:
        for index, element in enumerate(self):
            if function(element, index, self):
                return index

    return -1


def some_method(self, function):
    some_method_function_arguments_count = get_function_positional_arguments_count(function)

    if some_method_function_arguments_count == 0 or some_method_function_arguments_count > 3:
        raise ValueError("Invalid number of positional arguments in the 'some' function. The passed callback function"
                         " can have three positional arguments: the current element of the array, the index of the"
                         " current element, and the entire array.")

    if some_method_function_arguments_count == 1:
        for element in self:
            if function(element):
                return True

    elif some_method_function_arguments_count == 2:
        for index, element in enumerate(self):
            if function(element, index):
                return True

    elif some_method_function_arguments_count == 3:
        for index, element in enumerate(self):
            if function(element, index, self):
                return True

    return False


def every_method(self, function):
    every_method_function_arguments_count = get_function_positional_arguments_count(function)

    if every_method_function_arguments_count == 0 or every_method_function_arguments_count > 3:
        raise ValueError("Invalid number of positional arguments in the 'every' function. The passed callback function"
                         " can have three positional arguments: the current element of the array, the index of the"
                         " current element, and the entire array.")

    if every_method_function_arguments_count == 1:
        for element in self:
            if not function(element):
                return False

    elif every_method_function_arguments_count == 2:
        for index, element in enumerate(self):
            if not function(element, index):
                return False

    elif every_method_function_arguments_count == 3:
        for index, element in enumerate(self):
            if not function(element, index, self):
                return False

    return True


def flat_method(self, depth=1):
    flatten = []

    def flat(arr, flat_depth):
        for element in arr:
            if type(element) is list and flat_depth > 0:
                flat(element, flat_depth - 1)
            else:
                flatten.append(element)

    flat(self, depth)

    return flatten


def join_method(self, delimiter, cast_types=False):
    """
    Since JavaScript has automatic typecasting to a string and it usually works correctly, but Python does not have such
    functionality, I decided to add an additional parameter that determines whether all array elements will be cast
    to a string type when concatenated.
    """

    if cast_types:
        stringified_array = list(map(lambda element: str(element), self))
        return delimiter.join(stringified_array)

    return delimiter.join(self)


def reversed_method(self):
    return self[::-1]


def reduce_method(self, function, initial_value=None):
    if initial_value:
        return functools.reduce(function, self, initial_value)

    return functools.reduce(function, self)