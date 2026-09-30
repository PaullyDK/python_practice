from pathlib import Path

book_one_path = Path('book.txt')
book_one = book_one_path.read_text()

book_one_count = book_one.lower().count('the')
print(f"Book one has {book_one_count} instances of 'the'.")


book_two_path = Path('book2.txt')
book_two = book_two_path.read_text()

book_two_count = book_two.lower().count('the ')
print(f"Book two has {book_two_count} instances of 'the'.")


book_three_path = Path('book3.txt')
book_three = book_three_path.read_text()

book_three_count = book_three.lower().count('the ')
print(f"Book three has {book_three_count} instances of 'the'.")