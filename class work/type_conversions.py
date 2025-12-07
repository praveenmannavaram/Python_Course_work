"""
===========================================
PYTHON TYPE CONVERSIONS (TYPE CASTING)
===========================================

This program demonstrates:
1. Implicit Type Conversion
2. Explicit Type Conversion
3. Integer, Float, String, List, Tuple, Set, Dictionary, Boolean, and Complex conversions
4. Valid and invalid conversions
5. Truthy and Falsy values
"""

print("\n========== IMPLICIT TYPE CONVERSION ==========\n")

a = 10
b = 2.5
c = a + b   # int + float -> float

print("a =", a, "type:", type(a))
print("b =", b, "type:", type(b))
print("a + b =", c, "type:", type(c))


print("\n========== EXPLICIT TYPE CONVERSION ==========\n")

print("Built-in conversion functions:")
print("int(), float(), str(), list(), tuple(), set(), dict(), bool(), complex()")


# ------------------------------------------------
# ✅ INTEGER TYPE CONVERSIONS
# ------------------------------------------------
print("\n========== INTEGER TYPE CONVERSION ==========\n")

a = 10
print("Original value:", a, "type:", type(a))

print("int to float:", float(a))
print("int to str:", str(a))
print("int to complex:", complex(a))
print("int to bool:", bool(a))

print("NOTE: int cannot be directly converted to list, tuple, set, or dict.")


# ------------------------------------------------
# ✅ FLOAT TYPE CONVERSIONS
# ------------------------------------------------
print("\n========== FLOAT TYPE CONVERSION ==========\n")

b = 12.5
print("Original value:", b, "type:", type(b))

print("float to int:", int(b))
print("float to str:", str(b))
print("float to bool:", bool(b))

print("NOTE: float cannot be directly converted to list, tuple, set, or dict.")


# ------------------------------------------------
# ✅ STRING TYPE CONVERSIONS
# ------------------------------------------------
print("\n========== STRING TYPE CONVERSION ==========\n")

s = "python"
print("Original value:", s, "type:", type(s))

print("string to list:", list(s))
print("string to tuple:", tuple(s))
print("string to set:", set(s))
print("string to bool:", bool(s))

print("\nNumeric string conversion:")
num_str1 = "100"
num_str2 = "12.5"
print("int('100'):", int(num_str1))
print("float('12.5'):", float(num_str2))

print("\nInvalid conversions:")
print("int('python')  -> ERROR")
print("float('python')-> ERROR")


# ------------------------------------------------
# ✅ LIST TYPE CONVERSIONS
# ------------------------------------------------
print("\n========== LIST TYPE CONVERSION ==========\n")

lst = [1, 2, 3]
print("Original list:", lst, "type:", type(lst))

print("list to tuple:", tuple(lst))
print("list to set:", set(lst))
print("list to bool:", bool(lst))

print("NOTE: list cannot be directly converted to int or float.")


# ------------------------------------------------
# ✅ TUPLE TYPE CONVERSIONS
# ------------------------------------------------
print("\n========== TUPLE TYPE CONVERSION ==========\n")

t = (4, 5, 6)
print("Original tuple:", t, "type:", type(t))

print("tuple to list:", list(t))
print("tuple to set:", set(t))
print("tuple to bool:", bool(t))


# ------------------------------------------------
# ✅ SET TYPE CONVERSIONS
# ------------------------------------------------
print("\n========== SET TYPE CONVERSION ==========\n")

s1 = {7, 8, 9}
print("Original set:", s1, "type:", type(s1))

print("set to list:", list(s1))
print("set to tuple:", tuple(s1))
print("set to bool:", bool(s1))


# ------------------------------------------------
# ✅ DICTIONARY TYPE CONVERSIONS
# ------------------------------------------------
print("\n========== DICTIONARY TYPE CONVERSION ==========\n")

d = {1: "a", 2: "b"}
print("Original dict:", d, "type:", type(d))

print("dict to list:", list(d))     # keys only
print("dict to tuple:", tuple(d))  # keys only
print("dict to set:", set(d))      # keys only
print("dict to bool:", bool(d))

print("Dictionary keys:", d.keys())
print("Dictionary values:", d.values())
print("Dictionary items:", d.items())


# ------------------------------------------------
# ✅ BOOLEAN TYPE CONVERSION RULES
# ------------------------------------------------
print("\n========== BOOLEAN TYPE CONVERSION ==========\n")

print("bool(0):", bool(0))
print("bool(0.0):", bool(0.0))
print("bool(''):", bool(""))
print("bool([]):", bool([]))
print("bool(()):", bool(()))
print("bool({}):", bool({}))
print("bool(None):", bool(None))

