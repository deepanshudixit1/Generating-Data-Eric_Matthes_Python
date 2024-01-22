from random import randint

class Die:
    #class representing single die
    def __init__(self,num_sides=6):
        #assume six sided die
        self.num_sides=num_sides
        
    def roll(self):
        #return random value between 1 and numbber of sides
        return randint(1,self.num_sides)