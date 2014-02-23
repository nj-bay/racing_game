from dice import Dice

class Vehicle(object):
    def __init__(self):
        self.vehicle_dice = Dice()
        self.name = "Vehicle"
        self.distance = 0

    def run(self):
        self.distance += self.vehicle_dice.get_value()

    def get_distance(self):
        return self.distance

    def bool_win(self, map_length):
        if self.distance == map_length:
            return true
        else:
            if self.distance > map_length:
                self.distance = map_length - (self.distance - map_length)
            return false



class Car(Vehicle):
    def __init__(self):
        self.car_dice = Dice()
        self.car_dice1 = Dice()
        self.car_dice2 = Dice()
        self.name = "Car"
        self.distance = 0
    def run(self):
        self.distance += self.car_dice.get_value()
        self.distance += self.car_dice1.get_value()
        self.distance += self.car_dice2.get_value()

class Motorcycle(Vehicle):
    def __init__(self):
        self.motor_dice = Dice()
        self.motor_dice1 = Dice()
        self.name = "Car"
        self.distance = 0
    def run(self):
        self.distance += self.motor_dice.get_value()
        self.distance += self.motor_dice1.get_value()

class Bike(Vehicle):
    def __init__(self):
        self.bike_dice = Dice()
        self.name = "Bike"
        self.distance = 0
