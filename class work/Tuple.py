# TUPLE CREATION

# Empty tuple
t = ()
print("Empty tuple:", t)

# Using tuple() constructor
t = tuple()
print("Using tuple() constructor:", t)

# Tuple with values
t = (1, 2, 3, 4, 5, 1, 2, 4)
print("Tuple with values:", t)

# Correct way using tuple()
t = tuple((1, 2, 3, 4, 5))
print("Correct tuple():", t)

# Tuple without parentheses (tuple packing)
t = 1, 2, 3, 4, 5
print("Tuple packing:", t)

# Single element tuple
t = (1)
print("Not a tuple:", t)     # prints integer

t = (1,)
print("Single element tuple:", t)


# TUPLE INDEXING & SLICING

t = ('int', 'float', 'complex', 'bool', 'set', 'dict', 'list', 'tuple', 'string')

print("\nIndexing examples:")
print(t[1])   # float
print(t[-1])  # string
print(t[-2])  # tuple
print(t[2])   # complex

print("\nSlicing examples:")
print(t[3:6])         # ('bool', 'set', 'dict')
print(t[-1:-4:-1])    # ('string', 'tuple', 'list')
print(t[-3:])         # last 3 elements
print(t[2::-1])       # reverse until index 2
print(t[::2])         # step 2 forward
print(t[::-2])        # step 2 backward

# TUPLE OPERATIONS

t1 = (1, 2, 3)
t2 = (7, 8, 9)

print("\nConcatenation:", t1 + t2)
print("Repetition:", t1 * 5)

print("Membership check:", 3 in t1)
print("Not in check:", 4 not in t1)

# UNPACKING

t = (10, 20, 30)
a, b, c = t
print("\nTuple Unpacking:", a, b, c)

# Login-like example
t = ("Uname", "mail@gmail.com", "Pwd@123")
uname, mail, pwd = t
print("Username:", uname)
print("Mail:", mail)
print("Password:", pwd)


# TUPLE METHODS

t = (1, 2, 3, 1, 2, 3, 1, 2)

print("\nCount:", t.count(2))
print("Index of 2:", t.index(2))
print("Length:", len(t))
print("Max:", max(t))
print("Min:", min(t))
print("Sum:", sum(t))

# IMMUTABILITY DEMONSTRATION
print("\nTuples are immutable:")
try:
    t[1] = 14
except TypeError as e:
    print("Error:", e)