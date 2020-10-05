import random


krump_stats = {
    'weapon_skill': 60,
    'ballistics_skill': 30,
    'strength_mod': 11,
}

class Weapon(object):
    def roll_for_hit(self, skill_value, modifiers=0):
        percent = random.randint(1, 100)
        if 

    def roll_for_damage(self):
        rolls = self.num_dice
        total_damage = 0
        while rolls > 0:
            damage_roll = random.randint(1, 10)

            if damage_roll == 10:
                rolls += 1
            rolls -= 1



class BrotherKrump(object):
    def __init__(self, weapon_skill=

def roll_for_damage():
    pass


def roll_for_hit(): 
