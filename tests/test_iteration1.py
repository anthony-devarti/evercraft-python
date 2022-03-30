import pytest
from evercraft.models.character import Character
# Feature: Create a Character
# get a name
# set a name

# make sure that a character instance can be made
# def test_makeCharacter():
#     assert Character()


# default test case for character class
def test_setCharacterName():
    ret_name = 'Evercraft'
    traits = {
        "name": "Evercraft",
        "alignment": 'good',
        "AC": 10,
        "HP": 12,
        "life": True,
        "str": 10,
        "dex": 10,
        "int": 10,
        "wis": 10,
        "cha": 10,
        "con": 10
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
        "HP": 12,
        "life": True,
        "str": 10,
        "dex": 10,
        "int": 10,
        "wis": 10,
        "cha": 10,
        "con": 10
    }
    c1 = Character(traits)
    assert c1.get_name() == ret_name

# make character alignment good


def test_makeCharacterAlignGood():
    align_value = 'good'
    traits = {
        "name": "Rufus",
        "alignment": 'good',
        "AC": 10,
        "HP": 12,
        "life": True,
        "str": 10,
        "dex": 10,
        "int": 10,
        "wis": 10,
        "cha": 10,
        "con": 10
    }
    c1 = Character(traits)
    assert c1.alignment == align_value

# checking for default values
# if an empty object is passed in, will the AC==10?
# this assumes that the object being passed in is empty, so we can check for
# a default value rather than manually passing one in at creation


def test_defaultAC():
    traits = {}
    c2 = Character(traits)
    assert c2.AC == 10


def test_default_hit_points():
    traits = {}
    c2 = Character(traits)
    assert c2.HP == 5


# def test_attack_roll20():

# Feature: Character Can Attack

# > As a combatant I want to be able to attack other combatants
#  so that I can survive to fight another day

# - roll a 20 sided die (don't code the die)
# - roll must meet or beat opponent's armor class to hit
# - a natural roll of 20 always hits

# test for a crit success regardless of enemy AC
def test_hit_on_20():
    traits = {}
    enemy = Character(traits)
    assert Character.attack(enemy, 20, Character.str) == "Hit"

# test for a miss with a roll lower than the enemy AC


def test_guess_i_never_miss_huh():
    traits = {}
    enemy = Character(traits)
    assert Character.attack(enemy, 9, 10) == "Whiff"

# test for a hit with a result greater than enemy AC


def test_i_slapped_will_smith():
    traits = {}
    enemy = Character(traits)
    assert Character.attack(enemy, 10, 10) == "Hit"

# test for a hit with a roll greater than enemy ACdef test_i_slapped_will_smith_harder():

    traits = {}
    enemy = Character(traits)
    assert Character.attack(enemy, 14, 10) == "Hit"


# #### Feature: Character Can Be Damaged

# > As an attacker I want to be able to damage my enemies so that they will die and I will live

# - If attack is successful, other character takes 1 point of damage when hit
# this should have the enemy take one damage on a hit that isn't a crit
def test_i_can_deal_damage():
    traits = {}
    enemy = Character(traits)
    Character.attack(enemy, 19)
    assert enemy.HP == 4
# - If a roll is a natural 20 then a critical hit is dealt and the damage is doubled


def test_i_critically_deal_damage():
    traits = {}
    enemy = Character(traits)
    Character.attack(enemy, 20)
    assert enemy.HP == 3

# - when hit points are 0 or fewer, the character is dead


def test_i_can_murder():
    traits = {
        "name": "Rufus",
        "alignment": 'good',
        "AC": 12,
        'HP': 1,
        "life": True,
        "str": 10,
        "dex": 10,
        "int": 10,
        "wis": 10,
        "cha": 10,
        "con": 10
    }
    whipporwill = Character(traits)
    Character.attack(whipporwill, 19)
    assert whipporwill.HP == 0


def test_i_can_murder_better():
    traits = {
        "name": "Hooper",
        "alignment": 'evil',
        "AC": 12,
        'HP': 1,
        "life": True,
        "str": 10,
        "dex": 10,
        "int": 10,
        "wis": 10,
        "cha": 10,
        "con": 10
    }
    whipporwill = Character(traits)
    Character.attack(whipporwill, 20)
    assert whipporwill.life == False

# #### Feature: Character Has Abilities Scores
# > As a character I want to have several abilities so that I am not
#  identical to other characters except in name
# - Abilities are Strength, Dexterity, Constitution, Wisdom,
# Intelligence, Charisma
# - Abilities range from 1 to 20 and default to 10


def test_i_have_special_abilities_like_no_one_else():
    traits = {
        "name": "Hooper",
        "alignment": 'evil',
        "AC": 12,
        'HP': 1,
        "life": True,
        "str": 10,
        "dex": 10,
        "int": 10,
        "wis": 10,
        "cha": 10,
        "con": 10
    }
    hooper = Character(traits)
    assert True == True


# # - Abilities have modifiers according to the following table
# |   Score   | Modifier |   Score   | Modifier |   Score   | Modifier |   Score   | Modifier |
# |:---------:|:--------:|:---------:|:--------:|:---------:|:--------:|:---------:|:--------:|
# |   __1__   |    -5    |   __6__   |    -2    |  __11__   |     0    |  __16__   |    +3    |
# |   __2__   |    -4    |   __7__   |    -2    |  __12__   |    +1    |  __17__   |    +3    |
# |   __3__   |    -4    |   __8__   |    -1    |  __13__   |    +1    |  __18__   |    +4    |
# |   __4__   |    -3    |   __9__   |    -1    |  __14__   |    +2    |  __19__   |    +4    |
# |   __5__   |    -3    |  __10__   |     0    |  __15__   |    +2    |  __20__   |    +5    |

