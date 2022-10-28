import random

class Equipment():
    armor_list = { 
        'leather_armor': {'ac': 2},
        'plate_armor': {'klass': 'fighter', 
                        'race': 'dwarf', 
                        'ac': 8},
        'magic_leather': {'ac': 2, 
                            'damage_received': -2},
        'shield': {'ac': 3, 
                    'klass': 'fighter', 
                    'weapon_bonus': -4, 
                    'negative': -2}
    }
    weapon_list = {
        'longsword': {'damage': 4},
        'waraxe': {'damage': 7, 
                    'weapon_bonus': + 2, 
                    'crit_mult': + 1},
        'elven_longsword': {'damage': 5, 
                            'weapon_bonus': 1, 
                            'race_target_weapon': 'orc', 
                            'race_wield_weapon': 'elf', 
                            'race_bonus': 2, 
                            'race_bonus_double': 5},
        'nun_chucks': {'damage': 5, 
                        'klass': 'monk', 
                        'negative': -4},
        'source_code': {'damage': 8,
                        'crit_mult': +3,
                        'crit_range': -2},
        'goblin_spear':{'damage': 4,
                        'crit_range': -1,
                        'dex': 2},
        'sword_of_stupidity':{'int': -4,
                            'wis': -4,
                            'crit_mult': + 4}                
    }
    misc_list = dict()

class Dice():
    def roll_dice(self, die):
        twenty = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        twelve = [1,2,3,4,5,6,7,8,9,10,11,12]
        eight = [1,2,3,4,5,6,7,8]
        six = [1,2,3,4,5,6]
        four = [1,2,3,4]
        
        if die == 20:
            roll = random.choice(twenty)
        elif die == 12:
            roll = random.choice(twelve)
        elif die == 8:
            roll = random.choice(eight)
        elif die == 6:
            roll = random.choice(six)
        elif die == 4:
            roll = random.choice(four)
        elif die == 1:
            roll == 20
        return roll

