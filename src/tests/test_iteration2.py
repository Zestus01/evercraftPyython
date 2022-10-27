## Tests for iterations 2
from evercraft2 import *

def test_fighter_exist():
    fighter = Fighter('name', 'alignment')
    assert fighter is not None

def test_fighter_check_name():
    fighter = Fighter('john', 'good')
    assert fighter.name != None

def test_fighter_knows_modifier():
    fighter = Fighter('john', 'good')
    fighter.str = 14
    assert fighter.modifiers('str') == 2

def test_fighter_klass():
    fighter = Fighter('john', 'good')
    assert fighter.klass == 'fighter'
    
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

def test_rogue_klass_attribute():
    sneaky = Rogue('Sneaky', 'Evil')
    assert sneaky.klass == 'rogue'

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

def test_monk_klass():
    buddha = Monk('Buddha', 'Neutral')
    assert buddha.klass is not 'thing'

def test_monk_klass_two():
    buddha = Monk('Buddha', 'Neutral')
    assert buddha.klass is 'monk'

def test_monk_wis_ac_positive():
    buddha = Monk('Buddha', 'Neutral')
    rat = Character('rat', 'Chaotic Evil')
    buddha.wis = 14
    buddha.update_character()
    assert not rat.attack(11, buddha)

def test_monk_wis_ac_negative():
    buddha = Monk('Buddha', 'Neutral')
    rat = Character('rat', 'Chaotic Evil')
    buddha.wis = 8
    buddha.update_character()
    assert buddha.ac == 10

def test_monk_gain_6_health_level():
    buddha = Monk('Buddha', 'Neutral')
    rat = Character('rat', 'Chaotic Evil')
    buddha.exp = 990
    buddha.attack(15, rat)
    assert buddha.health == 11

def test_monk_extra_damage():
    buddha = Monk('Buddha', 'Neutral')
    rat = Character('rat', 'Chaotic Evil')
    buddha.attack(14, rat)
    assert rat.health == 2

def test_monk_crit_hit():
    buddha = Monk('Buddha', 'Neutral')
    rat = Character('rat', 'Chaotic Evil')
    buddha.attack(20, rat)
    assert rat.is_alive == False

def test_monk_to_hit_2_level():
    buddha = Monk('Buddha', 'Neutral')
    rat = Character('rat', 'Chaotic Evil')
    buddha.level = 2
    assert buddha.attack(9, rat)
    
def test_monk_to_hit_3_level():
    buddha = Monk('Buddha', 'Neutral')
    rat = Character('rat', 'Chaotic Evil')
    buddha.level = 3
    assert buddha.attack(8, rat)

def test_monk_to_hit_6_level():
    buddha = Monk('Buddha', 'Neutral')
    rat = Character('rat', 'Chaotic Evil')
    buddha.level = 6
    assert buddha.attack(5, rat)

def test_paladin_exists():
    jesus = Paladin('Jesus', 'Good')
    assert jesus is not None

def test_paladin_exists():
    jesus = Paladin('Jesus', 'Good')
    assert jesus.klass is 'paladin'   

def test_paladin_is_good():
    lucifer = Paladin('Lucifer', 'Evil')
    assert lucifer.alignment != 'Evil'


def test_paladin_8_health():
    jesus = Paladin('Jesus', 'Good')
    rat = Character('rat', 'Chaotic Evil')
    jesus.exp = 990
    jesus.attack(13, rat)
    assert jesus.health == 13

def test_paladin_extra_damage_evil():
    jesus = Paladin('Jesus', 'Good')    
    rat = Character('rat', 'Lawful evil')
    jesus.attack(14, rat)
    assert rat.health == 1

def test_paladin_extra_damage_not_evil():
    jesus = Paladin('Jesus', 'Good')
    rat = Character('rat', 'Chaotic')
    jesus.attack(14, rat)
    assert rat.health == 3

def test_paladin_smite_evil():
    jesus = Paladin('Jesus', 'Good')
    rat = Character('rat', 'Chaotic Evil')
    jesus.attack(20, rat)
    assert not rat.is_alive

def test_paladin_to_hit_plus1():
    jesus = Paladin('Jesus', 'Good')
    rat = Character('rat', 'Chaotic')
    jesus.level_up()
    assert jesus.attack(8, rat)

def test_paladin_smite_evil_on_miss():
    jesus = Paladin('Jesus', 'Good')
    rat = Character('rat', 'Chaotic Evil')
    assert jesus.attack(8, rat)