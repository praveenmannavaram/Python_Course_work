# 1. Creating Sets

print("=== Creating Sets ===")

# Empty set
s = set()
print("Empty set:", s)

# Creating a set with unique elements
s = {1, 2, 3, 4, 5, 6, 7}
print("Original set:", s)

# Duplicate values in a set (duplicates are ignored)
s = {1, 11, 1, 1, 2, 3, 2, 3, 4, 5, 6, 7}
print("Set after removing duplicates:", s)

# Another set
s = {100, 2000, 2, 1, 57, 14, 48}
print("New set:", s)

'''
#Output
=== Creating Sets ===
Empty set: set()
Original set: {1, 2, 3, 4, 5, 6, 7}
Set after removing duplicates: {1, 2, 3, 4, 5, 6, 7, 11}
New set: {2000, 1, 2, 48, 100, 57, 14}
'''

# 2. Set Add / Remove Operations

print("\n=== Add / Remove Operations ===")

# Add an integer
s.add(90)
print("After adding 90:", s)

# Remove an element (raises error if not found)
try:
    s.remove(4000)
except KeyError:
    print("Cannot remove 4000: Not found in set")

# Add float
s.add(12.23)
print("After adding float:", s)

# Add string
s.add("1234")
print("After adding string:", s)

# Add complex number
s.add(12 + 1j)
print("After adding complex number:", s)

'''
#Output
=== Add / Remove Operations ===
After adding 90: {2000, 1, 2, 48, 100, 57, 90, 14}
Cannot remove 4000: Not found in set
After adding float: {1, 2, 12.23, 14, 2000, 90, 100, 48, 57}
After adding string: {1, 2, 12.23, 14, 2000, 90, '1234', 100, 48, 57}
After adding complex number: {1, 2, 12.23, 14, (12+1j), 2000, 90, '1234', 100, 48, 57}
'''

# 3. Set Operations

print("\n=== Set Operations ===")

girls = {"Asha", "Meena", "Riya"}
guys = {"Ravi", "Kiran", "Riya"}
online = {"Riya", "Kiran"}

# UNION – combines all unique elements
print("Union:", girls | guys)
print("Union (method):", girls.union(guys))

# INTERSECTION – common elements
print("Intersection:", girls.intersection(guys))

# DIFFERENCE – removes matching elements
print("Guys - Online:", guys.difference(online))

# SYMMETRIC DIFFERENCE – elements not common in both
print("Symmetric Difference:", guys.symmetric_difference(online))

'''
#Output
=== Set Operations ===
Union: {'Meena', 'Asha', 'Kiran', 'Ravi', 'Riya'}
Union (method): {'Meena', 'Asha', 'Kiran', 'Ravi', 'Riya'}
Intersection: {'Riya'}
Guys - Online: {'Ravi'}
Symmetric Difference: {'Ravi'}
'''

# 4. Subset & Superset Checks

print("\n=== Subset / Superset ===")

a = {1, 2, 3, 4, 5, 6}
b = {5, 6, 7, 8, 9}

print("A - B Difference:", a.difference(b))

a = {1, 2, 3, 4}
b = {2, 3}

print("Is A subset of B?", a.issubset(b))
print("Is B subset of A?", b.issubset(a))
print("Is A a superset of B?", a.issuperset(b))

'''
#Output
=== Subset / Superset ===
A - B Difference: {1, 2, 3, 4}
Is A subset of B? False
Is B subset of A? True
Is A a superset of B? True
'''

# 5. Disjoint Check

print("\n=== Disjoint Check ===")

print("Are girls and guys disjoint (no common elements)?", girls.isdisjoint(guys))

'''
#Output
=== Disjoint Check ===
Are girls and guys disjoint (no common elements)? False
'''

# 6. intersection_update()

print("\n=== intersection_update() Example ===")

x = {1, 2, 3, 4}
y = {3, 4, 5, 6}

print("Before intersection_update:", x)
x.intersection_update(y)  
print("After intersection_update:", x)

'''
#Output
=== intersection_update() Example ===
Before intersection_update: {1, 2, 3, 4}
After intersection_update: {3, 4}
'''