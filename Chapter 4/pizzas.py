pizzas = ["Meat Lovers", "Pepperoni", "Breakfast"]

friend_pizzas = pizzas[:]

pizzas.append("Barbecue")
friend_pizzas.append("Hawaiian")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friends favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)