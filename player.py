from random import randint
from weapon import Weapon

class Player:

    def __init__(self, pname="Player Name", strgth="10", cel="10", health="10", cha="10", wis="10", aff="10", hp="8"):
        self.name = pname
        self.strength = strgth
        self.celerity = cel
        self.health = health
        self.charisma = cha
        self.wisdom = wis
        self.affinity = aff
        self.hitpoints = self.__calculate_hitpoints__(hp, health)
        self.max_hitpoints = self.__calculate_hitpoints__(hp, health)
        self.armored_defense = 10 + int(cel)
        self.weapon = Weapon("Greatsword", 2, 10)

    def __str__(self):
        output = "Player Name: " + self.name + ", Hit Points: " + str(self.hitpoints) + "\n"
        output = output + "Strength: " + self.strength + ", Celerity: " + self.celerity + ", Health: " + self.health + "\n"
        output = output + "Charisma: " + self.charisma + ", Wisdom: " + self.wisdom + ", Affinity: " + self.affinity + "\n"
        return output

    def __calculate_hitpoints__(self, baseHp, health):
        return int(baseHp) + int((int(health) - 10) / 2)

    def attack(self, weapon, target):
        attack_roll = randint(1,20) + (int(self.strength) - 10) / 2
        if attack_roll >= target.armored_defense:
            target.hitpoints -= weapon.roll_damage()