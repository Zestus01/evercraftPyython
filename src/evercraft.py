class Character(dict):
    def __init__(self):
        self = dict()
    def create(self, name, alignment):
        self['name'] = name;
        self['alignment'] = alignment
        self['armor'] = 10
        self['health'] = 5
        self['is_alive'] = True
        self['dex'] = 10
        self['str'] = 10
        self['con'] = 10
        self['wis'] = 10
        self['int'] = 10
        self['chr'] = 10
    def get(self, key):
        return self[key]
    def add(self, key, value):
        self[key] = value
    def attack(self, dice_roll, enemy):
        if(dice_roll == 20):
            enemy['health'] -= 2
            if(enemy['health'] <= 0):
                enemy['is_alive'] = False
            return True
        if(dice_roll >= enemy['armor']):
            enemy['health'] -= 1
            if(enemy['health'] <= 0):
                enemy['is_alive'] = False
            return True
        else:
            return False
    def modifiers(self, ability):
        score = self[ability]
        return score
        

    pass