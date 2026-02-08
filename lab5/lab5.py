import random
from functions_lab05_starter import hero_attacks, monster_attacks

# Lab 05 - Game
# Student Name|Number: Aaron Balayo [101575606]
# 2026-02-08

#----------------------------------------
#functions
#-----------------------------------------

def collect_loot(belt, loot_options):
    """Collect two random loot items"""
    for _ in range(2):
        if loot_options:
            loot_index = random.randint(0, len(loot_options) - 1)
            item = loot_options.pop(loot_index)
            belt.append(item)
    belt.sort()
    print("Your belt:", belt)
    return [belt, loot_options]


def use_loot(belt, health_points):
    """Use the first item in belt (if any)"""
    if belt:
        item = belt.pop(0)
        print(f"You quickly use: {item}")
        if item in ["Health Potion", "Leather Boots"]:
            health_points = min(20, health_points + 2)  # reasonable cap
            print(f"Health increased → {health_points}")
        elif item == "Poison Potion":
            health_points = max(0, health_points - 2)
            print(f"Poison! Health decreased → {health_points}")
        else:
            print("It had no effect...")
    else:
        print("No items to use.")
    return [belt, health_points]


def inception_dream(depth=0):
    """Recursive dream layers - base returns 2, recursive adds 1"""
    if depth >= 4 or random.random() < 0.4:  # prevent too deep
        return 2
    return 1 + inception_dream(depth + 1)


#--------------Main Game------------#

#Get hero name (two words)
while True:
    name_input = input("Enter your Hero's name (two words): ").strip()
    parts = name_input.split()
    if len(parts) != 2:
        print("Please enter exactly TWO words.")
        continue
    first, second = parts
    if not (first.isalpha() and second.isalpha()):
        print("Names must contain only letters.")
        continue
    hero_name = name_input
    short_name = first[:2] + second[0]  # e.g. "Strong John" → "StJ"
    break

#Game setup
combat_strength = int(input("Enter your combat strength (1-6): "))
m_combat_strength = int(input("Enter monster's combat strength (1-6): "))

combat_strength = max(1, min(6, combat_strength))
m_combat_strength = max(1, min(6, m_combat_strength))

weapon_roll = random.randint(1, 6)
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
combat_strength = min(6, combat_strength + weapon_roll)
print(f"Your weapon: {weapons[weapon_roll - 1]}")

health_points = random.randint(1, 20)
m_health_points = random.randint(1, 20)

loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Boots of Speed", "Ring of Aquila"]
belt = []

print("\n=== Encounter ===")
print(f"{hero_name} (HP:{health_points}, Str:{combat_strength})")
print(f"Hobgoblin (HP:{m_health_points}, Str:{m_combat_strength})")
print()

print("You find a loot bag! Two items:")
belt, loot_options = collect_loot(belt, loot_options)

print("\nYou use one item before the fight:")
belt, health_points = use_loot(belt, health_points)

#Dice roll
Diceroll = random.randint(1, 6)
print(f"\nDiceroll roll: {Diceroll}")
hero_first = Diceroll in [1, 3, 5]
print("You attack first!" if hero_first else "Monster attacks first!")

#Combat
print("\nFight!")
while health_points > 0 and m_health_points > 0:
    if hero_first:
        m_health_points = hero_attacks(combat_strength, m_health_points)
        if m_health_points <= 0:
            break
        health_points = monster_attacks(m_combat_strength, health_points)
    else:
        health_points = monster_attacks(m_combat_strength, health_points)
        if health_points <= 0:
            break
        m_health_points = hero_attacks(combat_strength, m_health_points)

    # alternate turns after first round
    hero_first = not hero_first  # toggle after first full exchange

#Ending
if health_points > 0:
    print(f"\nVictory! {hero_name} defeated the Hobgoblin!")

    # req 2: use short_name
    stars = "***"  # or calculate based on your logic
    print(f"Hero {short_name} gets <{stars}> stars")

    # req 6: inception dream
    print("\nReality starts to bend...")
    crazy_level = inception_dream()
    print(f"Abyssal: {crazy_level}")
    health_points -= 1
    combat_strength += crazy_level
    print(f"After the Abyss → HP: {health_points}, Strength: {combat_strength}")

    print("You lived, if you died somehow then those villagers or the world would've died or something")
else:
    print(f"\ndead...noob")

print("mortis")