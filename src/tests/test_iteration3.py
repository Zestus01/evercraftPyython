from evercraft2 import *

def test_race_does_exist():
    dan = Character('dan', 'Chaotic Neutral')
    assert dan.race is 'human'

def test_race_change_to_elf():
    estus = Character('estus', 'Chaotic Neutral', 'elf')
    assert estus.race is 'elf'

def test_race_change_with_class():
    estus = Paladin('estus', 'Chaotic Neutral', 'elf')
    assert estus.race == 'elf' and estus.klass is 'paladin'

def test_race_can_be_orc():
    josh = Character('josh', 'Chaotic Neutral', 'orc')
    assert josh.str == 14

def test_rogue_can_be_orc():
    josh = Rogue('josh', 'Chaotic Neutral', 'orc')
    assert josh.klass == 'rogue' and josh.race == 'orc'

def test_race_orc_ac_bonus():
    josh = Character('josh', 'Chaotic Neutral', 'orc')
    rat = Character('rat', 'Neutral')
    assert not rat.attack(11, josh)

def test_race_orc_wis_change():
    josh = Character('josh', 'Chaotic Neutral', 'orc')
    assert josh.wis != 10

def test_race_dwarf_con():
    gimli = Character('Gimli', 'Lawful Good', 'dwarf')
    assert gimli.race == 'dwarf'

def test_dwarf_race_minus_chr():
    gimli = Character('Gimli', 'Lawful Good', 'dwarf')
    assert gimli.chr == 8

def test_race_dwarf_con_level():
    gimli = Character('Gimli', 'Lawful Good', 'dwarf')
    gimli.level_up()
    assert gimli.health == 20

def test_race_dwarf_con_level_two():
    gimli = Character('Gimli', 'Lawful Good', 'dwarf')
    gimli.con = 16
    gimli.level_up()
    assert gimli.health == 24

def test_dwarf_hurt_orc():
    gimli = Character('Gimli', 'Lawful Good', 'dwarf')
    josh = Character('josh', 'Chaotic Neutral', 'orc')
    gimli.attack(13, josh)
    assert josh.health == 7

def test_dwarf_hurt_orc_two():
    gimli = Character('Gimli', 'Lawful Good', 'dwarf')
    josh = Character('josh', 'Chaotic Neutral', 'orc')
    assert gimli.attack(10, josh)

def test_dwarf_not_get_bonus():
    gimli = Character('Gimli', 'Lawful Good', 'dwarf')
    josh = Character('josh', 'Chaotic Neutral', 'elf')
    assert gimli.attack(12, josh)

def test_elf_con_mod():
    estus = Character('estus', 'Chaotic Neutral', 'elf') 
    assert estus.modifiers('con') == -1

def test_elf_crit_range():
    estus = Character('estus', 'Chaotic Neutral', 'elf')   
    josh = Character('josh', 'Chaotic Neutral', 'orc')
    estus.attack(19, josh)
    assert josh.health == 8

def test_elf_extra_dex_ac():
    estus = Character('estus', 'Chaotic Neutral', 'elf')  
    rat = Character('Rat', 'Rat')
    assert not rat.attack(10, estus)

def test_elf_ac_bonus_orc():
    josh = Character('josh', 'Chaotic Neutral', 'orc')
    estus = Character('estus', 'Chaotic Neutral', 'elf')  
    assert not josh.attack(10, estus)

def test_halfling_bonus_dex_mod():
    stimpy = Character('Stimpy', 'Good', 'halfling')
    assert stimpy.modifiers('dex') == 1

def test_halfling_not_evil():
    stimpy = Character('Stimpy', 'evil', 'halfling')
    assert stimpy.alignment is not 'evil'

def test_halfling_on_halfling_violence():
    stimpy = Character('Stimpy', 'evil', 'halfling')
    frodo = Character('Frodo', 'Good', 'halfling')
    assert stimpy.attack(13, frodo)

def test_halfling_bonus_ac():
    stimpy = Character('Stimpy', 'evil', 'halfling')
    rat = Character('Rat', 'Neutral')
    assert not rat.attack(12, stimpy)
