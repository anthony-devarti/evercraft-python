# this is where your character code will go
TRAITS = {
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


"""CHARACTER_DEF = {
    "name": "Evercraft",
    "alignment": "neutral",
    "AC": 10,
    "hit_point": 5
}"""
 
class Character:
    name = "Evercraft"
    alignment = "neutral"
    AC = 10
    HP = 5
    life = True
    str = 10
    dex = 10
    int = 10
    wis = 10
    cha = 10
    con = 10
    def __init__(self, obj=None):
        if obj:
            self.life = obj["life"]
            self.str = obj["str"]
            self.dex = obj["dex"]
            self.int = obj["int"]
            self.wis = obj["wis"]
            self.cha = obj["cha"]
            self.con = obj["con"]
            self.name = obj["name"]
            self.alignment = obj["alignment"] 
            self.AC = obj["AC"]+(self.modify(self.dex))
            self.HP = max(1, obj["HP"]+(self.modify(self.con)))

    def set_name(self, name):
       self.name = name

    def get_name(self):
       return self.name
    
    def attack(self, target, roll, score):
        ###
        mod = self.modify(score)
        damage = 1 + mod
        ###
        if roll == 20:
            if damage < 1:
                damage = 1
            target.HP = target.HP - (damage*2)
            if target.HP <= 0:
                target.life=False
            return 'Hit'
        elif roll + mod >= target.AC:
            if damage < 1:
                damage = 1
            target.HP = target.HP - damage
            if target.HP<=0:
                target.life=False
            return "Hit"
        elif roll + mod < target.AC:
            return "Whiff"
        else:
            return "That doesn't seem to be a number"

    def modify(self, score):
        switcher={
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



c1 = Character(TRAITS)

c2 = Character()
bad_guy = {
    "name": "Evil Rufus",
    "alignment": 'evil',
    "AC": 12,
    'HP': 8,
    "life": True,
    "str" : 10,
    "dex" : 10,
    "int" : 10,
    "wis" : 10,
    "cha" : 10,
    "con" : 10
}
enemy = Character(bad_guy)
print(c1.AC)


