import pytest
from evercraft.models.character import Character
from evercraft.models.fighter import Fighter
from evercraft.models.rogue import Rogue
from evercraft.models.monk import Monk


### Iteration 2 - Classes

# > As a player I want to play a Fighter so that I can kick ass and take
#  names

def test_i_am_a_fight():
    assert Fighter()

# - attacks roll is increased by 1 for every level instead of every other level
def test_my_HP_gets_better():
    traits={
        "level":2,
        "XP": 1000
    }
    doofus = Fighter(traits)
    enemy = Fighter()
    assert doofus.attack(enemy, 9, doofus.str) == "Hit"

# - has 10 hit points per level instead of 5
def test_my_HP_gets_better():
    traits = {
        "XP":1001,
        "level":2,
    }
    doofus = Fighter(traits)
    assert doofus.HP == 15

## does is still work if you have above base con?
def test_my_HP_gets_better_with_better_con():
    traits = {
        "XP": 1001,
        "level": 2,
        "con": 14
    }
    loofus = Fighter(traits)
    assert loofus.HP == 19

def test_character():
    man = Character()
    assert man.HP == 5

def test_rogue_crits_triple():
    enemy = Character()
    moofus = Rogue()
    moofus.attack(enemy, 20, moofus.str)
    assert enemy.HP == 2

# ignores an opponents Dexterity modifier (if positive) to Armor Class when attacking
def test_rogue_ignores_armor():
    traits = {
        "dex":14
    }
    enemy = Character(traits)
    moofus = Rogue()
    assert moofus.attack(enemy, 11, moofus.str) == "Hit"
    
#This should not require any additional code, as the base attack method 
# includes the chosen modifier


#even if a rogue character is set to be good, they will be set to neutral instead
def test_bad_boy():
    traits = {
        "alignment":"good"
    }
    moofus = Rogue(traits)
    assert moofus.alignment == "neutral"


##making a monk
def test_i_can_be_a_monk():
    assert Monk()

# >Monk<

# - has 6 hit point per level instead of 5
def test_hp_increases_by_six():
    traits = {
        "level":2,
        "XP":1001
    }
    adrian = Monk(traits)
    assert adrian.HP==12

#even if their con is bad
def test_hp_w_bad_con():
    traits = {
        "con":1,
        "level":2,
        "XP":1001
    }
    adrian = Monk(traits)
    assert adrian.HP==12
#still working at even higher levels
def test_hp_w_high_level():
    traits = {
        "level":12,
        "XP":11001
    }
    adrian = Monk(traits)
    assert adrian.HP==72

# - does 3 points of damage instead of 1 when successfully attacking
def test_deal_more_dmg():
    adrian = Monk()
    enemy = Character()
    adrian.attack(enemy, 10, adrian.str)
    assert enemy.HP==2

# - adds Wisdom modifier (if positive) to Armor Class in addition to Dexterity

def test_wis_adds_to_AC():
    traits={
        "dex":14,
        "wis":14
        }
    adrian = Monk(traits)
    assert adrian.AC == 14

# - attack roll is increased by 1 every 2nd and 3rd level
##this is just fizzbuzz

#this should work based on the inherited code
def test_attack_increase_at_lvl_2():
    traits={
            "level":2,
            "XP":1001
            }
    adrian = Monk(traits)
    enemy = Character()
    assert adrian.attack(enemy, 9, adrian.str) == "Hit"

#this should increase again at level 3
def test_attack_increase_at_lvl_3():
    traits={
            "level":3,
            "XP":2001
            }
    adrian = Monk(traits)
    enemy = Character()
    assert adrian.attack(enemy, 8, adrian.str) == "Hit"

#at level 6, this should have increased 3x from evens, and 2x from 3s
def test_attack_increase_at_lvl_6():
    traits={
            "level":6,
            "XP":5001
            }
    adrian = Monk(traits)
    enemy = Character()
    assert adrian.attack(enemy, 5, adrian.str) == "Hit"