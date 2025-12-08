# ZEPTO
# Task 1: Take Product Details as Input

print("🛒 ========= WELCOME TO ZEPTO PRODUCT SYSTEM ========= 🛒\n")

product_id = int(input("Enter Product ID: "))
product_name = input("Enter Product Name: ")
price = float(input("Enter Price: "))

categories = input("Enter Categories (comma-separated): ").split(",")

available_stock = int(input("Enter Available Stock: "))
sold_stock = int(input("Enter Sold Stock: "))
stock_details = (available_stock, sold_stock)

discount_percentage = float(input("Enter Discount Percentage: "))

features = set(input("Enter Product Features (comma-separated): ").split(","))

supplier_name = input("Enter Supplier Name: ")
supplier_contact = input("Enter Supplier Contact Number: ")
supplier_location = input("Enter Supplier Location: ")

supplier_details = {
    "name": supplier_name,
    "contact": supplier_contact,
    "location": supplier_location
}

# -----------------------------------------------------
# Task 2: Display Using Different Formatting Techniques
# -----------------------------------------------------

print("\n=============== ZEPTO PRODUCT DETAILS ===============")

# 1. Using Comma Separation
print("\n1. Using Comma Separation (sep=',')")
print("Product ID, Name, Price:", product_id, product_name, price, sep=", ")

# 2. Using Percentage Formatting
print("\n2. Using Percentage Formatting (% operator)")
print("Product Discount: %.2f%%" % discount_percentage)

# 3. Using f-strings
print("\n3. Using f-strings")
print(f"Product Name: {product_name}")
print(f"Price: ₹{price:.2f}")
print(f"Discount: {discount_percentage}%")
print(f"Stock Available: {stock_details[0]} units")

# 4. Using .format() method
print("\n4. Using .format() method")
print("Supplier Details: Name - {}, Contact - {}, Location - {}"
      .format(supplier_details['name'],
              supplier_details['contact'],
              supplier_details['location']))

print("\nCategories:", categories)
print("Features:", features)
print("Stock Details (Available, Sold):", stock_details)

print("\n===================== END =====================")

#output:
##🛒 ========= WELCOME TO ZEPTO PRODUCT SYSTEM ========= 🛒
##
##Enter Product ID: 32
##Enter Product Name: Oats
##Enter Price: 343
##Enter Categories (comma-separated): Grocery,Health,Fitness
##Enter Available Stock: 45
##Enter Sold Stock: 23
##Enter Discount Percentage: 67
##Enter Product Features (comma-separated): High Fiber,Healthy,Organic
##Enter Supplier Name: HealthyFoods
##Enter Supplier Contact Number: 9876543210
##Enter Supplier Location: Hyderabad
##
##=============== ZEPTO PRODUCT DETAILS ===============
##
##1. Using Comma Separation (sep=',')
##Product ID, Name, Price:, 32, Oats, 343.0
##
##2. Using Percentage Formatting (% operator)
##Product Discount: 67.00%
##
##3. Using f-strings
##Product Name: Oats
##Price: ₹343.00
##Discount: 67.0%
##Stock Available: 45 units
##
##4. Using .format() method
##Supplier Details: Name - HealthyFoods, Contact - 9876543210, Location - Hyderabad
##
##Categories: ['Grocery', 'Health', 'Fitness']
##Features: {'Organic', 'Healthy', 'High Fiber'}
##Stock Details (Available, Sold): (45, 23)
##
##===================== END =====================
