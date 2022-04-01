# this is where your character code will go
import math


class Character:
    name = "Evercraft",
    alignment = "neutral",
    AC = 10
    base_hp = 5
    HP = 5
    life = True
    str = 10
    dex = 10
    int = 10
    wis = 10
    cha = 10
    con = 10
    XP = 0
    level = 1
    race = "human"
    # object that stores the default values for a new character
    DEFAULT: {
        "name": "Evercraft",
        "alignment": "neutral",
        "race": "human",
        "AC": 10,
        "HP": 5,
        "life": True,
        "str": 10,
        "dex": 10,
        "int": 10,
        "wis": 10,
        "cha": 10,
        "con": 10,
        "XP": 0,
        "level": 1,
        "base_hp": 5
    }

    def __init__(self, obj={}):
        # for each key in the obj
        for key in obj:
            # if there is an appropriate key
            if key in obj:
                # set the attribute to the one in the key that was established
                setattr(self, key, obj[key])
            # otherwise
            else:
                # set them to the values in the default object.
                setattr(self, key, self.DEFAULT[key])
        # set the armor class using the set_AC method.  Do the same for the set HP method
        self.AC = self.set_AC(self.dex)
        self.HP = self.set_HP(self.con)
        self.check_XP(self.XP)
    # this isn't strictly necessary, since you can set the value without it.

    def set_name(self, name):
        self.name = name
    # same for this

    def get_name(self):
        return self.name
    # attack method
    # this handles attacks, damage, xp on sucessful attack, checking for level up

    def attack(self, target, roll, score):

        # check this because it's probably no good
        racial_bonus = 0
        racial_armor = 0
        AC_buff = 0
        if self.race == "dwarf" and target.race == "orc":
            racial_bonus = 2
            print("bonus")
        elif self.race == "elf" and roll == 19:
            roll = roll+1
        elif self.race == "orc" and target.race == "elf":
            # add a temporary buff
            AC_buff = 2
        elif self.race !="halfling" and target.race == "halfling":
            AC_buff=2
        else:
            print("no bonus")
            racial_bonus = 0

        # creates a mod for the attack roll
        mod = self.modify(score)
        # base damage and the modifier established earlier
        damage = 1 + mod + racial_bonus
        # a second modifier based on the level
        mod_level = (math.floor(self.level/2))
        # roll result totals everything that can modify the roll
        roll_result = roll + mod + mod_level + racial_bonus
        # check for a crit first
        if roll == 20:
            # add XP, then check for a level up
            self.XP = self.XP + 10
            self.check_XP(self.XP)
            # if, for any reason, the damage output is less than one, make it one instead
            if damage < 1:
                damage = 1
            # reduce the target's HP based on the damage output
            target.HP = target.HP - (damage*2)
            # check if their HP was reduced to 0, and switch their life boolean to false if they are.
            if target.HP <= 0:
                target.life = False
            return 'Crit'
        elif roll_result >= target.AC+AC_buff:
            self.XP = self.XP + 10
            self.check_XP(self.XP)
            if damage < 1:
                damage = 1
            target.HP = target.HP - damage
            if target.HP <= 0:
                target.life = False
            return "Hit"
        elif roll_result < target.AC+AC_buff:
            return "Whiff"
        else:
            return "That doesn't seem to be a number"

    def modify(self, score):
        switcher = {
            20: 5,
            19: 4,
            18: 4,
            17: 3,
            16: 3,
            15: 2,
            14: 2,
            13: 1,
            12: 1,
            11: 0,
            10: 0,
            9: -1,
            8: -1,
            7: -2,
            6: -2,
            5: -3,
            4: -3,
            3: -4,
            2: -4,
            1: -5
        }
        return switcher.get(score)

    # We want to call these when a character is created, at level up, and equipment(stretch)
    # they also will probably want to be merged into a unified function later
    def set_AC(self, score):
        return max(1, self.AC + self.modify(score))

    def set_HP(self, score):
        print('character set hp')
        # this should take care of the dwarf setup.
        if self.race == "dwarf":
            return max(1, self.base_hp * self.level + self.modify(score)*self.level*2)
        else:
            return max(1, self.base_hp * self.level + self.modify(score)*self.level)

    def racial_bonus(self, target):
        if target.race == "orc" and self.race == "dwarf":
            return 2
        else:
            return 0
    # this function probably should be called whenever a xp changes
    # this will include setAC and setHP so they will update when the lev

    def check_XP(self, XP):
        # taking a snapshot of the current level
        current_level = self.level
        self.level = (math.floor(self.XP/1000))+1
        # checking for changes, and only running these if the level has changed
        if self.level != current_level:
            self.set_AC(self.dex)
            self.set_HP(self.con)

    #RACES#
    def is_orc(self):
        self.race = "orc"
        self.str = self.str+2
        self.int = self.int-1
        self.wis = self.wis-1
        self.cha = self.cha-1
        self.AC = self.AC+2

    def is_elf(self):
        self.race = "elf"
        self.dex = self.dex+1
        self.con = self.con-1

    # this only will affect the HP at character creation.
    # This will need to apply another way at level up
    def is_dwarf(self):
        self.race = "dwarf"
        self.con = self.con+1
        self.cha = self.cha-1
        self.HP = max(self.HP, self.HP+self.modify(self.con)*2)
        # is it possible to change the roll result from this function under certain circumstances?

    def is_halfling(self):
        self.race= "halfling"
        self.dex = self.dex+1
        self.str = self.str-1
        if self.alignment=="evil":
            print("You are too smol to be evil.  Let's go with neutral")
            self.alignment="neutral"


##############
#End of Class#
##############
# some non-default traits to work with
example_traits = {
    "name": "Rufus",
    "alignment": 'good',
    "AC": 12,
    'HP': 8,
    "life": True,
    "str": 12,
    "dex": 14,
    "int": 10,
    "wis": 10,
    "cha": 10,
    "con": 14,
    "XP": 0,
    "level": 1
}
Rufus = Character(example_traits)
c2 = Character()
bad_guy = {
    "name": "Evil Rufus",
    "alignment": 'evil',
    "AC": 12,
    'HP': 8,
    "life": True,
    "str": 10,
    "dex": 10,
    "int": 10,
    "wis": 10,
    "cha": 10,
    "con": 10,
    "XP": 0
}
bad_guy = Character(bad_guy)
print(Rufus.level)
Rufus.attack(bad_guy, 20, Rufus.str)
print(Rufus.level)
# default character
# print(c1.AC)