class Character(Equipment, Dice):

    def __init__(self, name, alignment, race = 'human'):
        self.name = name
        self.alignment = alignment
        self.is_alive = True
        self.dex = 10
        self.str = 10
        self.wis = 10
        self.chr = 10
        self.con = 10
        self.int = 10
        self.ac = 10
        self.exp = 0
        self.level = 1
        self.health = 5
        self.damage = 1 ## Base damage 1
        self.crit_mult = 2 ## Helper variable for rogue, crit damage
        self.health_increase = 5 ## Variable for health increase per level
        self.damage_mod = 'str'
        self.ignore_dex = False ## False for everyone but rogue 
        self.abilities = ['dex', 'str', 'con', 'wis', 'int', 'chr']
        self.is_pally = False ## False for everyone but paladin
        self.crit_range = 20
        self.race = race
        self.race_health_increase = 1
        self.weapon_bonus = 0
        self.equiped_weapon = '' ## Empty strings false equivalent
        self.equiped_armor = '' 
        self.equiped_shield = ''
        self.klass = 'thing'
        self.race_target_weapon = ''
        self.race_wield_weapon = ''
        self.damage_received = 0
        if(self.race != 'human'):
            self.race_update()

    def equip_armor(self, armor):
        ## If there already is an equiped weapon un-equip it then continue
        if(self.equiped_armor):
            self.unequip_armor()
            ## For each attribute
        for attr in self.armor_list[armor]:
            ## If the attr shouldn't be added to the character
            if(attr == 'klass' or attr == 'race' or attr == 'negative'):
                continue
            ## To stop the attribute from being added to the character
            if(attr.__contains__('race_bonus')):
                continue
            ## Special case for race_wield and race_target
            if(attr.__contains__('race')):
                self.__setattr__(attr, self.armor_list[armor][attr])
            else:
                self.__setattr__(attr, self.__getattribute__(attr) + self.armor_list[armor][attr])
        self.equiped_armor = armor

    def unequip_armor(self):
        for attr in self.armor_list[self.equiped_armor]:
            if(attr == 'klass' or attr == 'race' or attr == 'negative'):
                continue
            if(attr.__contains__('race_bonus')):
                continue
            elif(attr.__contains__('race')):
                self.__setattr__(attr, '')
            else:
                self.__setattr__(attr, self.__getattribute__(attr) - self.armor_list[armor][attr])
        self.equiped_armor = ''

    def equip_weapon(self, weapon):
        ## If there already is an equiped weapon unequip it then continue
        if(self.equiped_weapon):
            self.unequip_weapon()
        ## For each attribute
        for attr in self.weapon_list[weapon]:
            ## For the attributes that shouldn't be added to the character
            if(attr == 'klass' or attr == 'race' or attr == 'negative'):
                continue
            ## Same as above if statement
            if(attr.__contains__('race_bonus')):
                continue
            ## For the race_target, race_wield, don't concatenates  the string
            if(attr.__contains__('race')):
                self.__setattr__(attr, self.weapon_list[weapon][attr])
            else:    
                self.__setattr__(attr, self.__getattribute__(attr) + self.weapon_list[weapon][attr])
        self.equiped_weapon = weapon  

    def unequip_weapon(self):
        ## For each attribute of the weapon
        for attr in self.weapon_list[self.equiped_weapon]:
            ## If the attr shouldn't be added to the character
            if(attr == 'klass' or attr == 'race' or attr == 'negative'):
                continue
            ## Broken up for readability, as above if statement
            if(attr.__contains__('race_bonus')):
                continue
            ## For the race_target and race_wield
            if(attr.__contains__('race')):
                self.__setattr__(attr, '')
            else: 
                self.__setattr__(attr, self.__getattribute__(attr) - self.weapon_list[self.equiped_weapon][attr])
        self.equiped_weapon = ''            

    def race_update(self):
        ## 100% of the time, random all the time
        if(self.race == 'chaos'):
            self.str = self.roll_dice(20)
            self.int = self.roll_dice(20)
            self.dex = self.roll_dice(20)
            self.wis = self.roll_dice(20)
            self.chr = self.roll_dice(20)
            self.con = self.roll_dice(20)
            self.ac = 10 + self.modifiers('dex')
            
        if(self.race == 'orc'):
            self.str += 4
            self.int -= 2
            self.chr -= 2
            self.wis -= 2
            self.ac += 2

        elif(self.race == 'dwarf'):
            self.con += 2
            self.chr -= 2
            self.race_health_increase = 2

        elif(self.race == 'elf'):
            self.dex += 2
            self.con -= 2
            self.crit_range = 19

        elif(self.race == 'halfling'):
            self.dex += 2
            self.str -= 2
            if(self.alignment.__contains__('evil') or self.alignment.__contains__('Evil')):
                self.alignment = self.alignment.replace('evil', 'neutral')
                self.alignment = self.alignment.replace('Evil', "Neutral")
        ## Updates the AC and health from race bonus
        self.update_character()

    ## Gets the ability score and does the math to calculate the bonus
    def modifiers(self, ability):
        return(getattr(self, ability) - 10 ) // 2
    ## Helper function to calculate hit chance
    def to_hit_bonus(self):
        return self.level // 2

    def weapon_bonus_help(self, enemy):
        if self.equiped_weapon == '':
            return 0
        race_target_weapon_match = False
        race_wield_weapon_match = False
        ## Checking if the klass can wield the weapon
        for attr in self.weapon_list[self.equiped_weapon]:
            if(attr == 'klass' and (self.weapon_list[self.equiped_weapon][attr] != self.klass)):
                return self.weapon_list[self.equiped_weapon]['negative']
        ## Checking if race weapon target is the enemy race
        if(hasattr(self, 'race_target_weapon')):
            if(self.race_target_weapon == enemy.race):
                race_target_weapon_match = True
        ## Checking if the correct race is wielding the weapon                
        if(hasattr(self, 'race_wield_weapon')):
            if(self.race_wield_weapon == self.race):
                race_wield_weapon_match = True
        ## If both the wield and target is the correct race 
        if(race_target_weapon_match and race_wield_weapon_match):
            return self.weapon_list[self.equiped_weapon]['race_bonus_double']
        ## If only one of the races matches the weapon    
        elif(race_target_weapon_match or race_wield_weapon_match):
            return self.weapon_list[self.equiped_weapon]['race_bonus']
        else:
            return 0

        pass
    ## Attack, checks the dice_roll against the enemy's AC. Sets to dead if health is equal to or lower than 0
    def attack(self, dice_roll, enemy):
        ac = enemy.ac + (enemy.modifiers('dex') if not self.ignore_dex else 0)
        smite = 0
        race_mod = 0
        weapon_race_mod = self.weapon_bonus_help(enemy)

        ## If paladin I need to smite evil
        if(self.is_pally):
            if(enemy.alignment.__contains__('Evil') or enemy.alignment.__contains__('evil')):
                smite = 2
                self.crit_mult = 3

        ##Race based attacking
        if(self.race == 'orc' and enemy.race == 'elf'):
            ac += 2

        ##Halfing on Halfing violence is a problem we need to stop 
        if(self.race != 'halfling' and enemy.race == 'halfling'):
            ac += 2

        ##checking race damage against orc from dwarfs
        if(self.race == 'dwarf'):
            if(enemy.race == 'orc'):
                race_mod = 2

        ## Damage is increased by stat associated modifier and hit bonus
        damage = self.modifiers(self.damage_mod) + (self.to_hit_bonus()) + smite + race_mod + weapon_race_mod + enemy.damage_received
        to_hit = damage + self.weapon_bonus
        ## If the extra damage will take away it resets to 0 
        if(damage < 0):
            damage = 0

        ## Critical Hit
        if(dice_roll >= self.crit_range):
            enemy.health -= (self.damage * 2 + (damage * self.crit_mult))
            self.gain_exp()
            if(enemy.health <= 0):
                enemy.is_alive = False
            return True
        ## If the dice roll isn't a crit but hits
        if((dice_roll + to_hit) >= ac):
            enemy.health -= (self.damage + damage)
            self.gain_exp()
            if(enemy.health <= 0):
                enemy.is_alive = False
            return True
            
        else:
            return False
    ## A Helper function to increase the stats by modifiers 
    def update_character(self):
        self.health = self.con + self.modifiers('con')
        self.ac = self.ac + self.modifiers('dex')
    ## Helper function to give exp to player and checks for level up
    def gain_exp(self):
        self.exp += 10
        if(self.exp >= (self.level * 1000)):
            self.level_up()
    ## Level up's the character and checks if the con mod is positive
    def level_up(self):
        self.level += 1
        if(self.con >= 10):
            self.health += self.health_increase + (self.modifiers('con') * self.race_health_increase)
        else:
            self.health += self.health_increase


