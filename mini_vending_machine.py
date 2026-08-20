coffee_menu = [
    {"name": "Espresso", "price": 50, "stock": 5},
    {"name": "Latte", "price": 70, "stock": 3},
    {"name": "Cappuccino", "price": 80, "stock": 2}
]


print("=== COFFEE MENU ===\n")

for menu in coffee_menu:
    print(f'{menu["name"]} - P{menu["price"]}')

customer_chooses = input("\nChoose Coffee: ").title()

coffee_found = False

for coffee in coffee_menu:
    if coffee['name'] == customer_chooses:
        coffee_found = True
        print(coffee['name'])
    else:
        print("Coffe not found")
        coffee_found = False
