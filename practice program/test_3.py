##Q1. Automated Salary Tax Calculator
##A company deducts tax based on the following salary brackets:
##● Up to 2,50,000 → No Tax
##● 2,50,001 – 5,00,000 → 5%
##● 5,00,001 – 10,00,000 → 20%
##● Above 10,00,000 → 30%
##Write a script that takes annual salary as input and calculates total tax amount.
##Input Format
##A single float salary
##Output Format
##Tax amount as float
##Sample Input 1
##300000
##Sample Output 1
##15000.0
##Sample Input 2
##1100000
##Sample Output 2
##Python
##Python
##Python
##3,30000.0


salary = float(input("Enter the salary: "))

tax = 0
if salary <= 250000:
    tax = 0
elif salary <= 500000:
    tax = salary * 0.05
elif salary <= 1000000:
    tax = salary * 0.20
else:
    tax = salary * 0.30

print(tax)

#output:
##Enter the salary: 5000000
##1500000.0


##Q2. Movie Ticket Pricing System
##A theater charges differently based on age:
##● Below 5: Free
##● 5–18: ₹100
##● 19–60: ₹150
##● Above 60: ₹120
##Take the age of n visitors and calculate the total collection.
##Input Format
##● First line: Integer n
##● Next n lines: one age per line
##Output Format
##Total ticket collection
##Sample Input 1
##4
##3
##17
##35
##65
##Sample Output 1
##370

n = int(input("Enter the no of people: "))
total = 0

for i in range(n):
    age = int(input("Enter the ages: "))
    if age < 5:
        continue
    elif age <= 18:
        total += 100
    elif age <= 60:
        total += 150
    else:
        total += 120

print(total)

#Output:
##Enter the no of people: 2
##Enter the ages: 23
##Enter the ages: 34
##300


##Q3. Electricity Bill Generator
##Design a bill generator based on units consumed:
##● First 100 units: ₹1.5/unit
##● 101–200 units: ₹2.5/unit
##● 201–500 units: ₹4/unit
##● Above 500 units: ₹6/unit
##Input Format
##Integer units
##Output Format
##Total bill in rupees
##Sample Input 1
##250
##Sample Output 1
##600.0

units = int(input("Enter the no of units: "))
bill = 0

if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = 150 + (units - 100) * 2.5
elif units <= 500:
    bill = 400 + (units - 200) * 4
else:
    bill = 1600 + (units - 500) * 6

print(bill)

#output:
##Enter the no of units: 342
##968


##Q4. Car Parking Fee Calculator
##Charges are based on hours parked:
##● Up to 2 hours → ₹30
##● Every additional hour → ₹10/hr
##● Max per day (24 hrs) → ₹200
##Input Format
##Integer hours
##Python
##Python
##Python
##Python
##Output Format
##Fee amount
##Sample Input 1
##3
##Sample Output 1
##40
##Sample Input 2
##24
##Sample Output 2
##200


hours = int(input("Enter the no of hours: "))

if hours <= 2:
    fee = 30
elif hours < 24:
    fee = 30 + (hours - 2) * 10
else:
    fee = 200

print(fee)

#output:
##Enter the no of hours: 10
##110


##Q5. Product Inventory Checker (Nested Conditionals)
##Take product name and quantity as input. Based on quantity:
##● 0 → Out of Stock
##● 1–10 → Low Stock
##● 11–50 → In Stock
##● Above 50 → Overstocked
##Input Format
##● First line: Product name
##Python
##Python
##Python
##Python
##● Second line: Integer quantity
##Output Format
##Message as per condition
##Sample Input 1
##Mouse
##5
##Sample Output 1
##Mouse: Low Stock

name = input("Enter the name: ")
qty = int(input("Enter the quantity: "))

if qty == 0:
    print(f"{name}: Out of Stock")
elif qty <= 10:
    print(f"{name}: Low Stock")
elif qty <= 50:
    print(f"{name}: In Stock")
else:
    print(f"{name}: Overstocked")

#output:
##Enter the name: speaker
##Enter the quantity: 10
##speaker: Low Stock


##Q6. Pattern – Row-wise Alternating 0 and 1 (Nested Loops)
##Write a program to print a square pattern of size n, where each row alternates between 0
##and 1.
##Input Format
##An integer n
##Output Format
##Pattern as described
##Sample Input 1
##4
##Sample Output 1
##0 1 0 1
##1 0 1 0
##0 1 0 1
##1 0 1 0
##Python
##Python

