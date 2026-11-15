# Menu dictionary jisme item ka naam (key) aur price (value) hai
menu = {
    "Burger": 120,
    "Pizza": 250,
    "Fries": 80,
    "Coke": 40
}

# Cart list jisme customer ke add kiye gaye items store honge
cart = []
discount_applied = False

# Menu Dikhana 
def show_menu():
    for item in menu:
        print(item, "- Rs.", menu[item])

# Cart Mein Item Dhundhna :
def find_in_cart(name):
    for i in range(len(cart)):
        if cart[i]["name"] == name:
            return i
    return -1

# Subtotal nikalne k liye :
def calculate_subtotal():

    subtotal = 0

    for food in cart:

        item = food[0]
        quantity = food[1]

        price = menu[item]

        subtotal = subtotal + (price * quantity)

    return subtotal

# Item add karna (validation ke saath):
def add_item():

    show_menu()

    item = input("\nEnter food item name: ").strip().title()

    # Item ki avalibality check krna:
    if item not in menu:
        print("Sorry! This item is not available.")
        return

    # Item ki quantity check karna :
    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

    except ValueError:
        print("Please enter quantity in numbers.")
        return

    # Item ko cart me add karna :
    cart.append([item, quantity])

    print(item, "added to cart successfully!")

# Item hatana :

def remove_item():

    item = input("Enter item name to remove: ").title()

    for food in cart:

        if food[0] == item:
            cart.remove(food)
            print(item, "removed successfully.")
            return

    print("Item not found in cart.")

# Coupon lagana or 10% discount: 

def apply_coupon(code):
    global coupon_used
    code = code.strip().upper()

    if code == "SAVE10":
        coupon_used = code
    else:
        print("Invalid coupon code. Only SAVE10 is accepted.")


# Checkout (billing ka main part ):

def checkout():
    # Step 1: Check karna ki cart khali toh nahi hai
    if not cart:
        print("Your cart is empty! Please add items before checkout.")
        return

    # Step 2: Subtotal calculate karna
    subtotal = sum(item["price"] * item["qty"] for item in cart)

    # Step 3: Discount calculate karna (10% agar SAVE10 laga hai)
    if discount_applied:
        discount = subtotal * 0.10
        discount_text = f"Discount (10%): {discount:.2f}"
    else:
        discount = 0.00
        discount_text = f"Discount: {discount:.2f}"

    # Discount ke baad bacha hua amount
    amount_after_discount = subtotal - discount

    # Step 4: GST (5% of amount after discount)
    gst = amount_after_discount * 0.05

    # Step 5: Delivery Charge (Free agar subtotal >= 300, warna 40)
    if subtotal >= 300:
        delivery = 0
        delivery_text = "0 (free)"
    else:
        delivery = 40
        delivery_text = "40"

    # Step 6: Final Total nikalna
    total = amount_after_discount + gst + delivery

    # Step 7: Bill print karna (Exact Test Case format mein)
    print(f"Subtotal: {subtotal} | {discount_text}")
    print(f"GST (5%): {gst:.2f} | Delivery: {delivery_text}")
    print(f"Total: {total:.2f}")


# Main Menu loop :  (Program ko baar baar chlana jab tak customer exit select na kare)

while True:

    print("\n===== ONLINE FOOD ORDERING SYSTEM =====")
    print("1. Show Menu")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Search Item")
    print("5. View Cart")
    print("6. Checkout")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_menu()

    elif choice == "2":
        add_item()

    elif choice == "3":
        remove_item()

    elif choice == "4":
        search_item()

    elif choice == "5":
        show_cart()

    elif choice == "6":
        checkout()

    elif choice == "7":
        print("Thank you for visiting!")
        break

    else:
        print("Invalid choice. Please try again.")