guest_quantity = int(input("How many dinner guests are in your party? "))

if guest_quantity > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")