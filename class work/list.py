# List creation
l = []
l = list()
l = [1, 2, 3, 4, 5, 6]
l = list([1, 2, 3, 4, 5])
print(l)

# Nested lists
l = [[1, 2], [3, 4], [5, 6]]

# Duplicate values
l = [1, 1, 1, 1, 1, 1, 2]
print(l)

# Concatenation
print([1, 2, 3] + [4, 5, 6])

# Repetition
print([1, 2] * 5)

# Membership
print(2 in l)
print(6 in l)

# Indexing and slicing
l = ['praveen', 'kumar', 'mannavaram', 'sai', 'sarath', 'satish', 'sunil']
print(l)
print(l[2])
print(l[-3])
print(l[-2])
print(l[-1])
print(l[1])
print(l[0])
print(l[1:3])
print(l[-1:-4:-1])
print(l[::2])
print(l[1::2])
print(l[::-1])

# Nested list indexing
l = [[1, 2], [3, 4], [5, 6]]
print(l[2])
print(l[1])
print(l[0])
print(l[0][0])
print(l[2][0])
print(l[1][1])

# Modifying list elements
l = [10, 20, 30, 40, 50]
print(id(l))
print(l[1])
l[1] = 20.3
print(l)
print(id(l))

l[2] = 30 + 4j
print(l)
l[3] = "string"
print(l)

# append()
l.append([1, 2, 3])
print(l)
l.append((10, 202, 30))
print(l)

# Adding single values
l.append(70)
l.append(80)
print(l)

# extend()
l.extend([100, 90, 20, 10])
print(l)

# insert()
l.insert(0, 10)
print(l)
l.insert(5, {1: 2, 2: 4, 3: 6, 4: 8})
print(l)
l.insert(8, {1, 2, 3, 4})
print(l)

# remove()
l.remove(10)
print(l)
l.remove((10, 202, 30))
print(l)
l.remove({1, 2, 3, 4})
print(l)
l.remove(100)
print(l)

# pop()
l.pop(2)
print(l)
l.pop(1)
print(l)
l.pop()
print(l)

# pop multiple
print(l.pop())
print(l.pop())
print(l)

# del
del l[2]
print(l)

# clear
l.clear()
print(l)

# del list completely
l = [1, 2, 3, 4]
del l

# index, count, sort
l = [10, 20, 30, 40, 50, 60, 70, 80]
print(l.index(30))
print(l.index(80))

l.append(10)
print(l)
print(l.index(10))
print(l.count(10))

l.sort()
print(l)

# sorted()
l = [8, 2, 3, 4, 1, 8, 3, 4]
print(sorted(l))
print(l)

# sort and reverse
l.sort()
print(l)

l.sort(reverse=True)
print(l)

l.reverse()
print(l)

# Copy lists
a = [1, 2, 3, 4, 5]
b = a
b.append(6)
print(a)
print(b)

# proper copy
c = a.copy()
c.append(9)
print(c)
print(a)

# max, min, len
l = [1, 2, 3, 3, 4, 4, 8, 8]
print(max(l))
print(min(l))
print(len(l))

# any, all
l = [0, 0.0, "", [], (), {}, set(), False]
print(any(l))
print(all(l))

l.append(1)
print(l)
print(any(l))
print(all(l))

a = [1, 2, 3, 4, 5, 6]
print(all(a))