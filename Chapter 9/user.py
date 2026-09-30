class User:
    def __init__(self, first_name, last_name, middle_name, city, state):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.city = city
        self.state = state
        self.login_attempts = 0

    def describe_user(self):
        print(f"The user's full name is {self.first_name.title()} " 
            f"{self.middle_name.title()} {self.last_name.title()}, and they " 
            f"live in {self.city.title()}, {self.state.title()}.")
        
    def greet_user(self):
        print(f"Hi, {self.first_name.title()}!")

    def increment_login_attempts(self):
        """Increments the amount of login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the amount of login attempts"""
        self.login_attempts = 0