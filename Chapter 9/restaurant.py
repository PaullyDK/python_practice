class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints the restaurant type and name."""
        print(f"It's a {self.cuisine_type} restaurant called {self.restaurant_name}.")

    def open_restaurant(self):
        """Informs the user that the restaurant is now open."""
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number_served):
        """Sets the number of people served by this restaurant"""
        self.number_served = number_served

    def increment_number_served(self, number_added):
        """Increments the number of people the restuarant has served"""
        self.number_served += number_added

        
    