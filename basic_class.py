class Car():
    # A simple attempt to represent a car
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class User():
    def __init__(self, first_name, last_name, rank, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.rank = rank
        self.age = age
        self.location = location
        self.number_served = 0
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def set_number_served(self):
        # self.number_served += serves
        return self.number_served

    def increment_number_served(self):
        self.number_served += 1

    def describe_user(self):
        label_width = 10  # Adjust this value as needed
        print(f'''
First Name: {self.first_name:<{label_width}}
Last Name:  {self.last_name:<{label_width}}
Age:        {self.age:<{label_width}}
Rank:       {self.rank:<{label_width}}
Location:   {self.location:<{label_width}}
''')

    def greet_user(self):
        print(f'Good Morning {self.first_name} {self.last_name}')


user1 = User('Misbah', 'Ahmed', 'Noob', 24, 'Sylhet')
# print(user1.login_attempts)
# user1.increment_login_attempts()
# print(user1.login_attempts)
# user1.increment_login_attempts()
# print(user1.login_attempts)
# user1.increment_login_attempts()
# print(user1.login_attempts)
# user1.increment_login_attempts()
# print(user1.login_attempts)
# user1.reset_login_attempts()
# print(user1.login_attempts)

# user1.describe_user()
# user1.greet_user()
