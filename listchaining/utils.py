from inspect import getfullargspec


def get_function_positional_arguments_count(function):
    function_spec = getfullargspec(function)
    function_arguments_count = len(function_spec.args)

    has_function_default_arguments = function_spec.defaults is not None
    if has_function_default_arguments:
        function_arguments_count -= len(function_spec.defaults)

    return function_arguments_count
