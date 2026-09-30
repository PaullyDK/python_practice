responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would" \
    " you go? ")

    responses[name] = response

    repeat = input("Let someone else respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to visit {response}.")