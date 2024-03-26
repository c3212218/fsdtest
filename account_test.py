# Import the Car class from car.py
from car import Car

class Account:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")

# Now you can use the Car class here
my_car = Car("Toyota", "Camry")
print("My car:", my_car.get_info())

