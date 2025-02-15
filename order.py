#!/usr/bin/env python3 

"""A program to calculate the total for a fast food order."""

__author__ = "Lydia Frame"
__date__ = "02/15/2025"


# Constants for menu items and their prices
BURGER_PRICE = 1.99
FRIES_PRICE = 0.99
DRINK_PRICE = 1.59
CHICKEN_PRICE = 1.79

def get_item_and_quantity():
    """Prompts the user to input an item and the quantity they want to order.
    
    Returns:
        tuple: A tuple containing the item name (string) and the quantity (integer).
    """
    item = input("Item? ").lower()
    print()
    quantity = int(input("Qty? "))
    print()
    
    return item, quantity


def calculate_price(item, quantity):
    """Calculates the price for a given item and quantity.
    
    Args:
        item (str): The name of the item (burger, fries, drink, or chicken).
        quantity (int): The quantity of the item the user wants to purchase.
    
    Returns:
        float: The total price for the given item and quantity. Returns 0 if the item is invalid.
    """
    
    if item == "burger":
        return BURGER_PRICE * quantity
    elif item == "fries":
        return FRIES_PRICE * quantity
    elif item == "drink":
        return DRINK_PRICE * quantity
    elif item == "chicken":
        return CHICKEN_PRICE * quantity
    return 0  # Return 0 if the item is invalid

def main():
    subtotal = 0
    while True:
        item, quantity = get_item_and_quantity()
        
        # Calculate price for the item, if invalid, price will be 0
        price = calculate_price(item, quantity)
        
        if price == 0:
            print("Invalid item entered. Try again.")
            continue
        
        subtotal += price

        # Print the current subtotal
        print("Subtotal = $" + str(round(subtotal, 2)))

        # Ask if the user wants to continue
        more_items = input("More? ").lower()
        print()
        if more_items != "y":
            break

    # Print the total
    print("Order total: $" + str(round(subtotal, 2)))

if __name__ == "__main__":
    main()
