import random
from datetime import datetime

# ==========================================
#          JOLLIBEE ORDERING SYSTEM

# ==========================================
ADMIN_PASSWORD = "1234"
# FOOD MENU WITH PRICES AND PREPARATION TIMES
menu = {
    "Chickenjoy Meals": {
        1: ("1pc Chickenjoy with Rice", 99, 10),
        2: ("1pc Chickenjoy with Spaghetti", 145, 12),
        3: ("2pc Chickenjoy with Rice", 169, 15),
        4: ("Chickenjoy Bucket (6pcs)", 499, 20)
    },
    "Burger Meals": {
        5: ("Yumburger with Fries and Drink", 99, 8),
        6: ("Cheesy Yumburger Meal", 119, 8),
        7: ("Champ Meal", 179, 12)
    },
    "Solo Burgers": {
        8: ("Yumburger", 45, 5),
        9: ("Cheesy Yumburger", 59, 6),
        10: ("Champ Burger", 139, 10)
    },
    "Jolly Spaghetti": {
        11: ("Jolly Spaghetti Solo", 65, 7),
        12: ("Jolly Spaghetti with Drink", 89, 8),
        13: ("Jolly Spaghetti Family Pan", 220, 12)
    },
    "Sides and Drinks": {
        14: ("Regular Fries", 45, 5),
        15: ("Large Fries", 65, 5),
        16: ("Peach Mango Pie", 39, 5),
        17: ("Coke Float", 49, 3),
        18: ("Regular Coke", 35, 2)
    }
}
# STORE ALL CUSTOMER ORDERS
orders = []

# ==========================================
#              MAIN MENU

# ==========================================


def main_menu():
    while True:
        print("\n" + "=" * 50)
        print("              WELCOME TO JOLLIBEE!")
        print("                ORDERING SYSTEM")
        print("=" * 50)
        print("\n1. Admin")
        print("2. User / Customer")
        print("0. Exit System")
        choice = input("\nSelect Menu: ")
        if choice == "1":
            admin_login()
        elif choice == "2":
            user_menu()
        elif choice == "0":
            print("\nThank you for using Jollibee Ordering System!")
            break
        else:
            print("\nInvalid selection. Please try again.")

# ==========================================
#                ADMIN LOGIN

# ==========================================


def admin_login():
    print("\n" + "=" * 50)
    print("                  ADMIN LOGIN")
    print("=" * 50)
    password = input("Enter Admin Password: ")
    if password == ADMIN_PASSWORD:
        print("\nLogin Successful!")
        admin_menu()
    else:
        print("\nIncorrect Password!")
        print("Access Denied.")

# ==========================================
#                 ADMIN MENU

# ==========================================


def admin_menu():
    while True:
        print("\n" + "=" * 50)
        print("                  ADMIN MENU")
        print("=" * 50)
        print("1. View All Orders")
        print("2. View Order Details")
        print("3. Update Order Status")
        print("0. Logout")
        choice = input("\nSelect Option: ")
        if choice == "1":
            view_all_orders()
        elif choice == "2":
            view_order_details()
        elif choice == "3":
            update_order_status()
        elif choice == "0":
            print("\nAdmin Logged Out.")
            break
        else:
            print("\nInvalid selection.")

# ==========================================
#             VIEW ALL CUSTOMER ORDERS

# ==========================================


def view_all_orders():
    print("\n" + "=" * 65)
    print("                  ALL CUSTOMER ORDERS")
    print("=" * 65)
    if not orders:
        print("\nNo orders available yet.")
        return
    for order in orders:
        print("\nOrder Number :", order["order_number"])
        print("Customer     :", order["customer"])
        print("Order Type   :", order["order_type"])
        print("Total Amount : PHP", f"{order['total']:.2f}")
        print("Payment      :", order["payment_method"])
        if order["payment_method"] == "Online":
            print("Online Mode  :", order["online_method"])
        print("Prep Time    :", order["prep_time"], "minutes")
        print("Status       :", order["status"])
        print("-" * 65)

# ==========================================
#              VIEW ORDER DETAILS

# ==========================================


