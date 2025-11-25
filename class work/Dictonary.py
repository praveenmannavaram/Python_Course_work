
# 1. Creating Dictionaries


print("\nCreating Dictionaries")

d1 = {}                      
d2 = dict()                  
d3 = {'name': 'praveen', 'course': 'pfs', 'batch': 41}
d4 = {'name': 'mannavaram', 'course': 'pfs', 'batch': 41}

# Dictionary with multiple data types as keys
d5 = {
    1: 'value',
    12.3: 'value',
    'string': 'value',
    (1, 2, 3): 'value',     
    False: 'value'
}

print("Dictionary d3:", d3)
print("Dictionary d4:", d4)
print("Dictionary d5:", d5)

# 2. Accessing Values


print("\nAccessing Values")

print("d3['name']:", d3['name'])
print("d3.get('course'):", d3.get('course'))
print("d3.get('unknown_key', 'Default Value'):", d3.get('unknown_key', 'Default Value'))



# 3. Adding & Updating Dictionary Data


print("\nAdding & Updating")

d3['age'] = 21                      
d3.update({'location': 'Andhra'})   

print("After updates:", d3)

# setdefault(): Adds key if not available
d3.setdefault('email', 'noemail@example.com')
print("After setdefault():", d3)



# 4. Removing Elements


print("\nRemoving Elements")

d_temp = {'a': 1, 'b': 2, 'c': 3}

print("Original:", d_temp)
print("pop('b'):", d_temp.pop('b'))       
print("popitem():", d_temp.popitem())      

print("Remaining:", d_temp)



# 5. Dictionary Keys, Values, Items


print("\nKeys, Values & Items")

print("Keys:", d3.keys())
print("Values:", d3.values())
print("Items:", d3.items())



# 6. Iterating Through Dictionary


print("\nIterating Through Dictionary")

for key, value in d3.items():
    print(f"Key: {key} -> Value: {value}")



# 7. Length, Max, Min, Sorted


print("\nBuilt-in Functions")

sample_dict = {5: "A", 9: "B", 1: "C", 3: "D"}

print("Dictionary:", sample_dict)
print("Length:", len(sample_dict))
print("Max key:", max(sample_dict))
print("Min key:", min(sample_dict))
print("Sorted keys:", sorted(sample_dict))



# 8. Nested Dictionary Example


print("\nNested Dictionary")

student = {
    "name": "Praveen",
    "course": "AIML",
    "marks": {
        "python": 90,
        "maths": 85,
        "ds": 88
    }
}

print("Student Dictionary:", student)
print("Python Marks:", student["marks"]["python"])



# 9. Dictionary Comprehension


print("\nDictionary Comprehension")

squares = {num: num * num for num in range(1, 6)}
print("Squares:", squares)