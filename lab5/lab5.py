import random
from functions_lab05_starter import hero_attacks, monster_attacks

# Lab 05 - Game
# Student Name|Number: Aaron Balayo [101575606]
# 2026-02-08

#----------------------------------------
#game setup
#-----------------------------------------

player_name = "Drifter"
health_points = 35              # starting player health
combat_strength = random.randint(9, 14)   # player's attack power

monster_name = "Hobgoblin"
m_health_points = 28            # starting monster health
m_combat_strength = random.randint(7, 11) # monster's attack power

print("========================================")
print(f"  Welcome, brave regressor {player_name}!")
print(f"  HEY! {monster_name} appears!")
print("========================================")
print()

#show stats
print(f"You    : HP {health_points}  |  Strength {combat_strength}")
print(f"{monster_name}: HP {m_health_points}  |  Strength {m_combat_strength}")
print("-" * 40)
print()

#-----------------------------------------
#combat loop
#----------------------------------------

while health_points > 0 and m_health_points > 0:
    #Player attacking first
    print("Ey, your turn.")
    m_health_points = hero_attacks(combat_strength, m_health_points)
    print()

    if m_health_points <= 0:
        print("========================================")
        print(f"Good work, you killed {monster_name}!")
        print("========================================")
        break

    #Monster attacking if still alive
    print("MONSTER'S TURN!!!!")
    health_points = monster_attacks(m_combat_strength, health_points)
    print()

    if health_points <= 0:
        print("========================================")
        print(f"You got killed by {monster_name}")
        print("          lol noob")
        print("========================================")
        break

    # Quick status update between rounds
    print(f"Your HP: {health_points} | {monster_name} HP: {m_health_points}")
    print("-" * 40)
    print()

#ending thing
if health_points > 0:
    print("Good thing you lived, if you died those villagers and the world would die or something y'know?")
else:
    print("*Dark Souls 2 theme plays*...")