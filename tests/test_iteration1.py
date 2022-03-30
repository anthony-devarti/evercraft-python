import pytest
from evercraft.models.character import Character
#### Feature: Create a Character
#get a name
#set a name

#make sure that a character instance can be made
# def test_makeCharacter():
#     assert Character()


# default test case for character class
def test_setCharacterName():
    ret_name = 'Evercraft'
    traits = {
    "name": "Evercraft",
    "alignment": 'good',
    "AC": 10,
    "HP": 12
    }
    c1 = Character(traits)
    assert c1.name == ret_name 

# test case for character name
def test_getCharacterName():
    ret_name = "Rufus"
    traits = {
    "name": "Rufus",
    "alignment": 'good',
    "AC": 10,
    "HP": 12
    }
    c1 = Character(traits)
    assert c1.get_name()==ret_name

# make character alignment good
def test_makeCharacterAlignGood():
    align_value = 'good'
    traits = {
    "name": "Rufus",
    "alignment": 'good',
    "AC": 10,
    "HP": 12
    }
    c1 = Character(traits)
    assert c1.alignment == align_value

# checking for default values
#if an empty object is passed in, will the AC==10?
# this assumes that the object being passed in is empty, so we can check for
# a default value rather than manually passing one in at creation
def test_defaultAC():
    traits= { }
    c2 = Character(traits)
    assert c2.AC==10

def test_default_hit_points():
    traits = {}
    c2 = Character(traits)
    assert c2.HP == 5


# def test_attack_roll20():

#### Feature: Character Can Attack

# > As a combatant I want to be able to attack other combatants
#  so that I can survive to fight another day

# - roll a 20 sided die (don't code the die)
# - roll must meet or beat opponent's armor class to hit
# - a natural roll of 20 always hits

# test for a crit success regardless of enemy AC
def test_create_enemy():
    traits = {}
    enemy = Character(traits)
    assert Character.attack(enemy, 20) == "Hit"

#test for a miss with a roll lower than the enemy AC
def test_guess_i_never_miss_huh():
    traits={}
    enemy = Character(traits)
    assert Character.attack(enemy, 9) == "Whiff"

#test for a hit with a result greater than enemy AC
def test_i_slapped_will_smith():
    traits={}
    enemy= Character(traits)
    assert Character.attack(enemy, 10) == "Hit"

#test for a hit with a roll greater than enemy AC
def test_i_slapped_will_smith_harder():
    traits={}
    enemy= Character(traits)
    assert Character.attack(enemy, 14) == "Hit"


# #### Feature: Character Can Be Damaged

# > As an attacker I want to be able to damage my enemies so that they will die and I will live

# - If attack is successful, other character takes 1 point of damage when hit
# this should have the enemy take one damage on a hit that isn't a crit
def test_i_can_deal_damage():
    traits={}
    enemy = Character(traits)
    Character.attack(enemy, 19)
    assert enemy.HP == 4
# - If a roll is a natural 20 then a critical hit is dealt and the damage is doubled

# - when hit points are 0 or fewer, the character is dead





# #### Feature: Character Has Abilities Scores

# > As a character I want to have several abilities so that I am not identical to other characters except in name

# - Abilities are Strength, Dexterity, Constitution, Wisdom, Intelligence, Charisma
# - Abilities range from 1 to 20 and default to 10
# - Abilities have modifiers according to the following table