def view_order_details():
    if not orders:
        print("\nNo orders available.")
        return
    try:
        order_number = int(input("\nEnter Order Number: "))
        selected_order = None
        for order in orders:
            if order["order_number"] == order_number:
                selected_order = order
                break
        if selected_order is None:
            print("\nOrder number not found.")
            return
        print("\n" + "=" * 55)
        print("                  ORDER DETAILS")
        print("=" * 55)
        print("Order Number :", selected_order["order_number"])
        print("Customer     :", selected_order["customer"])
        print("Date         :", selected_order["date"])
        print("Order Type   :", selected_order["order_type"])
        print("\nORDERED ITEMS")
        print("-" * 55)
        for item in selected_order["items"]:
            print("Food       :", item["name"])
            print("Price      : PHP", f"{item['price']:.2f}")
            print("Quantity   :", item["quantity"])
            print("Subtotal   : PHP", f"{item['subtotal']:.2f}")
            print("-" * 55)
        print("Total Amount : PHP", f"{selected_order['total']:.2f}")
        print("Payment      :", selected_order["payment_method"])
        if selected_order["payment_method"] == "Online":
            print("Online Mode  :", selected_order["online_method"])
        print("Prep Time    :", selected_order["prep_time"], "minutes")
        print("Order Status :", selected_order["status"])
        print("=" * 55)
    except ValueError:
        print("\nPlease enter a valid order number.")

# ==========================================
#              UPDATE ORDER STATUS

# ==========================================


def update_order_status():
    if not orders:
        print("\nNo orders available.")
        return
    try:
        order_number = int(input("\nEnter Order Number: "))
        selected_order = None
        for order in orders:
            if order["order_number"] == order_number:
                selected_order = order
                break
        if selected_order is None:
            print("\nOrder not found.")
            return
        print("\nCustomer :", selected_order["customer"])
        print("Current Status :", selected_order["status"])
        print("\n1. Preparing")
        print("2. Ready for Pickup / Serving")
        print("3. Completed")
        choice = input("\nSelect New Status: ")
        if choice == "1":
            selected_order["status"] = "Preparing"
        elif choice == "2":
            selected_order["status"] = "Ready"
        elif choice == "3":
            selected_order["status"] = "Completed"
        else:
            print("\nInvalid selection.")
            return
        print("\nOrder status successfully updated!")
        print("New Status:", selected_order["status"])
    except ValueError:
        print("\nInvalid order number.")

# ==========================================
#               USER MENU

# ==========================================


