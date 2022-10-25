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

def test_character_health():
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
    
