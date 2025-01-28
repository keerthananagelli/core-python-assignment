def add_item(menu, item):
    """Add a new item to the menu."""
    if item not in menu:
        menu.append(item)


def remove_item(menu, item):
    """Remove an item from the menu."""
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} not found in the menu.")


def check_item(menu, item):
    """Check if an item is available in the menu."""
    return f"{item} is {'available' if item in menu else 'not available'}."


# Example usage
menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item(menu, "Tacos")
remove_item(menu, "Salad")
print("Updated menu:", menu)
print(check_item(menu, "Pizza"))
