print("-----rectangle area-------")
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area_compute = (self.length * self.width)
        return area_compute

r1 = Rectangle(2, 3)
print(r1.area())

print("------inheritance bus sample-------")
class Vehicle:
    def __init__(self, max_speed, mileage_instance):
        self.max_speed =max_speed
        self.mileage_instance = mileage_instance
class Bus(Vehicle):
    pass