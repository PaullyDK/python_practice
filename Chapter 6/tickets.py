while True:
    ticket_price = input("Enter your age and I will tell you the price of your movie ticket. " \
    "Enter 'quit' to stop: ")

    if ticket_price == 'quit':
        break

    try:
        age = int(ticket_price)

        if int(ticket_price) < 3:
            print("Your ticket is free!")
        elif int(ticket_price) < 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")
    
    except ValueError:
        print("This input is invalid. Please enter 'quit' or an integer.")
