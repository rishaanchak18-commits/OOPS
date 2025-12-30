class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
car = Vehicle(180, 15)
print("Car max speed:", car.max_speed)
print("Car mileage:", car.mileage)