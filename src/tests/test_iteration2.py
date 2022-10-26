## Tests for iterations 2
from evercraft2 import *

def test_fighter_exist():
    fighter = Fighter('name', 'alignment')
    assert fighter is not None

def test_fighter_check_name():
    fighter = Fighter('john', 'good')
    assert fighter.name != None

def test_fighter_knows_modifer():
    fighter = Fighter('john', 'good')
    fighter.str = 14
    assert fighter.modifiers('str') == 2
    
def test_fighter_extra_to_hit():
    billy = Fighter('Billy Joe Bob', "Chaotic Neutral")
    rat = Character('rat', 'Chaotic Evil')
    assert billy.attack(9, rat)

def test_fighter_miss_hit():
    billy = Fighter('Billy Joe Bob', "Chaotic Neutral")
    rat = Character('rat', 'Chaotic Evil')
    assert not billy.attack(8, rat)

def test_fighter_not_gain_5_hp_on_level():
    billy = Fighter('Billy Joe Bob', "Chaotic Neutral")
    rat = Character('rat', 'Chaotic Evil')
    billy.exp = 990
    billy.attack(15, rat)
    assert billy.health != 10

def test_fighter_gain_10_hp_on_level():
    billy = Fighter('Billy Joe Bob', "Chaotic Neutral")
    rat = Character('rat', 'Chaotic Evil')
    billy.exp = 990
    billy.attack(15, rat)
    assert billy.health == 15

def test_rogue_exists():
    sneaky = Rogue('Sneaky', 'Evil')
    assert sneaky is not None

def test_rogue_not_good():
    sneaky = Rogue('Sneaky', 'Good')
    assert sneaky.alignment is not 'Good'

def test_rogue_triple_damage():
    sneaky = Rogue('Sneaky', 'Good')
    rat = Character('rat', 'Chaotic Evil')
    sneaky.attack(20, rat)
    assert rat.health == 3

def test_rogue_triple_damage_with_dex_mod():
    sneaky = Rogue('Sneaky', 'Good')
    rat = Character('rat', 'Chaotic Evil')
    sneaky.dex = 14
    rat.health = 10
    sneaky.attack(20, rat)
    assert rat.health == 2

def test_rogue_ignore_ac():
    sneaky = Rogue('Sneaky', 'Good')
    rat = Character('rat', 'Chaotic Evil')
    rat.dex = 16
    assert sneaky.attack(13, rat)
    
def test_rogue_damage_mod_dex():
    sneaky = Rogue('Sneaky', 'Good')
    rat = Character('rat', 'Chaotic Evil')
    sneaky.dex = 14
    rat.health = 10
    sneaky.attack(14, rat)
    assert rat.health == 7 

def test_rogue_to_hit_mod_dex():
    sneaky = Rogue('Sneaky', 'Good')
    rat = Character('rat', 'Chaotic Evil')
    sneaky.dex = 14
    rat.health = 10
    sneaky.attack(8, rat)
    assert rat.health == 7 

def test_rogue_level_up():
    sneaky = Rogue('Sneaky', 'Good')
    rat = Character('rat', 'Chaotic Evil')
    sneaky.dex = 14
    sneaky.exp = 990
    sneaky.attack(14, rat)
    assert sneaky.level == 2

def test_rogue_level_up_health():
    sneaky = Rogue('Sneaky', 'Good')
    rat = Character('rat', 'Chaotic Evil')
    sneaky.dex = 14
    sneaky.exp = 990
    sneaky.attack(14, rat)
    assert sneaky.health == 10

def test_monk_exists():
    buddha = Monk('Buddha', 'Neutral')
    assert buddha is not None

def test_monk_wis_ac_positive():
    buddha = Monk('Buddha', 'Neutral')
    rat = Character('rat', 'Chaotic Evil')
    buddha.wis = 14
    assert rat.attack(11, buddha)

def test_monk_wis_ac_negative():
    buddha = Monk('Buddha', 'Neutral')
    rat = Character('rat', 'Chaotic Evil')
    buddha.wis = 8
    assert rat.attack(11, buddha)

def test_monk_gain_6_health_level():
    buddha = Monk('Buddha', 'Neutral')
    rat = Character('rat', 'Chaotic Evil')
    buddha.exp = 990
    buddha.attack(15, rat)
    assert buddha.health == 11