import pytest
from evercraft.models.character import Character
from evercraft.models.fighter import Fighter
from evercraft.models.rogue import Rogue


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