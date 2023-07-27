# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 16:14:51 2021

@author: leen8
"""
class Tourist:
    #initalizes the elements of the tourist to the class
    def __init__(self,x,y):
        # sets the coordinates to class variables
        self.x = x
        self.y = y
        # sets turns to 0 because the tourist has taken 0 turns at the current time
        self.turns = 0
        # since the tourists havent died, gotten scared or bored, and therefore left yet, all of the values are set to False
        self.die = False
        self.scared = False
        self.left = False
        self.bored = False
    #returns the ouput of the location of the tourist and how many turns it has taken
    def __str__(self):
        output = "Tourist at ({},{}), {} turns without seeing a bear.".format(str(self.x),str(self.y),str(self.turns))               
        return output
    # if the tourist sees the bear, it returns the value of how many times its seen the bear within the range of the grid
    def see(self, bears):
        #creates a counter variable
        c = 0
        # determines how close the tourist is to the bear based on the coordinaetes of the bear and the tourist
        for b in bears:
            #D^2 = X^2+Y^2 is the distance formula used to find the distance between the two points
            x = abs(b.x - self.x)
            y = abs(b.y - self.y)
            #squares the x and the y and then takes the square root to see if the distance
            # between the two coordinates is less than or equal to 4, if so, it adds the counter 
            # of how many times they've seen it. 
            squarex = x**2
            squarey = y**2
            if (squarex + squarey)**.5 <= 4:
                c += 1
        return c
