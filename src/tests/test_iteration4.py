from evercraft2 import *

def test_is_this_connected():
    josh = Character('Josh', 'Chaotic Neutral', 'orc')
    assert josh.race is 'orc'

def test_character_has_weapon():
    josh = Character('Josh', 'Chaotic Neutral', 'orc')
    assert josh.weapon_list is not None

def test_character_has_armor():
    josh = Character('Josh', 'Chaotic Neutral', 'orc')
    assert josh.armor_list is not None    

def test_character_klass():
    josh = Fighter('Josh', 'chaotic Neutral')
    assert josh.klass is "fighter" 

def test_character_can_equip_weapon_two():
    josh = Fighter('Josh', 'chaotic Neutral')
    josh.equip_weapon('longsword')
    assert josh.damage == 5

def test_character_can_un_equip_weapon_two():
    josh = Fighter('Josh', 'chaotic Neutral')
    josh.equip_weapon('longsword')
    josh.unequip_weapon('longsword')
    assert josh.equiped_weapon == ''

def test_character_can_un_equip_weapon():
    josh = Fighter('Josh', 'chaotic Neutral')
    josh.equip_weapon('longsword')
    josh.unequip_weapon('longsword')
    assert josh.damage == 1

def test_character_can_equip_weapon():
    josh = Fighter('Josh', 'chaotic Neutral')
    josh.equip_weapon('longsword')
    assert josh.equiped_weapon == 'longsword'   

def test_another_weapon():
    josh = Fighter('Josh', 'chaotic Neutral')
    josh.equip_weapon('waraxe')
    assert josh.damage == 8

def test_if_to_hit_works():
    josh = Fighter('Josh', 'chaotic Neutral')
    josh.equip_weapon('waraxe')   
    assert josh.crit_mult == 3

def test_waraxe_hits():
    josh = Character('Josh', 'chaotic Neutral')
    rat = Character('rat', 'Alignment')
    josh.equip_weapon('waraxe')
    assert josh.attack(8, rat)
    
def test_unequip_weapon():
    josh = Character('Josh', 'chaotic Neutral')
    josh.equip_weapon('elven_longsword')
    assert josh.equiped_weapon is 'elven_longsword'

def test_daniel_done_with_evercraft():
    daniel = Rogue('Daniel', 'Chaotic', 'halfling')
    daniel.__setattr__('is_done_with_evercraft', True)
    assert daniel.is_done_with_evercraft

def test_estus_done_with_evercraft():
    estus = Monk('Estus', 'Chaotic', 'dwarf')
    estus.__setattr__('is_done_with_evercraft', True)
    assert estus.is_done_with_evercraft
    

# def test_armor_can_be_equiped():
#     josh = Character('Josh', 'chaotic Neutral')
#     josh.equiped_armor()    





