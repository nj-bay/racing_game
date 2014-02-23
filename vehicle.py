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
#switched true to false and vice versa




class Car(Vehicle):
    def __init__(self):
        self.car_dice = Dice()
        self.car_dice1 = Dice()
        self.car_dice2 = Dice()
        self.name = "Car"
        #self.distance = 0
        self.position = 0
    def run(self):
        # self.distance += self.car_dice.get_value()
        # self.distance += self.car_dice1.get_value()
        # self.distance += self.car_dice2.get_value()
        space = self.car_dice.get_value()
        # + self.car_dice1.get_value() + self.car_dice2.get_value()
        return space

    # def set_position(position):
    #     self.position = position

    # def get_position():
    #     return self.position

class Motorcycle(Vehicle):
    def __init__(self):
        self.motor_dice = Dice()
        self.motor_dice1 = Dice()
        self.name = "Motorcycle"
        #self.distance = 0
        self.position = 0
    def run(self):
        # self.distance += self.motor_dice.get_value()
        # self.distance += self.motor_dice1.get_value()
        space = self.motor_dice.get_value()
        # + self.car_dice1.get_value() + self.car_dice2.get_value()
        return space

    # def set_position(position):
    #     self.position = position

    # def get_position():
    #     return self.position


class Bike(Vehicle):
    def __init__(self):
        self.bike_dice = Dice()
        self.name = "Bike"
        #self.distance = 0
        self.position = 0
    def run(self):
        # self.distance += self.motor_dice.get_value()
        # self.distance += self.motor_dice1.get_value()
        space = self.bike_dice.get_value()
        # + self.car_dice1.get_value() + self.car_dice2.get_value()
        return space

    # def set_position(position):
    #     self.position = position

    # def get_position():
    #     return self.position
