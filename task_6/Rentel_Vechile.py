class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self, days):
        return self.rental_rate * days


# Car Class
class Car(Vehicle):
    def calculate_rental(self, days):
        return self.rental_rate * days + 500   # extra service charge


# Bike Class
class Bike(Vehicle):
    def calculate_rental(self, days):
        return self.rental_rate * days


# Truck Class
class Truck(Vehicle):
    def calculate_rental(self, days):
        return self.rental_rate * days + 1000  # loading charge



vehicles = [
    Car("Swift", 2000),
    Bike("Pulsar", 500),
    Truck("Tata Truck", 4000)
]

days = 3

for v in vehicles:
    print(v.model, "Rent:", v.calculate_rental(days))