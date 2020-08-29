from random import randint
from weapon import Weapon

class Enemy:

    def __init__(self):
        self.name = "Goblin"
        self.strength = "8"
        self.celerity = "12"
        self.health = "10"
        self.charisma = "8"
        self.wisdom = "8"
        self.affinity = "10"
        self.hitpoints = 6
        self.max_hitpoints = 6
        self.armored_defense = 11
        self.weapon = Weapon()

    def __str__(self):
        output = "Enemy Name: " + self.name + ", Hit Points: " + str(self.hitpoints) + "\n"
        output = output + "Strength: " + self.strength + ", Celerity: " + self.celerity + ", Health: " + self.health + "\n"
        output = output + "Charisma: " + self.charisma + ", Wisdom: " + self.wisdom + ", Affinity: " + self.affinity + "\n"
        return output

    def attack(self, weapon, target):
        attack_roll = randint(1,20) + int((int(self.celerity) - 10) / 2)
        if attack_roll >= target.armored_defense:
            target.hitpoints -= weapon.roll_damage()