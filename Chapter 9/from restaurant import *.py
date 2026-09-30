from restaurant import *

restaurant = Restaurant('IHOP', 'pancakes')

print(restaurant.number_served)

restaurant.set_number_served(420)

print(restaurant.number_served)

restaurant.increment_number_served(69)

print(restaurant.number_served)