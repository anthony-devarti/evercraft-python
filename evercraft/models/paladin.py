from evercraft.models.character import Character
import math

class Paladin(Character):
    base_hp = 8
    DEFAULT: {
        "name": "Evercraft",
        "alignment": "neutral",
        "AC": 10,
        "HP": 8,
        "life": True,
        "str": 10,
        "dex": 10,
        "int": 10,
        "wis": 10,
        "cha": 10,
        "con": 10,
        "XP": 0,
        "level": 1,
        "base_hp":8
    }
    def __init__(self, obj={}):
        for key in obj:
            if key in obj:
                setattr(self, key, obj[key])
            else:
                setattr(self, key, DEFAULT[key])
        self.AC = self.set_AC(self.dex)
        self.HP = self.set_HP(self.con)
        self.check_XP(self.XP)
        if self.alignment!="good":
            print("Yeah, right, Mary-Sue.  I'm going ahead and setting you to Good")
            self.alignment="good"

    def attack(self, target, roll, score):
        #creates a mod for the attack roll
        paladin_atk_mod = 2 if target.alignment == "evil" else 0
        mod = self.modify(score) + paladin_atk_mod
        #this controls for 2 bonus dmg before multipliers if the defender is evil
        damage = 3 if target.alignment == "evil" else 1
        #a second modifier based on the level 1:1 because it's a paladin
        mod_level = self.level
        if roll == 20:
            #add XP, then check for a level up
            self.XP = self.XP + 10
            self.check_XP(self.XP)
            if damage < 1:
                damage = 1
            #reduce the target's HP based on the damage output
            target.HP = target.HP - (damage*3 if target.alignment=="evil" else 2)
            #check if their HP was reduced to 0, and switch their life boolean to false if they are.
            if target.HP <= 0:
                target.life = False
            return 'Hit'
        elif roll + mod + mod_level >= target.AC:
            self.XP = self.XP + 10
            self.check_XP(self.XP)
            if damage < 1:
                damage = 1
            target.HP = target.HP - damage
            if target.HP <= 0:
                target.life = False
            return "Hit"
        elif roll + mod + mod_level < target.AC:
            return "Whiff"
        else:
            return "That doesn't seem to be a number"
        self.check_XP(self.XP)
        
    # add 8 hp per level instead of 5
    def set_HP(self, score):
        print('character set hp')
        return self.base_hp*self.level + self.modify(self.con)*self.level

#end of class
marysue = Paladin()
