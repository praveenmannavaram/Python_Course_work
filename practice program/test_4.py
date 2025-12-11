# Q1. Calculate BMI
def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m * height_m)
    print(round(bmi, 2))

print("Q1 OUTPUT:")
calculate_bmi(70, 1.75)
calculate_bmi(90, 1.8)
print()

##OUTPUT:
##22.86
##27.78

# Q2. Filter Even Numbers
def filter_even(numbers):
    res = [i for i in numbers if i % 2 == 0]
    print(res)

print("Q2 OUTPUT:")
filter_even([1, 2, 3, 4, 5, 6])
filter_even([11, 15, 21])
print()

##OUTPUT:
##[2, 4, 6]
##[]

# Q3. Generate Multiplication Table
def generate_table(n):
    table = [i * n for i in range(1, 11)]
    print(table)

print("Q3 OUTPUT:")
generate_table(2)
generate_table(5)
print()

##OUTPUT:
##[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
##[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# Q4. Check Anagram
def is_anagram(str1, str2):
    s1 = sorted(str1.replace(" ", "").lower())
    s2 = sorted(str2.replace(" ", "").lower())
    return s1 == s2

print("Q4 OUTPUT:")
print(is_anagram("listen", "silent"))
print(is_anagram("Hello", "Olelh"))
print(is_anagram("apple", "pale"))
print()

##OUTPUT:
##True
##True
##False

# Q5. Count Word Occurrences
def count_words(text):
    res = {}
    for word in text.split():
        res[word] = res.get(word, 0) + 1
    print(res)

print("Q5 OUTPUT:")
count_words("this is a test this is")
count_words("hello hello world")
print()

##OUTPUT:
##{'this': 2, 'is': 2, 'a': 1, 'test': 1}
##{'hello': 2, 'world': 1}

# Q6. Simulate LRU Cache
def lru_cache(requests, size):
    cache = []
    for item in requests:
        if item in cache:
            cache.remove(item)
            cache.insert(0, item)
        else:
            if len(cache) < size:
                cache.insert(0, item)
            else:
                cache.pop()
                cache.insert(0, item)
    print(cache)

print("Q6 OUTPUT:")
lru_cache([1,2,3,2,4,1], 3)
lru_cache([5,6,7,8], 2)
lru_cache([1,2,3,1], 2)
print()

##OUTPUT:
##[1, 4, 2]
##[8, 7]
##[1, 3]

# Q7. Flatten 2D List
def flatten_matrix(matrix):
    res = []
    for row in matrix:
        for col in row:
            res.append(col)
    print(res)

print("Q7 OUTPUT:")
flatten_matrix([[1, 2], [3, 4]])
flatten_matrix([[5], [6, 7], [8]])
print()

##OUTPUT:
##[1, 2, 3, 4]
##[5, 6, 7, 8]

# Q8. Create Email Address
def create_email(first_name, last_name, domain):
    print(f"{first_name.lower()}.{last_name.lower()}@{domain.lower()}.com")

print("Q8 OUTPUT:")
create_email("John", "Doe", "gmail")
create_email("ALICE", "Smith", "yahoo")
print()

##OUTPUT:
##john.doe@gmail.com
##alice.smith@yahoo.com

# Q9. Find All Factors of a Number
def get_factors(n):
    res = []
    for i in range(1, n + 1):
        if n % i == 0:
            res.append(i)
    print(res)

print("Q9 OUTPUT:")
get_factors(12)
get_factors(17)
get_factors(28)
print()

##OUTPUT:
##[1, 2, 3, 4, 6, 12]
##[1, 17]
##[1, 2, 4, 7, 14, 28]

# Q10. Format Invoice Entry
def format_invoice(item, quantity, price):
    total = quantity * price
    print(f"{item} x{quantity} @ ₹{price} = ₹{total}")

print("Q10 OUTPUT:")
format_invoice("Pen", 3, 10)
format_invoice("Notebook", 2, 45)

##OUTPUT:
##Pen x3 @ ₹10 = ₹30
##Notebook x2 @ ₹45 = ₹90