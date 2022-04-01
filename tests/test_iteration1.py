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
    rufus = Character()
    assert rufus.attack(enemy, 20, rufus.str) == "Crit"

# test for a miss with a roll lower than the enemy AC


def test_guess_i_never_miss_huh():
    enemy = Character()
    rufus = Character()
    assert rufus.attack(enemy, 9, 10) == "Whiff"

# test for a hit with a result greater than enemy AC


def test_i_slapped_will_smith():
    enemy = Character()
    rufus = Character()
    assert rufus.attack(enemy, 10, 10) == "Hit"

# test for a hit with a roll greater than enemy AC
def test_i_slapped_will_smith_harder():
    traits = {}
    enemy = Character(traits)
    rufus = Character()
    assert rufus.attack(enemy, 14, 10) == "Hit"


# #### Feature: Character Can Be Damaged

# > As an attacker I want to be able to damage my enemies so that they will die and I will live

# - If attack is successful, other character takes 1 point of damage when hit
# this should have the enemy take one damage on a hit that isn't a crit
def test_i_can_deal_damage():
    enemy = Character()
    rufus = Character()
    rufus.attack(enemy, 19, 10)
    assert enemy.HP == 4
# - If a roll is a natural 20 then a critical hit is dealt and the damage is doubled


def test_i_critically_deal_damage():
    traits = {}
    enemy = Character(traits)
    rufus= Character()
    rufus.attack(enemy, 20,10)
    assert enemy.HP == 3

# - when hit points are 0 or fewer, the character is dead


def test_i_can_murder():
    traits = {
        "name": "bird",
        "alignment": 'good',
        "AC": 12,
        'HP': 1,
        "life": True,
        "str": 10,
        "dex": 10,
        "int": 10,
        "wis": 10,
        "cha": 10,
        "con": 10,
        "base_hp":4
    }
    whipporwill = Character(traits)
    whipporwill.HP = 1
    rufus = Character()
    rufus.attack(whipporwill, 19, 10)
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
    rufus=Character()
    whipporwill.HP=1
    rufus.attack(whipporwill, 20,10)
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
    rufus = Character()
    assert rufus.modify(20) == 5

def test_modifier_from_19():
    rufus = Character()
    assert rufus.modify(19) == 4

def test_modifier_from_18():
    rufus = Character()
    assert rufus.modify(18) == 4

def test_modifier_from_17():
    rufus = Character()
    assert rufus.modify(17) == 3

def test_modifier_from_16():
    rufus = Character()
    assert rufus.modify(16) == 3

def test_modifier_from_15():
    rufus = Character()
    assert rufus.modify(15) == 2

def test_modifier_from_14():
    rufus = Character()
    assert rufus.modify(14) == 2

def test_modifier_from_12():
    rufus = Character()
    assert rufus.modify(12) == 1

def test_modifier_from_11():
    rufus = Character()
    assert rufus.modify(11) == 0

def test_modifier_from_10():
    rufus = Character()
    assert rufus.modify(10) == 0

def test_modifier_from_9():
    rufus = Character()
    assert rufus.modify(9) == -1

def test_modifier_from_4():
    rufus = Character()
    assert rufus.modify(4) == -3

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
    rufus=Character(traits)
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
    rufus.attack(bad, 9, rufus.str)
    assert bad.HP == 3
    
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
    "con" : 1,
    "XP" : 0
    }
    brutus = Character(traits)
    assert brutus.HP == 1

    # - When a successful attack occurs, the character 
# gains 10 experience points
def test_i_won_the_battle():
    traits = {
    "name": "Brutus",
    "alignment": 'good',
    "AC": 10,
    'HP': 1,
    "life": True,
    "str" : 10,
    "dex" : 14,
    "int" : 10,
    "wis" : 10,
    "cha" : 10,
    "con" : 1,
    "XP" : 0
    }
    brutus = Character(traits)
    oldXP=Character.XP
    enemy = Character()
    brutus.attack(enemy, 11, brutus.str)
    assert brutus.XP == oldXP+10

    #### Feature: A Character Can Level

# > As a character I want my experience points to increase my level and combat capabilities so that I can bring vengeance to my foes

# - Level defaults to 1
#this is the default level.  Every character made should start at 1, regardless of anything else
def test_level_defaults_to_one():
    doofus = Character()
    assert doofus.level == 1

## double back and check that our loop to assign traits is working as expected
def test_incomplete_trait_assignment():
    bad_traits={
        "name": "doofus"
    }
    doofus = Character(bad_traits)
# - After 1000 experience points, the character gains a level
#     - 0 xp -> 1st Level
#     - 1000 xp -> 2nd Level
## This is where we should write a test that makes a character level up whenever they reach 1000XP
def test_i_can_level_up():
    traits = {
        "XP":990,
        "level":1 
    }
    doofus = Character(traits)
    baddie = Character()
    doofus.attack(baddie, 20, doofus.str)
    assert doofus.level == 2
##Character is at correct level when they are created with starting XP
#     - 2000 xp -> 3rd Level
## We're probably modifying the first method to make it level the character up every 1000XP
def test_i_started_out_better():
    traits = {
        "XP":8000
    }
    doofus = Character(traits)
    assert doofus.level == 9





# - For each level:
#     - hit points increase by 5 plus Con modifier
## once again, modifying the level up method to make it make appropriate changes whenever the character goes up a Level to their CON stat
def test_my_HP_gets_better():
    traits = {
        "XP":1001,
        "level":2,
        "con":12
    }
    doofus = Character(traits)
    assert doofus.HP == 12



#     - 1 is added to attack roll for every even level achieved
##this will likely break previous attack tests that check to make sure that the damage is calculating right
## something that divides the level by 2 and rounds down then adds that much to their attack modifier.
## this will probably alter the attack method.
def test_my_damage_increases_w_level():
    traits = {
        "level": 2,
        "XP":1010
    }
    rufus = Character(traits)
    enemy = Character()
    assert rufus.attack(enemy, 9, rufus.str) == "Hit"
    
