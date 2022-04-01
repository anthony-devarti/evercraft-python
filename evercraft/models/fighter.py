##this is working, but the output window is not recognizing it
##we are successfully inheriting init and other functions from the parent
from evercraft.models.character import Character

class Fighter(Character):
    #changed the attack to include feat1
    def attack(self, target, roll, score):
        mod = self.modify(score)
        damage = 1 + mod
        #this is different from the parent class
        mod_level = self.level-1
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

    def set_HP(self, score):
        print('fighter set hp') 
        return self.HP + 10*(self.level-1) + self.modify(score)*self.level
        

