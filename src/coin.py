import random

class Coin:
    
    def __init__(self):
        self.states = ['H', 'T']

    def flip(self):
        #return self.states[random.randrange(0,2)]
        return random.choice(self.states)

