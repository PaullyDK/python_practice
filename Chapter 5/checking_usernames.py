current_users = ['Fred', 'Shaggy', 'Scooby', 'Velma', 'Daphne']

new_users = ['Fred', 'Shaggy', 'Paul', 'Nishan', 'Whitney']

lower_current_users = [item.lower() for item in current_users]

for new_user in new_users:
    if new_user.lower() in lower_current_users:
        print("Username already taken. Enter a new username.")
    else:
        print(f"{new_user} is available!")
