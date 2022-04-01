##same issue here.
from evercraft.models.character import Character
import math
class Rogue(Character):

    def __init__(self, obj={}):
        for key in obj:
            if key in obj:
                setattr(self, key, obj[key])
            else:
                setattr(self, key, self.DEFAULT[key])
        self.AC = self.set_AC(self.dex)
        self.HP = self.set_HP(self.con)
        self.check_XP(self.XP)
        if self.alignment=="good":
            print("You're a rogue! You're neutral, at best.")
            self.alignment="neutral"

    def attack(self, target, roll, score):
        mod = self.modify(score)
        damage = 1 + mod
        mod_level = (math.floor(self.level/2))
        #this recalculates the opp dex mod to be subtracted later.  
        #This allows us to not mutate other players' stats in this attack method
        opp_dex = target.modify(target.dex)
        if roll == 20:
            self.XP = self.XP + 10
            self.check_XP(self.XP)
            if damage < 1:
                damage = 1
            ##rogues do more damage on crits
            target.HP = target.HP - (damage*3)
            if target.HP <= 0:
                target.life = False
            return 'Hit'
        #this where the calculated dex is being subtracted from the target armor class
        elif roll + mod + mod_level >= target.AC - opp_dex:
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


    