import random
class Die(object):
    def __init__(self, sides = 6):
        self.sides = sides
        self.held = False
        self.die_face = 1
    def change_held(self, held):
        self.held = held
    def roll_die(self):
        if (self.held == False):
            self.die_face = random.randint(1, self.sides)
        else:
            pass
    def get_die_face(self):
        return self.die_face
