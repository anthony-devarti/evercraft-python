# this is where your character code will go
TRAITS = {
    "name": "Rufus",
    "alignment": 'good',
    "AC": 12,
    'HP': 8
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
    def __init__(self, obj=None):
        if obj:
            self.name = obj["name"]
            self.alignment = obj["alignment"] 
            self.AC = obj["AC"]
            self.HP = obj["HP"]
     
    def set_name(self, name):
       self.name = name

    def get_name(self):
       return self.name
    
    def attack(target, roll):
        if roll == 20 or roll >= target.AC:
            target.HP = target.HP - 1
            return 'Hit'
        elif roll < target.AC:
            return "Whiff"
        else:
            return "That doesn't seem to be a number"


c1 = Character(TRAITS)
c2 = Character()
bad_guy = {
    "name": "Evil Rufus",
    "alignment": 'evil',
    "AC": 12,
    'HP': 8
}
enemy = Character(bad_guy)
print(c1.AC)


