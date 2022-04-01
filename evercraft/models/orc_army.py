from evercraft.models.character import Character
from evercraft.models.fighter import Fighter
#as a dm, I can generate an orc army of variable size for combat encounters
#they have varied names
#they are all fighters
orc_names=[
    Ouhgan,
    Zunodagh,
    Darfu,
    Xorag,
    Shurkul,
    Ignorg,
    Lugdum,
    Verthag,
    Brag,
    Dubok,
    Yahg,
    Knurigig,
    Sogorim,
    Nag,
    Crothu,
    Sahgorim,
    Surgug,
    Durbul,
    Karthurg,
    Oghuglat,
    Orpigig,
    Gradba,
    Hagub,
    Kharag,
    Jorgagu,
    Dregu,
    Wholug,
    Epkagut,
    Tidgug,
    Opathu,
    Baronk,
    Olaghig,
    Perthag,
    Xruul,
    Zurghed,
    Kurz,
    Urbul,
    Sogugbu,
    Gulm,
    Porgarag
    ]

def orc_army(size):
    army=[]
    for i in range(size):
        orc_name=random.choice(orc_names)
        orc_name = Fighter({"name":orc_name})
        orc_name.is_orc()
        # print(orc_name + 'has enlisted')
        orc_name.append(army)
