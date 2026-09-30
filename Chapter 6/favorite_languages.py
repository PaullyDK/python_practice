favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

people_who_should_take_poll = ['sarah', 'jen', 'archibald', 'paul']

for people in people_who_should_take_poll:
    if people in favorite_languages:
        print("Thank you for taking the poll!")
    else:
        print("You need to take the poll!")