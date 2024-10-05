# Exceeding requirements:
# - Not letting the user input an option that is not available in the menu
# - Ask the user to say how many units of the item they would like to buy
# - Showing a custom message when the cart is empty
# - Showing which item got removed from the cart
# - Not letting the user input an item that does not exist on the cart to be removed

print("Welcome to the Shopping Cart Program!")

option = 0
cart_items = []
cart_item_amounts = []
cart_item_prices = []

while option != 5:
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    option = int(input("Please enter an action: "))

    if option == 1:
        item = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{item}'? "))
        amount = 0
        while amount <= 0:
            amount = int(input("How many of those are you buying? "))
            if amount <= 0:
                print(f"Please input a valid amount of '{item}'")
        cart_items.append(item)
        cart_item_prices.append(price)
        cart_item_amounts.append(amount)
        print(f"{amount} '{item}' has/have been added to the cart.")

    elif option == 2:
        if len(cart_items) > 0:
            print("The contents of the shopping cart are:")
            for i in range(len(cart_items)):
                item = cart_items[i]
                price = cart_item_prices[i]
                amount = cart_item_amounts[i]
                print(f"{i + 1}. {item} (x{amount}) - ${price:.2f}")
        else:
            print("There are no items on your cart. Please buy something :D")

    elif option == 3:
        item_to_remove = int(input("Which item would you like to remove? "))
        if item_to_remove > 0 and item_to_remove <= len(cart_items):
            item = cart_items[item_to_remove]
            cart_items.pop(item_to_remove - 1)
            cart_item_prices.pop(item_to_remove - 1)
            cart_item_amounts.pop(item_to_remove - 1)
            print(f"Item '{item}' removed.")
        else:
            print(f"Sorry. The item {item_to_remove} is not on your cart. :(")

    elif option == 4:
        sum = 0
        for i, price in enumerate(cart_item_prices):
            amount = cart_item_amounts[i]
            sum += price * amount
        print(f"The total price of the items in the shopping cart is ${sum:.2f}")

    elif option == 5:
        print("Thank you. Goodbye.")

    else:
        print(f"Sorry. The option {option} is invalid. Please, try again. :)")

    print()
