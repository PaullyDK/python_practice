from pathlib import Path

name_string = ''
while True:
    name = input("What is your name? Enter 'quit' to quit: ")

    if name == 'quit':
        break
    else:
        name_string += name + '\n'

path = Path('guest_book.txt')
path.write_text(name_string)