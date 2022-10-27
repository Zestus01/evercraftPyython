class Character():

    def __init__(self, name, alignment):
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

    def modifiers(self, ability):
        return(getattr(self, ability) - 10 ) // 2

    def to_hit_bonus(self):
        return self.level // 2
    

    ## Attack, checks the dice_roll against the enemy's AC. Sets to dead if health is equal to or lower than 0
    def attack(self, dice_roll, enemy):
        ac = enemy.ac + (enemy.modifiers('dex') if not self.ignore_dex else 0)
        smite = 0
        if(self.is_pally):
            if(enemy.alignment.__contains__('Evil') or enemy.alignment.__contains__('evil')):
                smite = 2
                self.crit_mult = 3
        damage = self.modifiers(self.damage_mod) + (self.to_hit_bonus()) + smite
        to_hit = damage 
        if(damage < 0):
            damage = 0
        if(dice_roll == 20):
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
            self.health += self.health_increase + self.modifiers('con')
        else:
            self.health += self.health_increase


# Iteration 2 bellow here


class Fighter(Character):
    def __init__(self, name, alignment):
        Character.__init__(self, name, alignment)
        self.health_increase = 10
    
    def to_hit_bonus(self):
        return self.level



class Rogue(Character):
    
    def __init__(self, name, alignment):
        if alignment == 'good' or alignment == 'Good':
            alignment = 'neutral' 
        Character.__init__(self, name, alignment)
        self.damage_mod = 'dex'
        self.crit_mult = 3
        self.ignore_dex = True

class Monk(Character):
    def __init__(self, name, alignment):
        Character.__init__(self, name, alignment)
        self.damage = 3
        if(self.wis > 11):
            self.ac = self.ac + self.modifiers('wis')
        self.health = self.health + self.modifiers('con')
        self.health_increase = 6

    def to_hit_bonus(self):
        bonus = self.level // 2
        bonus += self.level // 3
        return bonus

    def update_character(self):
        if(self.wis > 11):
            self.ac = self.ac + self.modifiers('wis')
        self.health = self.health + self.modifiers('con')
    


class Paladin(Character):
    def __init__(self, name, alignment):
        Character.__init__(self, name, 'Good')
        self.health_increase = 8
        self.is_pally = True

    def to_hit_bonus(self):
        return self.level

    # def attack(self, dice_roll, enemy):
    #     ac = (enemy.ac + enemy.modifiers('dex'))
    #     smite = 0
    #     if(enemy.alignment.__contains__('Evil') or enemy.alignment.__contains__('evil')):
    #         smite = 2
    #     damage = self.modifiers('str') + (self.level // 2) + smite
    #     to_hit = damage + (self.level // 2)
    #     if(damage < 0):
    #         damage = 0 
    #     if(dice_roll == 20):
    #         enemy.health -= (2 + (damage * 3))
    #         self.gain_exp()
    #         if(enemy.health <= 0):
    #             enemy.is_alive = False
    #         return True

    #     if((dice_roll + to_hit) >= ac):
    #         enemy.health -= (1 + damage)
    #         self.gain_exp()
    #         if(enemy.health <= 0):
    #             enemy.is_alive = False
    #         return True
            
    #     else:
    #         return False

# start of Iteration 3 bellow




