from evercraft2 import *

def test_character_exists():
    assert Character('Sims McBirdman', "Chaotic Neutral") is not None

def test_character_name():
    variable_name = Character('Sims McBirdman', "Chaotic Neutral")
    assert variable_name.name is not None

def test_set_character_name():
    name = 'Sims McBirdman'
    character1 = Character(name, "Chaotic Neutral")
    assert character1.name is name

def test_character2_name():
    character2 = Character('Adfa', "Neutral Good")
    assert character2.name is 'Adfa'

def test_character_change_name():
    name = 'Sims McBirdman'
    character1 = Character(name, 'Chaotic Neutral')
    character1.name = 'Adfa'
    assert character1.name is not name

def test_character_alignment():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    assert sims.alignment is not None

def test_character_ac_exists():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    assert sims.ac is not None

def test_character_ac_change():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    sims.ac = sims.ac + 2
    assert sims.ac is 12

def test_character_health_ex():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    assert sims.health == 5

def test_character_attack_hit():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    rat = Character('rat', 'Chaotic Evil')
    assert sims.attack(12, rat) == True

def test_character_attack_miss():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    rat = Character('rat', 'Chaotic Evil')
    assert sims.attack(1, rat) == False

def test_character_attack_damage():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    rat = Character('rat', 'Chaotic Evil')
    sims.attack(12, rat)
    assert rat.health != 5

def test_character_critical_hit():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    rat = Character('rat', 'Chaotic Evil')
    sims.attack(20, rat)
    assert rat.health == 3

def test_character_is_alive():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    assert sims.is_alive

def test_character_rat_death():
    rat = Character('rat', 'Chaotic Evil')
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    rat.health = 1
    sims.attack(14, rat)
    assert not rat.is_alive

def test_character_abilities():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    assert sims.dex == 10

def test_character_modifiers():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    sims.dex = 14
    assert sims.modifiers('dex') == 2

def test_character_modifiers2():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    sims.dex = 19
    assert sims.modifiers('dex') == 4

def test_character_modifiers_negative():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    sims.dex =  4
    assert sims.modifiers('dex') == -3

def test_character_modifiers_negative2():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    sims.dex =  7
    assert sims.modifiers('dex') == -2

def test_character_modifiers_negative3():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    sims.dex =  3
    assert sims.modifiers('dex') == -4

def test_character_adding_attribute():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    rat = Character('rat', 'Chaotic Evil')
    sims.str = 15
    sims.attack(15, rat)
    assert rat.health == 2

def test_character_attack_minus():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    rat = Character('rat', 'Chaotic Evil')
    rat.str = 7
    rat.attack(15, sims)
    assert sims.health == 4

def test_character_attack_critical_modifier():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    rat = Character('rat', 'Chaotic Evil')
    sims.str = 16
    sims.attack(20, rat)
    assert rat.is_alive is not True

def test_character_critical_attack_modifier_negative():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    rat = Character('rat', 'Chaotic Evil')
    rat.str = 5
    rat.attack(20, sims)
    assert sims.health == 3

def test_character_attack_modifier_two():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    rat = Character('rat', 'Chaotic Evil')
    sims.str = 17
    sims.attack(7, rat)
    assert rat.health == 1

def test_character_ac_added():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    rat = Character('rat', 'Chaotic Evil')
    sims.dex = 17
    assert not rat.attack(12, sims)

def test_character_ac():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    rat = Character('rat', 'Chaotic Evil')
    rat.dex = 1
    assert sims.attack(5, rat)

def test_character_health():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    rat = Character('rat', 'Chaotic Evil') 
    sims.con = 13
    sims.update_character()
    assert not sims.health == 5

def test_character_exp_exists():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    rat = Character('rat', 'Chaotic Evil') 
    assert sims.exp is not None

def test_character_gain_exp():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    rat = Character('rat', 'Chaotic Evil')
    sims.attack(11 , rat)
    assert sims.exp == 10

def test_character_level_exits():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    assert sims.level is not None

def test_character_level_up():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    rat = Character('rat', 'Chaotic Evil')
    sims.exp = 990
    sims.attack(12, rat)
    assert sims.level == 2

def test_character_level_3():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    rat = Character('rat', 'Chaotic Evil')
    sims.exp = 1990
    sims.level = 2
    sims.attack(12, rat)
    assert sims.level == 3

def test_character_repeat_hit_level():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    rat = Character('rat', 'Chaotic Evil')
    for i in range(0,100):
        sims.attack(12, rat)
    assert sims.level == 2    

def test_character_hit_no_level():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    rat = Character('rat', 'Chaotic Evil')
    sims.exp = 980
    sims.attack(12, rat)
    assert sims.level == 1

def test_character_hit_increases():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    rat = Character('rat', 'Chaotic Evil')
    sims.exp = 990
    sims.attack(12, rat)
    assert sims.health != 5

def test_character_damage_increase():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    rat = Character('rat', 'Chaotic Evil')
    sims.level = 2
    sims.attack(10, rat)
    assert rat.health == 3


def test_character_odd_level():
    sims = Character('Sims McBirdman', "Chaotic Neutral")
    rat = Character('rat', 'Chaotic Evil')
    sims.level = 5
    sims.attack(10, rat)
    assert rat.health == 2