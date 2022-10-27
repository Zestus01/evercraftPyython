class Equipment():
    armor_list = {
    }
    weapon_list = {
        'longsword': {'damage': 4},
        'waraxe': {'damage': 7, 'weapon_bonus': + 2, 'crit_mult': + 1},
        'elven_longsword': {'damage': 5, 'weapon_bonus': 1, 'race_target': 'orc', 'race_wield': 'elf'},
        'nun_chucks': {'damage': 5, 'class': 'monk'},
    }
    misc_list = dict()


    def get_item(self, dictionary, item):
        return dictionary[item]

class Dice():
    twenty = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    twelve = [1,2,3,4,5,6,7,8,9,10,11,12]
    eight = [1,2,3,4,5,6,7,8]
    six = [1,2,3,4,5,6]
    four = [1,2,3,4]

    def roll_dice(self, die):
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
        self.damage = 1
        self.crit_mult = 2
        self.health_increase = 5
        self.damage_mod = 'str'
        self.ignore_dex = False
        self.abilities = ['dex', 'str', 'con', 'wis', 'int', 'chr']
        self.is_pally = False
        self.crit_range = 20
        self.race = race
        self.race_health = 1
        self.weapon_bonus = 0
        self.equiped_weapon = ''
        self.equiped_armor = ''
        self.klass = 'thing'
        if(self.race != 'human'):
            self.race_update()



    def equip_armor(self, armor):
        if(self.equiped_armor):
            self.unequip_armor(self.equiped_armor)
        for attr in self.armor_list[armor]:
            if(not hasattr(self,  attr)):
                self.__setattr__(attr, self.armor_list[armor][attr])
            else:
                self.__setattr__(attr, self.__getattribute__(attr) + self.armor_list[armor][attr])
        self.equiped_armor = armor

    def unequip_armor(self, armor):
        for attr in self.armor_list[armor]:
            self.__setattr__(attr, self.__getattribute__(attr) - self.armor_list[armor][attr])
        self.equiped_armor = ''


    def equip_weapon(self, equip):
        if(self.equiped_weapon):
            self.unequip_weapon(self.equiped_weapon)
        for attr in self.weapon_list[equip]:
            if(not hasattr(self,  attr)):
                self.__setattr__(attr, self.weapon_list[equip][attr])
            else:    
                self.__setattr__(attr, self.__getattribute__(attr) + self.weapon_list[equip][attr])
        self.equiped_weapon = equip  

    def unequip_weapon(self, equip):
        for attr in self.weapon_list[equip]:
            self.__setattr__(attr, self.__getattribute__(attr) - self.weapon_list[equip][attr])
        self.equiped_weapon = ''            

    def race_update(self):
        if(self.race == 'orc'):
            self.str += 4
            self.int -= 2
            self.chr -= 2
            self.wis -= 2
            self.ac += 2

        elif(self.race == 'dwarf'):
            self.con += 2
            self.chr -= 2
            self.race_health = 2

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


    ## Gets the ability score and does the math to calculate the bonus
    def modifiers(self, ability):
        return(getattr(self, ability) - 10 ) // 2
    ## Helper function to calculate hit chance
    def to_hit_bonus(self):
        return self.level // 2

    ## Attack, checks the dice_roll against the enemy's AC. Sets to dead if health is equal to or lower than 0
    def attack(self, dice_roll, enemy):
        ac = enemy.ac + (enemy.modifiers('dex') if not self.ignore_dex else 0)
        smite = 0
        race_mod = 0
        
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
        damage = self.modifiers(self.damage_mod) + (self.to_hit_bonus()) + smite + race_mod
        to_hit = damage + self.weapon_bonus
        ## If the extra damage will take away it resets to 0 
        if(damage < 0):
            damage = 0

        ## Critical Hit
        if(dice_roll >= self.crit_range):
            enemy.health -= (self.damage * 2 + (damage * self.crit_mult))
            self.crit_mult = 2
            self.gain_exp()
            if(enemy.health <= 0):
                enemy.is_alive = False
            return True

        if((dice_roll + to_hit) >= ac):
            enemy.health -= (self.damage + damage)
            self.gain_exp()
            if(enemy.health <= 0):
                enemy.is_alive = False
            return True
            
        else:
            return False

    def update_character(self):
        self.health = self.con + self.modifiers('con')

    def gain_exp(self):
        self.exp += 10
        if(self.exp >= (self.level * 1000)):
            self.level_up()

    def level_up(self):
        self.level += 1
        if(self.con >= 10):
            self.health += self.health_increase + (self.modifiers('con') * self.race_health)
        else:
            self.health += self.health_increase


# Iteration 2 bellow here


class Fighter(Character):
    def __init__(self, name, alignment, race = 'human'):
        super().__init__(name, alignment, race)
        self.health_increase = 10
        self.klass = 'fighter'
    
    def to_hit_bonus(self):
        return self.level

class Rogue(Character):
    
    def __init__(self, name, alignment, race = 'human'):
        super().__init__(name, alignment, race)
        self.damage_mod = 'dex'
        self.crit_mult = self.crit_mult + 1
        self.ignore_dex = True
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