n = int(input("Ente the number of patterns: "))

for i in range(n):
    for j in range(n):
        print((i + j) % 2, end=" ")
    print()

#output:
##Ente the number of patterns: 6
##0 1 0 1 0 1 
##1 0 1 0 1 0 
##0 1 0 1 0 1 
##1 0 1 0 1 0 
##0 1 0 1 0 1 
##1 0 1 0 1 0


##Q7. Gym Subscription Billing (Menu Driven Program)
##Menu:
##1. Monthly – ₹500
##2. Quarterly – ₹1300
##3. Yearly – ₹5000
##Write a menu-driven script to calculate bill amount based on user choice and number of
##persons.
##Input Format
##● Line 1: Choice (1/2/3)
##● Line 2: Number of people
##Output Format
##Total bill amount
##Sample Input 1
##2
##3
##Sample Output 1
##3900

billing = {1: 500, 2: 1300, 3: 5000}

choice = int(input("Enter the choice of bill: "))
people = int(input("Enter the number of people: "))

print(billing[choice] * people)

#output:
##Enter the choice of bill: 3
##Enter the number of people: 4
##20000

##Q8. Billing Bot – Apply Discount Based on Amount
##You are creating a billing bot. Apply discount based on total purchase:
##● ₹0–999 → No discount
##● ₹1000–4999 → 5%
##● ₹5000–9999 → 10%
##Python
##Python
##Python
##● ₹10000+ → 15%
##Input Format
##A float value representing total amount
##Output Format
##Final payable amount after discount
##Sample Input
##12000
##Sample Output
##10200.0

amount = float(input("Enter the amount: "))
discount = 0

if amount < 1000:
    discount = 0
elif amount < 5000:
    discount = amount * 0.05
elif amount < 10000:
    discount = amount * 0.10
else:
    discount = amount * 0.15

print(amount - discount)

#output:
##Enter the amount: 234244
##199107.4


##Q9 : ATM PIN Verification with Blocking Logic
##Create a script for an ATM system where a user gets 3 chances to enter the correct 4-digit
##PIN.
##● If the correct PIN is entered, display "Access Granted".
##● If all 3 attempts are wrong, print "ATM Blocked. Try Again Later."
##Stored PIN: 1234
##Input Format
##Three lines: each a 4-digit integer PIN attempt
##Output Format
##Result message based on attempts
##Sample Input
##1111
##Python
##Python
##Python
##2222
##1234
##Sample Output
##Access Granted
##Sample Input
##1111
##2222
##3333
##Sample Output
##ATM Blocked. Try Again Later.


stored_pin = 1234

for i in range(3):
    pin = int(input("Enter the pin: "))
    if pin == stored_pin:
        print("Access Granted")
        break
else:
    print("ATM Blocked. Try Again Later.")

#output:
##1264
##3244
##3534
##ATM Blocked. Try Again Later.
##Enter the pin: 1243
##Enter the pin: 2123
##Enter the pin: 1234
##Access Granted


##Q10 : Bus Booking System – Track Full and Empty Seats
##A bus has n seats. You are given a list of seat numbers booked (1 to n).
##● Print total seats
##● Count and print number of booked seats and available seats
##Input Format
##● Line 1: Integer n – total number of seats
##● Line 2: Space-separated list of booked seat numbers
##Output Format
##Python
##Python
##Python
##Python
##● Total seats
##● Booked seats count
##● Available seats count
##Sample Input 1
##10
##2 4 6 7
##Sample Output 1
##Total Seats: 10
##Booked: 4
##Available: 6
##Sample Input 2
##5
##1 2 3 4 5
##Sample Output 2
##Total Seats: 5
##Booked: 5
##Available: 0

n = int(input("Enter the total seats: "))
booked = list(map(int, input("Enter the seat numbers: ").split()))

print(f"Total Seats: {n}")
print(f"Booked: {len(booked)}")
print(f"Available: {n - len(booked)}")

#output:
##Enter the total seats: 24
##Enter the seat numbers: 3
##Total Seats: 24
##Booked: 1
##Available: 23
##
##Enter the total seats: 24
##Enter the seat numbers: 6 3 5 7 23 21 22 18 16 12
##Total Seats: 24
##Booked: 10
##Available: 14