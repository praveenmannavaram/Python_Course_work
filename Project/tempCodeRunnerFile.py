
#********************************
#  Simple Goods Selling App
#********************************

products = ["Laptop", "Mouse", "Phone", "Charger", "Speaker"]
stocks =   [10,        50,      30,      0,         25]
prices =   [50000,     500,     15000,   300,       2000]

def show_products():
    print("\n****** AVAILABLE PRODUCTS ******")
    for i in range(len(products)):
        print(f"{i+1}. {products[i]}  | Stock: {stocks[i]}  | Price: ${prices[i]}")

def buy_product():
    show_products()
    choice = int(input("\nEnter product number to buy: ")) - 1

    if choice < 0 or choice >= len(products):
        print("Invalid choice!")
        return

    product = products[choice]
    stock = stocks[choice]
    price = prices[choice]

    if stock == 0:
        print(f"❌ {product} is OUT OF STOCK.")
        return

    qty = int(input(f"Enter quantity of {product}: "))

    if qty <= 0:
        print("❌ Quantity must be more than 0.")
        return

    if qty > stock:
        print(f"❌ Only {stock} items available!")
        return

    total = qty * price
    stocks[choice] -= qty

    print("\n****** BILL RECEIPT ******")
    print(f"Product: {product}")
    print(f"Quantity: {qty}")
    print(f"Price Each: ₹{price}")
    print(f"Total Amount: ₹{total}")
    print("**************************\n")

def main_menu():
    while True:
        print("******* GOODS SELLING APP ******")
        print("1. View Products")
        print("2. Buy Product")
        print("3. Exit")

        option = input("Choose an option: ")

        if option == "1":
            show_products()
        elif option == "2":
            buy_product()
        elif option == "3":
            print("Thank you for visiting our store!!! Have a great day 😊")
            break
        else:
            print("Invalid option. Try again!!!")
main_menu()
