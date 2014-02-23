#from dice import Dice
from game_map import GameMap
from vehicle import *



###1. chose your vehicle
print "Welcome to the Racing Game!!!!!!!"
#instructions
response = raw_input("What vehicle would you like to choose? (c)ar, (m)otorcycle, (b)ike, (q)uit")

while response != "q":
    print "We are playing the Game"
    if response == "c":
        print("let's start driving a car!")
        myVeh = Car()
    elif response == "m":
        print("let's drive a Motorcycle")
        myVeh = Motorcycle()
    elif response == "b":
        print("let's ride a Bike")
        myVeh = Bike()
    else:
        print "your input was invalid"
        response = raw_input("What vehicle would you like to choose? (c)ar, (m)otorcycle, (b)ike, (q)uit")
        continue

    new_map = GameMap()                #set vehicles


    while new_map.bool_win() is False:
        spaces = myVeh.run()
        print "The car is moving space %d" % spaces
        new_map.new_position(spaces)
        print "New position is %d" % new_map.position


    print "We are Finished Racing"

    response = raw_input( "Do you wish to play again? What vehicle would you like to choose? (c)ar, (m)otorcycle, (b)ike, (q)uit")




###2. initial Map



###3. ask player to roll dice and show the result






###
#dice = Dice()
#value = dice.get_value()
#print "Dice Value %d" % (value)

#myVeh = Vehicle()
#myCar = Car()
#myMoto = Motorcycle()
#myBike = Bike()
# game_map = GameMap()
# map_length = game_map.get_length()


# myVeh.run()
# print "Veh distance %d" %  myVeh.get_distance()

#myCar.run()
#print "Car distance %d" % ( myCar.get_distance() )

# game_map = GameMap()
# map_length = game_map.get_length()

# print "Map length %d" % (map_length)
#print "Value %d, %s, %c, %f" % (value, myname, mychar, myfloat)