# Iteration 2 below here
class Fighter(Character):
    def __init__(self, name, alignment, race = 'human'):
        super().__init__(name, alignment, race)
        self.health_increase = 10
        self.klass = 'fighter'
    ## Redefine to_hit_bonus to give proper bonus
    def to_hit_bonus(self):
        return self.level

class Rogue(Character):
    
    def __init__(self, name, alignment, race = 'human'):
        super().__init__(name, alignment, race)
        self.damage_mod = 'dex'
        self.crit_mult = self.crit_mult + 1
        self.ignore_dex = True
        ## Checking the alignment given and forces it to be neutral if good
        if self.alignment.__contains__('good') or self.alignment.__contains__('Good'):
            self.alignment = self.alignment.replace('Good', 'Neutral')
            self.alignment = self.alignment.replace('good', 'neutral')
        self.klass = 'rogue'

class Monk(Character):
    def __init__(self, name, alignment, race = 'human'):
        super().__init__(name, alignment, race)
        self.damage = 3
        if(self.wis > 11):
            self.ac = self.ac + self.modifiers('wis')
        self.health = self.health + self.modifiers('con')
        self.health_increase = 6
        self.klass = 'monk'

    def to_hit_bonus(self):
        bonus = self.level // 2
        bonus += self.level // 3
        return bonus

    def update_character(self):
        if(self.wis > 11):
            self.ac = self.ac + self.modifiers('wis')
        self.health = self.health + self.modifiers('con')

class Paladin(Character):
    def __init__(self, name, alignment, race = 'human'):
        super().__init__(name, 'Good', race)
        self.health_increase = 8
        self.is_pally = True
        self.klass = 'paladin'

    def to_hit_bonus(self):
        return self.level


