class Character():

    def __init__(self, name, alignment):
        self.name = name
        self.alignment = alignment
        self.ac = 10
        self.health = 5
        self.is_alive = True
        self.dex = 10
        self.str = 10
        self.wis = 10
        self.chr = 10
        self.con = 10
        self.int = 10
        self.abilities = ['dex', 'str', 'con', 'wis', 'int', 'chr']
    ## Attack, checks the dice_roll against the enemy's AC. Sets to dead if health is equal to or lower than 0
    def attack(self, dice_roll, enemy):
        if(dice_roll == 20):
            enemy.health -= 2
            if(enemy.health <= 0):
                enemy.is_alive = False
            return True

        if(dice_roll >= enemy.ac):
            enemy.health -= 1
            if(enemy.health <= 0):
                enemy.is_alive = False
            return True
            
        else:
            return False

    def modifiers(self, ability):
        return(getattr(self, ability) - 10 ) // 2
