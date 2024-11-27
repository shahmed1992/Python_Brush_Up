def get_methods(obj):
    """Get methods available for various built in types """
    methods = []
    for method in dir(obj):
        if method.startswith("__"):
            pass
        else:

            methods.append(method)
    return methods

"""Methods of String"""
str_methods = get_methods(str)
# print(str_methods)
"""
    Output:
    ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 
    'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 
    'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 
    'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 
    'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 
    'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
    
"""

"""List Methods"""
list_methods = get_methods(list)
print(list_methods)
"""
    output:
    ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
"""

"""Set Methods"""
set_methods = get_methods(set)
print(set_methods)
"""
    Output:
    ['add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 
    'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
"""

""" Frozen set"""
# frozen set in Python  are immutable and can not be modified after the creation.
fruits = frozenset(["apple", "banana", "orange"])
print(fruits)
fruits.add("cherry") # AttributeError
print(fruits)

""" Tuple Methods"""
tuple_methods = get_methods(tuple)
print(tuple_methods)
"""
    Output:
    ['count', 'index']
"""

"""Dictionary Methods"""
dict_methods = get_methods(dict)
print(dict_methods)
"""
    Output:
        ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

"""

