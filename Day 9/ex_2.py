class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

class ElectricCar(Car):
    def __init__(self, model, color, battery_type):
        super().__init__(model, color)
        self.battery_type = battery_type

my_car = ElectricCar("BMW iX", "red", "molten salt")

print("Car's model is: ", my_car.model)
print("Car's color is: ", my_car.color)
print("Car's battery type is: ", my_car.battery_type)