from evercraft import *

def test_character_exists():
    assert Character() is not None

def test_character_name():
    variable_name = Character()
    variable_name.create('Sims', 'Chaotic')
    assert variable_name.get('name') is not None

def test_set_character_name():
    name = 'Sims McBirdman'
    character1 = Character()
    character1.create(name, 'Chaotic Neutral')
    assert character1.get('name') is name

def test_character2_name():
    character2 = Character()
    character2.create('Adfa', 'Neutral Good')
    assert character2.get('name') is 'Adfa'

def test_character_change_name():
    name = 'Sims McBirdman'
    character1 = Character()
    character1.create(name, 'Chaotic Neutral')
    character1.add('name', 'Adfa')
    assert character1.get('name') is not name

def test_character_alignment():
    sims = Character()
    sims.create('Sims McBirdman', "Chaotic Neutral")
    assert sims.get('alignment') is not None

def test_character_ac_exists():
    sims = Character()
    sims.create('Sims McBirdman', "Chaotic Neutral")
    assert sims.get('ac') is not None

def test_character_health():
    sims = Character()
    sims.create('Sims McBirdman', "Chaotic Neutral")
    assert sims.get('health') == 5

def test_character_attack_hit():
    sims = Character()
    sims.create('Sims McBirdman', "Chaotic Neutral")
    rat = Character()
    rat.create("rat", "Chaotic Evil")
    assert sims.attack(12, rat) == True

def test_character_attack_miss():
    sims = Character()
    rat = Character()
    sims.create('sims McBirdman', 'Chaotic neutral')
    rat.create('rat', 'Chaotic Evil')
    assert sims.attack(1, rat) == False

def test_character_attack_damage():
    sims = Character()
    rat = Character()
    sims.create('Sims mcBirdman', "Chaotic Neutral")
    rat.create('rat', 'Chaotic Evil')
    sims.attack(12, rat)
    assert rat.get('health') != 5

def test_character_critical_hit():
    sims = Character()
    rat = Character()
    sims.create('Sims McBirdman', 'Chaotic neutral')
    rat.create('rat', 'Chaotic Evil')
    sims.attack(20, rat)
    assert rat.get('health') == 3

def test_character_isAlive():
    sims = Character()
    sims.create('Sims McBirdman', 'Chaotic Neutral')
    assert sims.get('is_alive')

def test_character_ratDeath():
    rat = Character()
    rat.create("rat", "Chaotic Evil")
    sims = Character()
    sims.create('Sims McBirdman', 'Chaotic Neutral')
    rat.add('health', 1)
    sims.attack(14, rat)
    assert not rat.get('is_alive')

def test_character_abilities():
    sims = Character()
    sims.create('Sims McBirdman', 'Chaotic Neutral')
    assert sims.get('dex') == 10
    
def test_character_modifiers():
    sims = Character()
    sims.add('dexterity', 15)
    assert sims.modifiers('dexterity') == 15
