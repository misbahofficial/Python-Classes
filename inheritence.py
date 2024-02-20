class Car():
    # A simple attempt to represent a car
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    def __init__(self, battery_size=70):
        # Initialize the battery's attribute
        self.battery_size = battery_size

    def describe_battery(self):
        # printing a statement describing the battery size
        print(f"This car has {self.battery_size} kWh battery.")


# A child class of Car class
class ElectricCar(Car):
    # Represents aspects of car , specific to electric vehicle
    def __init__(self, make, model, year):
        # Initialize attribute of the parent class
        super().__init__(make, model, year)

        self.battery = Battery()


my_tesla = ElectricCar('Tesla', 'Model S', 2016)
my_tesla.battery.describe_battery()
