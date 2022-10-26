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

def test_fighter_miss_
