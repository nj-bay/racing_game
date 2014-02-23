#from dice import Dice
from game_map import GameMap
from vehicle import *



###1. choice your vehical
print "Welcome to the Racing Game!!!!!!!"

response = raw_input("")
###2. initial Map



###3. ask player to dice and show the result






###
#dice = Dice()
#value = dice.get_value()
#print "Dice Value %d" % (value)

myVeh = Vehicle()
myCar = Car()
myMoto = Motorcycle()
myBike = Bike()


myVeh.run()
print "Veh distance %d" % ( myVeh.get_distance() )

myCar.run()
print "Car distance %d" % ( myCar.get_distance() )

game_map = GameMap()
map_length = game_map.get_length()

print "Map length %d" % (map_length)
#print "Value %d, %s, %c, %f" % (value, myname, mychar, myfloat)
