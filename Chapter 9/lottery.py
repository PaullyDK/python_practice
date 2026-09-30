from random import choice

lottery_selection = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b',
                     'c', 'd', 'e', 'f']

winning_number = ''
for i in range(4):
    winning_number += choice(lottery_selection)

print(f"The winning number is: {winning_number}")

number_of_pulls = 0
while True:
    pull = ''
    for i in range(4):
        pull += choice(lottery_selection)
    
    number_of_pulls += 1
    if pull == winning_number:
        print(f"It took {number_of_pulls} pulls to get the winning number.")
        break