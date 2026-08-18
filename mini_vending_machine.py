coffee_menu = [
    {"name": "Espresso", "price": 50, "stock": 5},
    {"name": "Latte", "price": 70, "stock": 0},
    {"name": "Cappuccino", "price": 80, "stock": 2}
]


print("=== COFFEE MENU ===\n")

# DISPLAY COFFEE MENU
for menu in coffee_menu:
    print(f'{menu["name"]} - {menu["price"]}')

customer_choice = input("\nChoose Coffee: ").title()
print(f"\nYou selected: {customer_choice}")

for coffee in coffee_menu:
    print(coffee)
