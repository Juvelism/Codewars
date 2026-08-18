coffee_menu = [
    {"name": "Espresso", "price": 50, "stock": 5},
    {"name": "Latte", "price": 70, "stock": 3},
    {"name": "Cappuccino", "price": 80, "stock": 2}
]


print("=== COFFEE MENU ===\n")

# VIEW OF MENU
for menu in coffee_menu:
    print(f'{menu["name"]} - {menu["price"]}')

coffee_name = input("\nChoose Coffee: ")

print(coffee_menu['name']['price'])
