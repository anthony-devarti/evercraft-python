##same issue here.
from evercraft.models.character import Character

class Rogue(Character):

    def attack(self, target, roll, score):
        mod = self.modify(score)
        damage = 1 + mod
        mod_level = (math.floor(self.level/2))
        if roll == 20:
            self.XP = self.XP + 10
            self.check_XP(self.XP)
            if damage < 1:
                damage = 1
            target.HP = target.HP - (damage*2)
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