##create a modify method that takes in the score and returns the correct modifier
def test_modifier_from_20():
    assert Character.modify(20) == 5

def test_modifier_from_19():
    assert Character.modify(19) == 4

def test_modifier_from_18():
    assert Character.modify(18) == 4

def test_modifier_from_17():
    assert Character.modify(17) == 3

def test_modifier_from_16():
    assert Character.modify(16) == 3

def test_modifier_from_15():
    assert Character.modify(15) == 2

def test_modifier_from_14():
    assert Character.modify(14) == 2

def test_modifier_from_12():
    assert Character.modify(12) == 1

def test_modifier_from_11():
    assert Character.modify(11) == 0

def test_modifier_from_10():
    assert Character.modify(10) == 0

def test_modifier_from_9():
    assert Character.modify(9) == -1

def test_modifier_from_4():
    assert Character.modify(4) == -3

#### Feature: Character Ability Modifiers Modify Attributes

## > As a character I want to apply my ability modifiers improve my capabilities in combat so that I can vanquish my enemy with extreme prejudice

# - add Strength modifier to attack roll 
def test_i_have_strength():  
    traits={
    "name": "Rufus",
    "alignment": 'good',
    "AC": 12,
    'HP': 8,
    "life": True,
    "str" : 12,
    "dex" : 10,
    "int" : 10,
    "wis" : 10,
    "cha" : 10,
    "con" : 10
    }
    c1=Character(traits)
    bad_traits = {
        "name": "Evil Rufus",
        "alignment": 'evil',
        "AC": 10,
        'HP': 5,
        "life": True,
        "str" : 12,
        "dex" : 10,
        "int" : 10,
        "wis" : 10,
        "cha" : 10,
        "con" : 10
    }
    bad = Character(bad_traits)
    c1.attack(bad, 9, c1.str)
    assert bad.HP == 4
    
# - add strength mod to damage dealt

def test_add_str_to_damage():
    traits = {
    "name": "Rufus",
    "alignment": 'good',
    "AC": 12,
    'HP': 8,
    "life": True,
    "str" : 12,
    "dex" : 10,
    "int" : 10,
    "wis" : 10,
    "cha" : 10,
    "con" : 10
    }
    c1=Character(traits)
    bad_traits = {
        "name": "Evil Rufus",
        "alignment": 'evil',
        "AC": 10,
        'HP': 5,
        "life": True,
        "str" : 12,
        "dex" : 10,
        "int" : 10,
        "wis" : 10,
        "cha" : 10,
        "con" : 10
    }
    bad = Character(bad_traits)
    c1.attack(bad, 9, c1.str)
    assert bad.HP == 3

# - double Strength modifier on critical hits

def test_double_damage_on_crit():
    traits = {
    "name": "Rufus",
    "alignment": 'good',
    "AC": 12,
    'HP': 8,
    "life": True,
    "str" : 12,
    "dex" : 10,
    "int" : 10,
    "wis" : 10,
    "cha" : 10,
    "con" : 10
    }
    c1=Character(traits)
    bad_traits = {
        "name": "Evil Rufus",
        "alignment": 'evil',
        "AC": 10,
        'HP': 5,
        "life": True,
        "str" : 12,
        "dex" : 10,
        "int" : 10,
        "wis" : 10,
        "cha" : 10,
        "con" : 10
    }
    bad = Character(bad_traits)
    c1.attack(bad, 20, c1.str)
    assert bad.HP == 1

# - minimum damage is always 1 
# When a weak character attacks, their damage mod can deal negative damage
# we want to change that when attacks are dealt, they will deal at least 1
# start with non-20 die results
def test_weak_char_hits():
    traits = {
    "name": "Brutus",
    "alignment": 'good',
    "AC": 12,
    'HP': 8,
    "life": True,
    "str" : 1,
    "dex" : 10,
    "int" : 10,
    "wis" : 10,
    "cha" : 10,
    "con" : 10
    }
    brutus = Character(traits)
    bad = Character()
    brutus.attack(bad, 15, brutus.str)
    assert bad.HP == 4

# (even on a critical hit)
def test_weak_char_hit_on_crit():
    traits = {
    "name": "Brutus",
    "alignment": 'good',
    "AC": 12,
    'HP': 8,
    "life": True,
    "str" : 1,
    "dex" : 14,
    "int" : 10,
    "wis" : 10,
    "cha" : 10,
    "con" : 10
    }
    brutus = Character(traits)
    bad = Character()
    brutus.attack(bad, 20, brutus.str)
    assert bad.HP == 3

# - add Dexterity modifier to armor class

def test_dex_affects_ac():
    traits = {
    "name": "Brutus",
    "alignment": 'good',
    "AC": 12,
    'HP': 8,
    "life": True,
    "str" : 1,
    "dex" : 14,
    "int" : 10,
    "wis" : 10,
    "cha" : 10,
    "con" : 10
    }
    brutus = Character(traits)
    assert brutus.AC == 14

# - add Constitution modifier to hit points
def test_con_affects_hp():
    traits = {
    "name": "Brutus",
    "alignment": 'good',
    "AC": 12,
    'HP': 5,
    "life": True,
    "str" : 1,
    "dex" : 14,
    "int" : 10,
    "wis" : 10,
    "cha" : 10,
    "con" : 14
    }
    brutus = Character(traits)
    assert brutus.HP == 7

# even if the con is really low, char hp will never be negative
def test_bad_con_affects_hp():
    traits = {
    "name": "Brutus",
    "alignment": 'good',
    "AC": 12,
    'HP': 4,
    "life": True,
    "str" : 1,
    "dex" : 14,
    "int" : 10,
    "wis" : 10,
    "cha" : 10,
    "con" : 1
    }
    brutus = Character(traits)
    assert brutus.HP == 1