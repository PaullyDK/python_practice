keep = 0

while keep < 1:
    topping = input("What topping do you want on your pizza? Enter 'quit' to stop: ")
    
    if topping == 'quit':
        keep = 1
    else:
        print(f"Adding {topping} to the pizza.")

    
        