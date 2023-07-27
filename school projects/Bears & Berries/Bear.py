# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 12:02:26 2021

@author: leen8
"""
class Bear:
    #initalizes variables from the dictionary of data, takes in the coordinates
    # of the bear and its direction
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        #sets turns to 0, since there is no condition where it needs to wait turns
        # from sleeping or killing yet
        self.turns = 0
        #bear also did not eat anything yet so, it is set to 0 
        self.eat = 0
        #the bear did not leave, kill, or need to sleep yet, so all are set to false
        self.left = False
        self.kill = False
        self.sleep = False
    #sends back the output of where the bear is at a given point and direction
    def __str__(self):
        output = "Bear at ({},{}) moving {}".format(str(self.x),str(self.y),self.d)
        return output
    #function moves the bear on the grid based on the direction given from the 
    # data of bears
    def move(self):
            if self.d == "N":
                self.x -= 1
            elif self.d == "NE":
                self.x -= 1
                self.y += 1
            elif self.d == "NW":
                self.x-= 1
                self.y-= 1
            elif self.d == "S":
                self.x += 1
            elif self.d == "SE":
                self.x += 1   
                self.y += 1
            elif self.d == "SW":
                self.x += 1
                self.y-= 1
            elif self.d == "E":
                self.y += 1
            elif self.d == "W":
                self.y -= 1  
            
