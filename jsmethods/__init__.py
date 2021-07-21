import gc
import ctypes
from . import list_methods


def add_method(builtin_class, method_name, method_function):
    patchable_builtin_class = gc.get_referents(builtin_class.__dict__)[0]

    patchable_builtin_class[method_name] = method_function

    ctypes.pythonapi.PyType_Modified(ctypes.py_object(builtin_class))


add_method(list, "map", list_methods.map_method)
add_method(list, "flat", list_methods.flat_method)
add_method(list, "foreach", list_methods.foreach_method)
add_method(list, "join", list_methods.join_method)
add_method(list, "filter", list_methods.filter_method)
add_method(list, "reversed", list_methods.reversed_method)
add_method(list, "find", list_methods.find_method)
add_method(list, "find_index", list_methods.find_index_method)
add_method(list, "reduce", list_methods.reduce_method)
add_method(list, "some", list_methods.some_method)
add_method(list, "every", list_methods.every_method)
