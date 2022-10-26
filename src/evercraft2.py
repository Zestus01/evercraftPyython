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
        self.health = 5 + self.modifiers('con')
        self.abilities = ['dex', 'str', 'con', 'wis', 'int', 'chr']

    def modifiers(self, ability):
        return(getattr(self, ability) - 10 ) // 2

    ## Attack, checks the dice_roll against the enemy's AC. Sets to dead if health is equal to or lower than 0
    def attack(self, dice_roll, enemy):
        ac = (enemy.ac + enemy.modifiers('dex'))
        damage = self.modifiers('str') + (self.level // 2)
        to_hit = damage
        if(damage < 0):
            damage = 0
        if(dice_roll == 20):
            enemy.health -= (2 + (damage * 2))
            self.gain_exp()
            if(enemy.health <= 0):
                enemy.is_alive = False
            return True

        if((dice_roll + to_hit) >= ac):
            enemy.health -= (1 + damage)
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
            self.health += 5 + self.modifiers('con')
        else:
            self.health += 5


# Iteration 2 bellow here


class Fighter(Character):
    def __init__(self, name, alignment):
        Character.__init__(self, name, alignment)
        
    def attack(self, dice_roll, enemy):
        ac = (enemy.ac + enemy.modifiers('dex'))
        damage = self.modifiers('str') + (self.level // 2)
        to_hit = damage + self.level
        if(damage < 0):
            damage = 0
        if(dice_roll == 20):
            enemy.health -= (2 + (damage * 2))
            self.gain_exp()
            if(enemy.health <= 0):
                enemy.is_alive = False
            return True

        if((dice_roll + to_hit) >= ac):
            enemy.health -= (1 + damage)
            self.gain_exp()
            if(enemy.health <= 0):
                enemy.is_alive = False
            return True
            
        else:
            return False
    
    def level_up(self):
        self.level += 1
        if(self.con >= 10):
            self.health += 10 + self.modifiers('con')
        else:
            self.health += 10


class Rogue(Character):
    def __init__(self, name, alignment):
        if alignment == 'good' or alignment == 'Good':
            alignment = 'neutral' 
        Character.__init__(self, name, alignment)

    def attack(self, dice_roll, enemy):
        ac = enemy.ac 
        damage = self.modifiers('dex') + (self.level // 2)
        to_hit = damage
        if(damage < 0):
            damage = 0
        if(dice_roll == 20):
            enemy.health -= (2 + (damage * 3))
            self.gain_exp()
            if(enemy.health <= 0):
                enemy.is_alive = False
            return True

        if((dice_roll + to_hit) >= ac):
            enemy.health -= (1 + damage)
            self.gain_exp()
            if(enemy.health <= 0):
                enemy.is_alive = False
            return True
            
        else:
            return False

class Monk(Character):
    def __init__(self, name, alignment):
        Character.__init__(self, name, alignment)

    def update_character(self):
        self.ac = self.wis + self.modifiers('wis')
        self.health = self.con + self.modifiers('con')