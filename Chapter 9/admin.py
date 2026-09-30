from user import User

class Privileges:
    """Represents a list of priviledges"""

    def __init__(self):
        self.privileges = ["Can delete users", "Can power trip", "can get rekt"]

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    '''Defines an admin type of user'''

    def __init__(self, first_name, last_name, middle_name, city, state):
        super().__init__(first_name, last_name, middle_name, city, state)
        self.privileges = Privileges()