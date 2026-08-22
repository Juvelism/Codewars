coffee_menu = [
    {"name": "Espresso", "price": 50, "stock": 5},
    {"name": "Latte", "price": 70, "stock": 3},
    {"name": "Cappuccino", "price": 80, "stock": 2}
]


print("=== COFFEE MENU ===\n")

for menu in coffee_menu:
    print(f'{menu["name"]} - P{menu["price"]}')

customer_chooses = input("\nChoose Coffee: ").title()

coffee_found = []

coffee__found = False
coffee_out_stock = False

for coffee in coffee_menu:
    if coffee['name'] == customer_chooses:
        coffee_found.append(coffee)
        coffee_found = True

if coffee_found is False:
    print("Coffe not found!")
