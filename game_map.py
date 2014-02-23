import random

class GameMap(object):
    def __init__(self):
        self.length = random.randint(10, 31)
        self.position = 0

    def get_length(self):
        return self.length

    def bool_win(self):
        if self.position >= self.length:
            return True
        else:
            # if self.distance > map_length:
            #     self.distance = map_length - (self.distance - map_length)
            return False

    def new_position(self, spaces):
        self.position += spaces