print("bool(5):", bool(5))
print("bool('Python'):", bool("Python"))
print("bool([1, 2, 3]):", bool([1, 2, 3]))


# ------------------------------------------------
# ✅ COMPLEX TYPE CONVERSION
# ------------------------------------------------
print("\n========== COMPLEX TYPE CONVERSION ==========\n")

x = 5
print("int to complex:", complex(x))

print("NOTE: complex numbers cannot be converted into int or float.")
print("Example: int(2+3j) -> ERROR")


# ------------------------------------------------
# ✅ SUMMARY
# ------------------------------------------------
print("\n========== SUMMARY ==========\n")
print("1. Python supports both implicit and explicit type conversion.")
print("2. int, float, str, list, tuple, set, dict, bool, and complex are core data types.")
print("3. list(), tuple(), set() work well with strings and collections.")
print("4. bool() follows truthy and falsy rules.")
print("5. dict() conversion returns only keys.")
print("6. Invalid conversions raise runtime errors.")
print("\n✅ End of Type Conversion Demonstration")



#OUTPUTS:
##========== IMPLICIT TYPE CONVERSION ==========
##
##a = 10 type: <class 'int'>
##b = 2.5 type: <class 'float'>
##a + b = 12.5 type: <class 'float'>
##
##========== EXPLICIT TYPE CONVERSION ==========
##
##Built-in conversion functions:
##int(), float(), str(), list(), tuple(), set(), dict(), bool(), complex()
##
##========== INTEGER TYPE CONVERSION ==========
##
##Original value: 10 type: <class 'int'>
##int to float: 10.0
##int to str: 10
##int to complex: (10+0j)
##int to bool: True
##NOTE: int cannot be directly converted to list, tuple, set, or dict.
##
##========== FLOAT TYPE CONVERSION ==========
##
##Original value: 12.5 type: <class 'float'>
##float to int: 12
##float to str: 12.5
##float to bool: True
##NOTE: float cannot be directly converted to list, tuple, set, or dict.
##
##========== STRING TYPE CONVERSION ==========
##
##Original value: python type: <class 'str'>
##string to list: ['p', 'y', 't', 'h', 'o', 'n']
##string to tuple: ('p', 'y', 't', 'h', 'o', 'n')
##string to set: {'n', 'p', 'o', 'h', 'y', 't'}
##string to bool: True
##
##Numeric string conversion:
##int('100'): 100
##float('12.5'): 12.5
##
##Invalid conversions:
##int('python')  -> ERROR
##float('python')-> ERROR
##
##========== LIST TYPE CONVERSION ==========
##
##Original list: [1, 2, 3] type: <class 'list'>
##list to tuple: (1, 2, 3)
##list to set: {1, 2, 3}
##list to bool: True
##NOTE: list cannot be directly converted to int or float.
##
##========== TUPLE TYPE CONVERSION ==========
##
##Original tuple: (4, 5, 6) type: <class 'tuple'>
##tuple to list: [4, 5, 6]
##tuple to set: {4, 5, 6}
##tuple to bool: True
##
##========== SET TYPE CONVERSION ==========
##
##Original set: {8, 9, 7} type: <class 'set'>
##set to list: [8, 9, 7]
##set to tuple: (8, 9, 7)
##set to bool: True
##
##========== DICTIONARY TYPE CONVERSION ==========
##
##Original dict: {1: 'a', 2: 'b'} type: <class 'dict'>
##dict to list: [1, 2]
##dict to tuple: (1, 2)
##dict to set: {1, 2}
##dict to bool: True
##Dictionary keys: dict_keys([1, 2])
##Dictionary values: dict_values(['a', 'b'])
##Dictionary items: dict_items([(1, 'a'), (2, 'b')])
##
##========== BOOLEAN TYPE CONVERSION ==========
##
##bool(0): False
##bool(0.0): False
##bool(''): False
##bool([]): False
##bool(()): False
##bool({}): False
##bool(None): False
##bool(5): True
##bool('Python'): True
##bool([1, 2, 3]): True
##
##========== COMPLEX TYPE CONVERSION ==========
##
##int to complex: (5+0j)
##NOTE: complex numbers cannot be converted into int or float.
##Example: int(2+3j) -> ERROR
##
##========== SUMMARY ==========
##
##1. Python supports both implicit and explicit type conversion.
##2. int, float, str, list, tuple, set, dict, bool, and complex are core data types.
##3. list(), tuple(), set() work well with strings and collections.
##4. bool() follows truthy and falsy rules.
##5. dict() conversion returns only keys.
##6. Invalid conversions raise runtime errors.
##
##✅ End of Type Conversion Demonstration
