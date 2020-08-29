from random import randint

class Weapon:

    def __init__(self, name="dagger", damage_dice=1, damage_amt=4):
        self.name = name
        self.damage_dice = damage_dice
        self.damage_amt = damage_amt

    def roll_damage(self):
        total = 0
        for x in range(0, self.damage_dice):
            total += randint(1, self.damage_amt)
        return total
