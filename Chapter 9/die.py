from random import randint

class Die:
    """A simulation of a die that can have any number of sides."""

    def __init__(self, sides=6):
        """Initialize the die with a given number of sides (default is 6)."""
        self.sides = sides

    def roll_die(self):
        """
        Roll the die and print a random number between 1 and the number of 
        sides.
        """
        print(randint(1, self.sides))
