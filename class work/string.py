# 1. Defining Strings
s = ''
s = ""
s = ''' '''
s = "' '"

# 2. Concatenation
name = 'praveen'
name1 = "kumar"
print(name + name1)        # praveenkumar
print(name + ' ' + name1)  # praveen kumar

# 3. Repetition
print(name * 10)
print('*' * 100)
print('-' * 10)

# 4. Indexing
name = 'praveen kumar'
print(name[3])   # v
print(name[-2])  # a
print(name[-5])  # u
print(name[1])   # r

# 5. Slicing
names = 'praveenkumarmannavaramsaisarath'
print(names[0:7])    # praveen
print(names[:7])     # praveen
print(names[7:12])   # kumar
print(names[12:22])  # mannavaram
print(names[22:25])  # sai
print(names[25:31])  # sarath
print(names[25:])    # sarath
print(names[0:7:2])  # pavn
print(names[::3])    # pekkrrsia
print(names[-6:])    # arath

# Reverse string
print(names[::-1])

# Reverse partial sections
print(names[7::-1])     # ramu neev arp
print(names[6::-1])     # neev arp
print(names[15:7:-1])   # ravanna m
print(names[20:12:-1])  # mavarann
print(names[24:21:-1])  # ias
print(names[30:24:-1])  # htaras

# 6. Membership Operators
print('praveen' in names)     # True
print('Nithin' in names)      # False
print('Priya' in names)       # False
print('Sahithi' not in names) # True

# 7. Case Methods
print(names.upper())
print(names.lower())
print(names.swapcase())

l = 'python programming language'
print(l.capitalize())
print(l.title())
print("ß".casefold())

# 8. Alignment Methods
print(l.center(100, '*'))
print(l.center(50, '*'))
print(l.center(50, '-'))
print(l.center(50, '_'))
print(l.ljust(50, '-'))
print(l.ljust(50, ' ') + ':')
print(l.rjust(50, '-'))

# 9. Zero Fill
print('2'.zfill(6))
print('202'.zfill(6))
print('202123'.zfill(6))

# 10. Searching and Counting
print(names.find('p'))
print(names.find('a'))
print(names.find('praveen'))
print(names.find('z'))
print(names.rfind('a'))
print(names.index('k'))
print(names.index('a'))
print(names.rindex('a'))
print(names.count('a'))
print(names.count('e'))
print(names.count('i'))

# 11. Replace
print(names.replace('a', '*'))
print(names.replace('ar', ''))
print(names.replace('ar', '00'))
print(names.replace('ar', '-00-'))
print(names.replace('praveen', 'praveen kumar'))
