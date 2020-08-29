from player import Player
from enemy import Enemy
from random import *

def main():
    isActive = True
    player_characters = []
    enemies = []

    print("Welcome to the Battle Simulator.\n")
    while(isActive):
        print("\nMain Menu\n")
        print("Press 1 to manually create character.\n")
        print("Press 2 to automatically generate character.\n")
        print("Press 3 to input enemy stats.\n")
        print("Press 4 to start a combat.\n")
        print("Press 5 to output all player characters.\n")
        print("Press 6 to output all enemy characters.\n")

        decision = input("Please choose what you would like to do from the above actions. Press 0 to quit. ")

        if decision == "0":
            isActive = False
        elif decision == "1":
            player_characters.append(get_player_stats())
        elif decision == "2":
            player_characters.append(roll_character())
        elif decision == "3":
            enemies.append(Enemy())
        elif decision == "4":
            if len(player_characters) <=0 and len(enemies) <=0:
                print("Cannot Start Combat. A Player and An Enemy must be created.")
                continue
            combat(player_characters[0], enemies[0])
        elif decision == "5":
            for character in player_characters:
                print(character)
                print("\n")
        elif decision == "6":
            for enemy in enemies:
                print(enemy)
                print("\n")

def get_player_stats():
    print("\nManual Player Creation")
    player_name = input("\nWhat is the player's name? ")
    strength = input("\nWhat is the player's Strength stat? ")
    celerity = input("\nWhat is the player's Celerity stat? ")
    health = input("\nWhat is the player's Health stat? ")
    charisma = input("\nWhat is the player's Charisma stat? ")
    wisdom = input("\nWhat is the player's Wisdom stat? ")
    affinity = input("\nWhat is the player's Affinity stat? ")
    hit_points = input("\nWhat is the player's base Hit Points? ")
    return Player(player_name, strength, celerity, health, charisma, wisdom, affinity, hit_points)

def roll_character():
    print("\nAutomatic Player Creation")
    player_name = input("\nWhat is the player's name? ")
    hit_points = input("\nWhat is the player's base Hit Points? ")
    strength = roll(6,3)
    celerity = roll(6,3)
    health = roll(6,3)
    charisma = roll(6,3)
    wisdom = roll(6,3)
    affinity = roll(6,3)
    return Player(player_name, strength, celerity, health, charisma, wisdom, affinity, hit_points)

def roll(dice_type, dice_number):
    total = 0
    for x in range(dice_number):
        total += int(randint(1, dice_type))
    return str(total)

def combat(player, enemy):
    player.hitpoints = player.max_hitpoints
    enemy.hitpoints = player.max_hitpoints
    while(player.hitpoints > 0 and enemy.hitpoints > 0):
        player.attack(player.weapon, enemy)
        if enemy.hitpoints <= 0:
            print("Enemy defeated!")
            continue

        enemy.attack(enemy.weapon, player)
        if player.hitpoints <= 0:
            print("Player defeated!")
            continue

main()