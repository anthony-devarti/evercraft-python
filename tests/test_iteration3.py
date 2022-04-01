import pytest
from evercraft.models.character import Character
from evercraft.models.fighter import Fighter
from evercraft.models.rogue import Rogue
from evercraft.models.monk import Monk
from evercraft.models.paladin import Paladin

#Orc#

# - +2 to Strength Modifier mod 
def test_str_mod_adjust():
    tusku=Character()
    tusku.is_orc()
    assert tusku.str==12

# -1 to Intelligence mod 
def test_orc_no_smort():
    tusku=Character()
    tusku.is_orc()
    assert tusku.int==9

# -1 to Wisdom mod
def test_orc_make_poor_life_decision():
    tusku=Character()
    tusku.is_orc()
    assert tusku.wis==9

# -1 to Charisma Modifier
def test_orc_no_make_word():
    tusku=Character()
    tusku.is_orc()
    assert tusku.cha==9

# - +2 to Armor Class due to thick hide
def test_orc_no_hurt():
    tusku=Character()
    tusku.is_orc()
    assert tusku.AC==12

# >Dwarf<

# - +1 to Constitution Modifier
def test_dwarf_has_good_con():
    bibi=Character()
    bibi.is_dwarf()
    assert bibi.con==11
# -1 to Charisma Modifier
def test_dwarf_shy():
    bibi=Character()
    bibi.is_dwarf()
    assert bibi.cha==9
# - doubles Constitution Modifier when adding to hit points per level (if positive)
def test_dwarf_has_hp():
    bibi=Character()
    bibi.con=13
    bibi.is_dwarf()
    assert bibi.HP==9

# double the con mod for HP at levelup
def test_dwarf_has_hp_at_level():
    bibi=Character()
    bibi.con=14
    bibi.is_dwarf()
    enemy=Character()
    bibi.XP=990
    bibi.attack(enemy, 15, bibi.str)
    assert bibi.HP==9
# - +2 bonus to attack when attacking orcs (Dwarves hate Orcs)
def test_orc_rivalry():
    bibi=Character()
    bibi.is_dwarf()
    enemy=Character()
    enemy.is_orc()
    assert bibi.attack(enemy, 10, bibi.str)=="Hit"
# +2 bonus to attack when attacking orcs
def test_orc_rivalry():
    bibi=Character()
    bibi.is_dwarf()
    enemy=Character()
    enemy.is_orc()
    bibi.attack(enemy, 10, bibi.str)
    assert enemy.HP==2

#    >Elf< 

# - +1 to Dexterity Modifier, -1 to Constitution Modifier
def test_elf_dexterity():
    elfi=Character()
    elfi.is_elf()
    assert elfi.dex == 11

def test_elf_less_constitution():
    elfi = Character()
    elfi.is_elf()
    assert elfi.con == 9

# - does adds 1 to critical range for critical hits 
def test_elf_critical_hit():
    elfi = Character()
    elfi.is_elf()
    enemy = Character()
    assert elfi.attack(enemy, 19, elfi.str) == "Crit"
    
# (20 -> 19-20, 19-20 -> 18-20)
# - +2 to Armor Class when being attacked by orcs
def test_orc_defense():
    elfi = Character()
    elfi.is_elf()
    enemy = Character()
    enemy.is_orc()
    assert enemy.attack(elfi,9,enemy.str) == "Whiff"

# >Halfling<

# - +1 to Dexterity Modifier, -1 to Strength Modifier
def test_hafling_dexterity():
    hoofus=Character()
    hoofus.is_halfling()
    assert hoofus.dex == 11

def test_halfling_less_strength():
    hoofus=Character()
    hoofus.is_halfling()
    assert hoofus.str == 9

# - +2 to Armor Class when being attacked by non Halfling 
# (they are small and hard to hit)
def test_halfing_defense():
    hoofus = Character()
    hoofus.is_halfling()
    enemy = Character()
    enemy.is_orc()
    assert enemy.attack(hoofus,9,enemy.str) == "Whiff"

# - cannot have Evil alignment
def test_must_not_be_evil():
    traits ={
        "alignment":"evil"
    }
    hoofus = Character(traits)
    hoofus.is_halfling()
    assert hoofus.alignment != "good"