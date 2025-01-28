def calculate_total_price(cart_items):
    """
    Calculate the total price of items in the cart.
    Applies a 10% discount if the cart contains more than 5 items.
    Handles the case of an empty cart.
    """
    if not cart_items:
        return "Cart is empty."

    total_price = sum(cart_items.values())
    if len(cart_items) > 5:
        discount = total_price * 0.10
        total_price -= discount
    return f"Total Price: {total_price}"


# Example usage
cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
print(calculate_total_price(cart_items))
