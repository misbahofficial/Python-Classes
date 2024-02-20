class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f"Welcome to {self.name} restaurant.")
        print(f"We have {self.cuisine} cuisine to offer you!")

    def open_restaurant(self):
        print(f"{self.name} restaurant is open.")


class User:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''

    def greet_user(self):
        print(f"Good morning {self.first_name} {self.last_name}!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)

        self.flavours = ['Chocolate', 'Strawberry', 'Vanilla', 'Apple']

    def display_flavours(self):
        for item in self.flavours:
            print(item)


ice_cream = IceCreamStand('Seasons', 'Bengali')


# ice_cream.display_flavours()


class Admin(User):
    def __init__(self):
        super().__init__()

        self.privileges = ['can add post', 'can ban user', 'can delete a comment']

    def show_privileges(self):
        for item in self.privileges:
            print(item)


admin1 = Admin()

# admin1.show_privileges()


class Privileges(Admin):
    def __init__(self):
        super().__init__()


# p1 = Privileges()
# p1.greet_user()
