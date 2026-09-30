from pathlib import Path

    
try:    
    cat_path = Path('cats.txt')
    cats = cat_path.read_text()
    print("List of cats: ")
    print(cats)
except FileNotFoundError:
    pass

try:    
    dog_path = Path('dogs.txt')
    dogs = dog_path.read_text()
    print("List of dogs: ")
    print(dogs)
except FileNotFoundError:
    pass