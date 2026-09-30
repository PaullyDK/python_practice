favorite_numbers = {
    'Fred': [12, 69, 420],
    'Shaggy': [420, 69],
    'Velma': [13, 69],
    'Scooby': [2, 69],
    'Daphne': [69]
    }

for key, numbers in favorite_numbers.items():
    print(f"\n{key}'s favorite numbers are:")

    for number in numbers:
        print(number)