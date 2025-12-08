# A dictionary in Python is an ordered, mutable collection that stores key-value pairs.

# Syntax of a Dictionary:
# dictionary_name = {key1: value1, key2: value2, key3: value3}

# Creating a dictionary:
employee = {"name": "Karthik", "Age": 25, "gender": "M"}
print(employee)
# Output: {'name': 'Karthik', 'Age': 25, 'gender': 'M'}

# Accessing Values
print(employee["name"])      # Karthik
print(employee.get("name"))  # -> most preferable

# Adding and updating:
employee["company"] = "TCS"
print(employee)
# Output: {'name': 'Karthik', 'Age': 25, 'gender': 'M', 'company': 'TCS'}

# Removing items:
employee.pop("Age")
print(employee)
# Output: {'name': 'Karthik', 'gender': 'M', 'company': 'TCS'}

# Removes last item:
employee.popitem()
print(employee)
# Output: {'name': 'Karthik', 'gender': 'M'}

# Clear:
employee.clear()
print(employee)
# Output: {}

# Dictionary Built-in Methods
employee = {"name": "Karthik", "Age": 25, "gender": "M"}
print(employee.keys())
# Output: dict_keys(['name', 'Age', 'gender'])

print(employee.values())
# Output: dict_values(['Karthik', 25, 'M'])

print(employee.items())
# Output: dict_items([('name', 'Karthik'), ('Age', 25), ('gender', 'M')])

# Dictionary Methods for Adding and Updating Data
employee.update({
    "gender": "male",
    "phone": 987654,
    "company": "TCS"
})
print(employee)
# Output: {'name': 'Karthik', 'Age': 25, 'gender': 'male', 'phone': 987654, 'company': 'TCS'}

employee.setdefault("city", "Hyderabad")
print(employee['city'])
# Output: Hyderabad

# Dictionary Methods for Removing Data
# pop:
print(employee.pop("Age"))
# Output: 25

# Using delete:
del employee["gender"]
print(employee)
# Output: {'name': 'Karthik', 'phone': 987654, 'company': 'TCS', 'city': 'Hyderabad'}

# Using popitem():
employee.popitem()
print(employee)
# Output: {'name': 'Karthik', 'phone': 987654, 'company': 'TCS'}

# Clear:
employee.clear()
print(employee)
# Output: {}

# Dictionary comprehension:
cubes = {x: x*x*x for x in range(1, 6)}
print(cubes)
# Output: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
