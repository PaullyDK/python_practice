from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
    
def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    location = input("Where do you live? ")
    gender = input("What is your gender? ")

    data = {'username': username, 'location': location, 'gender': gender}

    contents = json.dumps(data)
    path.write_text(contents)
    return data

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        response = input(f"Are you {username['username']}? (yes/no) ")
        if response == 'yes':
            print(f"Welcome back, {username['username']}!")
            print(f"You are a {username['gender']} and you live in {username['location']}.")
        else:
            username = get_new_username(path)
            print(f"We'll remember you when you come back, {username['username']}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username['username']}!")

greet_user()