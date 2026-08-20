coffee_menu = [
    {"name": "Espresso", "price": 50, "stock": 5},
    {"name": "Latte", "price": 70, "stock": 3},
    {"name": "Cappuccino", "price": 80, "stock": 2}
]


user_input = input("What: ")

for i in coffee_menu:
    print(i['name'], i['price'])
