import random

class GameMap(object):
    def __init__(self):
        self.length = random.randint(10, 30)


    def get_length(self):
        return self.length

