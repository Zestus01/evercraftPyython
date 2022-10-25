from pprint import pprint
# pprint(dir(dict))

class Example:
    def __init__(self):
        self.fun = 'Hello'
        self.attr = 'Attriubute'
        self.dex = 10
    def print_atr(self, name):
        print(getattr(self, name))
    def change(self, attr, value):
        setattr(self, name, value)
# print('======================')

# pprint(dir(Example()))
test = Example()

test.print_atr('attr')
test.print_atr('dex')
test.print_atr('fun')
