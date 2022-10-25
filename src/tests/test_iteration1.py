from evercraft import *

def test_character_exists():
    assert Character() is not None
def test_character_name():
    variable_name = Character()
    variable_name.create('Sims McBirdman', 'Chaotic Neutral')
    assert variable_name.get('name') is not None
def test_set_character_name():
    name = 'Sims McBirdman'
    character1 = Character(name, 'Chaotic Neutral')
    assert character1.name is name
def test_character2_name():
    character2 = Character()
    character2.create('Adfa', 'Neutral Good')
    assert character2.get('name') is 'Adfa'
def test_character_change_name():
    name = 'Sims McBirdman'
    character1 = Character(name, 'Chaotic Neutral')
    character1.name = 'Adfa'
    assert character1.name is not name
def test_character_alignment():
    sims = Character("Sims McBirdman", 'Chaotic Neutral')
    assert sims.alignment is not None
def test_character_ac_exists():
    sims = Character("Sims McBirdman", 'Chaotic Neutral')
    assert sims.armor is not None
def test_character_health():
    sims = Character("Sims McBirdman", 'Chaotic Neutral')
    assert sims.health == 5
def test_character_attack_hit():
    sims = Character('Sims McBirdman', 'Chaotic Neutral')
    rat = Character("rat", "Chaotic Evil")
    assert sims.attack(12, rat) == True
def test_character_attack_miss():
    sims = Character('Sims McBirdman', 'Chaotic Neutral')
    rat = Character("rat", "Chaotic Evil")
    assert sims.attack(1, rat) == False
def test_character_attack_damage():
    sims = Character('Sims McBirdman', 'Chaotic Neutral')
    rat = Character("rat", "Chaotic Evil")
    sims.attack(12, rat)
    assert rat.health != 5
def test_character_critical_hit():
    sims = Character('Sims McBirdman', 'Chaotic Neutral')
    rat = Character("rat", "Chaotic Evil")
    sims.attack(20, rat)
    assert rat.health == 3
def test_character_isAlive():
    sims = Character('Sims McBirdman', 'Chaotic Neutral')
    assert sims.isAlive 
def test_character_ratDeath():
    rat = Character('rat', 'Chaotic Neutral')
    sims = Character('Sims McBirdman', 'Chaotic Neutral')
    rat.health = 1
    sims.attack(14, rat)
    assert not rat.isAlive
def test_character_abilities():
    sims = Character('Sims McBirdman', 'Chaotic Neutral')
    assert sims.dexterity == 10
def test_character_modifiers():
    sims = Character('Sims McBirdman', 'Chaotic Neutral')
    sims.dexterity = 15
    assert sims.modifiers('dexterity') == 10