def user_menu():
    print("\n" + "=" * 50)
    print("               CUSTOMER ORDERING")
    print("=" * 50)
    customer = input("\nEnter Customer Name: ")
    print("\nWelcome,", customer + "!")
    print("Please select your favorite meals.")
    order_items = []
    total = 0
    selected_prep_times = []
    # FOOD ORDERING
    while True:
        print("\n" + "=" * 50)
        print("                  FOOD MENU")
        print("=" * 50)
        categories = list(menu.keys())
        for number, category in enumerate(categories, 1):
            print(f"{number}. {category}")
        print("0. Finish Order")
        try:
            category_choice = int(input("\nSelect Food Category: "))
            if category_choice == 0:
                if not order_items:
                    print("Please select at least one food item.")
                    continue
                break
            if category_choice < 1 or category_choice > len(categories):
                print("Invalid category.")
                continue
            selected_category = categories[category_choice - 1]
            print("\n" + "-" * 50)
            print("             " + selected_category.upper())
            print("-" * 50)
            for number, item in menu[selected_category].items():
                food, price, prep_time = item
                print(
                    f"{number}. {food:35} "
                    f"PHP {price:.2f}"
                )
            print("-" * 50)
            food_choice = int(input("\nSelect Food Number: "))
            if food_choice not in menu[selected_category]:
                print("Invalid food number.")
                continue
            quantity = int(input("Enter Quantity: "))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue
            food_name, price, prep_time = menu[selected_category][food_choice]
            subtotal = price * quantity
            order_items.append({
                "name": food_name,
                "price": price,
                "quantity": quantity,
                "subtotal": subtotal
            })
            total += subtotal
            selected_prep_times.append(prep_time)
            print("\nSuccessfully Added to Order!")
            print("Food:", food_name)
            print("Quantity:", quantity)
            print(f"Subtotal: PHP {subtotal:.2f}")
            print(f"Current Total: PHP {total:.2f}")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # ======================================
    #              ORDER TYPE

    # ======================================
    print("\n" + "=" * 50)
    print("                  ORDER TYPE")
    print("=" * 50)
    print("1. Dine In")
    print("2. Takeout")
    while True:
        order_choice = input("\nSelect Order Type: ")
        if order_choice == "1":
            order_type = "Dine In"
            break
        elif order_choice == "2":
            order_type = "Takeout"
            break
        else:
            print("Invalid selection.")

    # ======================================
    #          RANDOM ORDER NUMBER

    # ======================================
    existing_numbers = [order["order_number"] for order in orders]
    while True:
        order_number = random.randint(1000, 9999)
        if order_number not in existing_numbers:
            break

    # ======================================
    #             PAYMENT METHOD

    # ======================================
    print("\n" + "=" * 50)
    print("                PAYMENT METHOD")
    print("=" * 50)
    print("1. Cash")
    print("2. Online Payment")
    while True:
        payment_choice = input("\nSelect Payment Method: ")
        if payment_choice == "1":
            payment_method = "Cash"
            online_method = "N/A"
            print("\nPLEASE PROCEED TO THE CASHIER.")
            print("Pay your order at the cashier counter.")
            break
        elif payment_choice == "2":
            payment_method = "Online"
            print("\n--------- ONLINE PAYMENT ---------")
            print("1. GCash")
            print("2. GoTyme")
            while True:
                online_choice = input("\nSelect Online Payment: ")
                if online_choice == "1":
                    online_method = "GCash"
                    break
                elif online_choice == "2":
                    online_method = "GoTyme"
                    break
                else:
                    print("Invalid selection.")
            print("\nSelected Payment:", online_method)
            print("Please complete payment using the")
            print("official payment instructions or QR code.")
            print("Payment is not automatically verified.")
            break
        else:
            print("Invalid payment method.")

    # ======================================
    #           PREPARATION TIME

    # ======================================
    # Estimated time uses the longest item
    # preparation time plus a small handling time.
    prep_time = max(selected_prep_times) + 5

    # ======================================
    #            SAVE CUSTOMER ORDER

    # ======================================
    new_order = {
        "order_number": order_number,
        "customer": customer,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "items": order_items,
        "total": total,
        "order_type": order_type,
        "payment_method": payment_method,
        "online_method": online_method,
        "prep_time": prep_time,
        "status": "Preparing"
    }
    orders.append(new_order)

    # ======================================
    #              ORDER RECEIPT

    # ======================================
    print("\n\n")
    print("=" * 55)
    print("                    JOLLIBEE")
    print("                  ORDER RECEIPT")
    print("=" * 55)
    print("Customer Name :", customer)
    print("Order Number  :", order_number)
    print("Order Type    :", order_type)
    print("Date          :", new_order["date"])
    print("-" * 55)
    print(f"{'ITEM':28} {'QTY':5} {'AMOUNT':10}")
    print("-" * 55)
    for item in order_items:
        print(
            f"{item['name'][:27]:28} "
            f"{item['quantity']:<5} "
            f"{item['subtotal']:>10.2f}"
        )
    print("-" * 55)
    print(f"{'TOTAL AMOUNT':33} PHP {total:.2f}")
    print("-" * 55)
    print("Payment Method :", payment_method)
    if payment_method == "Online":
        print("Online Service :", online_method)
    print("Estimated Prep :", prep_time, "minutes")
    print("=" * 55)
    print("             THANK YOU FOR ORDERING!")
    print("                  ENJOY YOUR MEAL!")
    print("=" * 55)

    # ======================================
    #           ORDER NOTIFICATION

    # ======================================
    print("\n              ORDER REMINDER")
    print("-" * 55)
    print("Your Order Number:", order_number)
    print("Estimated Preparation:", prep_time, "minutes")
    if order_type == "Dine In":
        print("\nPlease wait for your order number to be called.")
        print("Your meal will be served when ready.")
    else:
        print("\nPlease wait for your order number at the")
        print("takeout / pickup counter.")
    print("-" * 55)
    print("Your order has been submitted successfully!")

# ==========================================
#              RUN THE SYSTEM

# ==========================================
if __name__ == "__main__":
    main_menu()
