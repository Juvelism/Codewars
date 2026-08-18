coffee_menu = [
    {"name": "Espresso", "price": 50, "stock": 5},
    {"name": "Latte", "price": 70, "stock": 3},
    {"name": "Cappuccino", "price": 80, "stock": 2}
]


print("=== COFFEE MENU ===\n")

# VIEW OF MENU
for menu in coffee_menu:
    print(f'{menu["name"]} - {menu["price"]}')

customer_choice = input("\nChoose Coffee: ").title()

print(f"\nYou selected: {customer_choice}")

for price in coffee_menu:
    if price['name'] == customer_choice:
        print(f"Price: {price['price']}")
