from evercraft.models.character import Character
import math

class Monk(Character):
    def __init__(self, obj={}):
        base_hp = 6
        MONK_DEFAULT: {
        "name": "Evercraft",
        "alignment": "neutral",
        "AC": 10,
        "HP": 6,
        "life": True,
        "str": 10,
        "dex": 10,
        "int": 10,
        "wis": 10,
        "cha": 10,
        "con": 10,
        "XP": 0,
        "level": 1,
        "base_hp":6
        }
        for key in obj:
            if key in obj:
                setattr(self, key, obj[key])
            else:
                setattr(self, key, self.MONK_DEFAULT[key])
        self.AC = self.set_AC(self.dex, self.wis)
        self.HP = self.set_HP(self.con)
        self.check_XP(self.XP)

    def attack(self, target, roll, score):
        mod = self.modify(score)
        #starting dmg is 3, not 1#
        damage = 3 + mod
        mod_level = (math.floor(self.level/2))
        ##additional mod special to monks
        monk_level_mod = self.level//3
        if roll == 20:
            self.XP = self.XP + 10
            self.check_XP(self.XP)
            if damage < 1:
                damage = 1
            target.HP = target.HP - (damage*2)
            if target.HP <= 0:
                target.life = False
            return 'Hit'
        elif roll + mod + mod_level + monk_level_mod >= target.AC:
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

    # adding 6 hp per level instead of 5
    def set_HP(self, score):
        print('character set hp')
        return max(6 * self.level, 6*self.level + self.modify(score)*self.level)

    # adding 3 times the wisdom to the armor class
    def set_AC(self, score, second_score):
        print("I am modifying AC")
        return max(1, self.AC + self.modify(score) + self.modify(second_score))