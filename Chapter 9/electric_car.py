class Car:
    """Represents an instance of a car"""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Battery:
    """Represents a battery for an electric car"""

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrades the capacity of the battery."""
        if self.battery_size != 65:
            self.battery_size = 65

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_leaf = ElectricCar('nissan', 'leaf', 2024)
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()


