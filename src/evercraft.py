class Character(dict):
    def __init__(self):
        self = dict()
    # Our characters new init function, sets up the character and basic attributes
    def create(self, name, alignment):
        self['name'] = name;
        self['alignment'] = alignment
        self['ac'] = 10
        self['health'] = 5
        self['is_alive'] = True
        self['dex'] = 10
        self['str'] = 10
        self['con'] = 10
        self['wis'] = 10
        self['int'] = 10
        self['chr'] = 10
        self['abilities'] = ['dex', 'str', 'con', 'wis', 'int', 'chr']
    ## Gets the value from the provided key, basically the dot notation
    def get(self, key):
        return self[key]
    ## Sets the attribute to the give value or adds in that key pair value to dict
    def add(self, key, value):
        self[key] = value
    ## If there is value there already and want to update t
    def update(self, key, value):
        self[key] = self[key] + value

    def attack(self, dice_roll, enemy):
        if(dice_roll == 20):
            enemy.update('health', -2)
            if(enemy.get('health') <= 0):
                enemy.add('is_alive', False)
            return True
        if(dice_roll >= enemy['ac']):
            enemy.update('health', -1)
            if(enemy.get('health') <= 0):
                enemy.add('is_alive', False)
            return True
        else:
            return False
    def modifiers(self, ability):
        score = self[ability]
        return score
        

    pass