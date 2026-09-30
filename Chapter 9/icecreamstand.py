from restaurant import *

class IceCreamStand(Restaurant):
    """Presents an instance of an ice cream stand"""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        
        print("Available Flavors:")
        for flavor in self.flavors:
            print(flavor)

    