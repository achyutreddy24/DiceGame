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
    
class DiceBag(object):
    def __init__(self):
        self.dice = []
        self.dice_roll = []
    def add_die_obj(self, die_obj):
        self.dice.append(die_obj)
    def remove_die(self, die_obj):
        self.dice.remove(die_obj)
    def remove_die_index(self, index):
        del self.dice[index]
    def add_die_notation(self, standard_die_notation):
        lst_notation = standard_die_notation.split("d")
        for i in int(lst_notation[0]):
            die1 = Die(int(lst_notation[1]))
            self.dice.append(die1)
