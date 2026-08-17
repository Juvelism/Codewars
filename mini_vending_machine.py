coffee_menu = [
    {"name": "Espresso", "price": 50, "stock": 5},
    {"name": "Latte", "price": 70, "stock": 3},
    {"name": "Cappuccino", "price": 80, "stock": 2}
]


print("=== COFFEE MENU ===\n")

for menu in coffee_menu:
    print(f'{menu["name"]} - {menu["price"]}')

coffee_name = input("\nChoose Coffee: ")

print(f'You selected: {coffee_name.title()}')
print(f'Price: P{coffee_menu["price"]}')
