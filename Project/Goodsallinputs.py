print("========= WELCOME TO GOODS SERVICE PRODUCT =========\n")


product_id = int(input("Enter Product ID (Integer): "))  # Integer input - Product ID


product_price = float(input("Enter Product Price (Float): "))  # Float input - Product Price


product_code = complex(input("Enter Product Code (Example: 4+6j): "))  # Correct Complex input - Batch or Service Code


availability_input = input("Is the product available? (True/False): ").strip().lower()  # Boolean input → Availability
is_available = availability_input == "true"


list_input = input("Enter Product Features (comma separated): ")  # List input - Product Features
product_features = list(list_input.split(","))


tuple_input = input("Enter Product Dimensions (comma separated): ")  # Tuple input - Product Dimensions
product_dimensions = tuple(tuple_input.split(","))


set_input = input("Enter Product Tags (comma separated): ")  # Set input - Unique Product Tags
product_tags = set(set_input.split(","))


dict_input = input("Enter Extra Details (key:value, comma separated): ")  # Dictionary input - Extra Product Details
product_details = {}

pairs = dict_input.split(",")
for pair in pairs:
    key, value = pair.split(":")
    product_details[key.strip()] = value.strip()


print("\n=========== GOODS PRODUCT BILL ===========")
print("Product ID        :", product_id, type(product_id))
print("Product Price     : ₹", product_price, type(product_price))
print("Product Code      :", product_code, type(product_code))
print("Available         :", is_available, type(is_available))
print("Product Features  :", product_features, type(product_features))
print("Product Dimensions:", product_dimensions, type(product_dimensions))
print("Product Tags      :", product_tags, type(product_tags))
print("Extra Details     :", product_details, type(product_details))
print("=================================================================")


#Outputs:-

##Enter Product ID (Integer): 234
##Enter Product Price (Float): 435.54
##Enter Product Code (Example: 4+6j): 34+6j
##Is the product available? (True/False): True
##Enter Product Features (comma separated): wire, charger, cable
##Enter Product Dimensions (comma separated): 23, 34, 43
##Enter Product Tags (comma separated): new, offer, discount
##Enter Extra Details (key:value, comma separated): 1 : JBL, 2 : SONY, 3 : LG
##---------------- OUTPUT ----------------
##
##=========== GOODS PRODUCT BILL ===========
##Product ID        : 234 <class 'int'>
##Product Price     : ₹ 435.54 <class 'float'>
##Product Code      : (34+6j) <class 'complex'>
##Available         : True <class 'bool'>
##Product Features  : ['wire', ' charger', ' cable'] <class 'list'>
##Product Dimensions: ('23', ' 34', ' 43') <class 'tuple'>
##Product Tags      : {' discount', ' offer', 'new'} <class 'set'>
##Extra Details     : {'1': 'JBL', '2': 'SONY', '3': 'LG'} <class 'dict'>
##=========================================
