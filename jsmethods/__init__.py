import gc
import ctypes
from . import list_methods
from inspect import getmembers, isfunction


def add_method(builtin_class, method_name, method_function):
    patchable_builtin_class = gc.get_referents(builtin_class.__dict__)[0]

    patchable_builtin_class[method_name] = method_function

    ctypes.pythonapi.PyType_Modified(ctypes.py_object(builtin_class))


all_list_methods = getmembers(list_methods, isfunction)
for method_name, method_function in all_list_methods:
    add_method(list, method_name[:-7], method_function)

