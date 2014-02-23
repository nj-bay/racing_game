import random

class Dice(object):

    def __init__(self):
        #random.seed(4)
        self.dice_value = random.randint(1, 6)

    #def __repr__(self):
        #return self.dice_value
    def get_value(self):
        return self.dice_value
