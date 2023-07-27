# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 14:03:14 2021

@author: leen8
"""
class BerryField:
    #initalizes the berry field, by taking in the list of the list of grid, list of tourists created
    # in the main code, and the list of bears created in the main code from calling the Bear and 
    # Tourist classes and sets them to variables in the class
    def __init__(self, grid, tourists, bears):
        self.g = grid
        self.b = bears
        self.t = tourists
    #returns the completed grid based on the grid, tourist, and bear data  
    def __str__(self):
        #sets the grid to a string to it creates the grid as a string
        # and allows it to be appended and added with other strings
        grid = ''
        #sets the bear, tourist, or both (aka X) locations to false, so if there are
        # none, it just prints the grid with no B, T, or X
        B = False
        T = False
        X = False
        #gets the length of the rows of the grid:
        l = (len(self.g))
        # a nested for loop to determine if the coordinates of bears and tourists are 
        # the same within the grid
        for x in range(l):
            for y in range(l):
                for b in self.b:
                    for t in self.t:
                        # if the x and y coordinates of the bear and the tourist are the same, it makes the
                        # coordinate an X instead of a value, also sets X to true, since it is
                        # true for that location, and will be overriden by a B, T, or number
                          if b.x == x and t.x == x and b.y == y and t.y == y:
                            grid += ("{:>4}".format("X"))
                            X = True
                #if there is no X in the location, it goes through the bear or tourist list and finds its coordinates
                # so it can place either a B or T in that location (since both are not in the same location as
                # determined above.
                if X == False:
                    for b in self.b:
                        #if the coordinates of the bear equals the coordinates on the grid,
                        # it replaces that value with a B to indicate there is a bear there
                        # and sets B to True, so it won't be overriden by another value
                        if b.x == x and b.y == y:
                            grid += ("{:>4}".format("B"))                                                                                                                                                                                     
                            B = True
                        # if the coordinates of the tourist equals the coordinates on the grid, 
                        # it replaces that value with a T to indicate there is a tourist on the 
                        # grid, and sets T to true, so it won't be overiden by another value
                    for t in self.t:
                        if t.x == x and t.y == y:
                            grid += ("{:>4}".format("T"))
                            T = True
                # however, if neither both, a bear, or a tourist, is at that given location
                # it puts the value from the grid in that location
                if B == False and T == False and X == False:
                    grid += ("{:>4}".format(self.g[x][y]))
                # resets the X. B, and T locations back to false, so it can check the next
                # value in the grid list so it doesn't only print the first instance of a 
                # bear, tourist, or both in the locations on the grid
                X = False
                B = False
                T = False
            #prints a new line after each row of the grid has been created from the loops above
            grid += "\n"
        #then, finally returns the final grid
        return grid
    #returns total number of berries
    def total(self):
        #creates a all berries variable
        allb = 0
        #loops through the grid at each row sums it and adds it to the all berries variable, then returns 
        # its value
        for x in self.g:
            allb += sum(x)
        return allb
    #grows all the berries in the grid each time
    def grow(self):
        #goes through the grid at each value and only grows the berries (by incrimenting it by 1) if they are 
        # greater than or equal to 0 or less than 10
        for x in range(len(self.g)):
            for y in range(len(self.g)):
                if (self.g[x][y] >= 1 and self.g[x][y] < 10):
                    self.g[x][y] += 1
    
    #spreads the berries in the grid
    def spread(self):
        for x in range(len(self.g)):
            for y in range(len(self.g)):
                #if the coordinate is equal to 10 berries, it changes the berries around it
                if self.g[x][y] == 10:
                    #creates variables of the boundary of the grid, the row up and down from the coordinate
                    # and the column to the right and left of the coordinate
                    lgrid = len(self.g[x])-1
                    xup = x+1
                    xdown = x-1
                    yup = y+1
                    ydown = y-1
                    #if the row or column is not at the end of the grid nor the row or column is at the top left of the
                    # grid, the sets the coordinates around it equal to 1
                    if x != lgrid and  y != lgrid and x != 0 and y != 0:
                        #sets all the coordinates all around it to be set to 1 
                        
                        #on the x row
                        if (self.g[x][yup] == 0):
                            self.g[x][yup] = 1
                        if (self.g[x][ydown] == 0):
                            self.g[x][ydown] = 1
                        #on the y column
                        if (self.g[xup][y] == 0):
                            self.g[xup][y] = 1
                        if (self.g[xdown][y] == 0):
                            self.g[xdown][y] = 1
                        #on the row above x
                        if (self.g[xup][yup] == 0):
                            self.g[xup][yup] = 1
                        if (self.g[xup][ydown] == 0):
                            self.g[xup][ydown] = 1
                        #on th row below x
                        if (self.g[xdown][yup] == 0):
                            self.g[xdown][yup] = 1
                        if (self.g[xdown][ydown] == 0):
                            self.g[xdown][ydown] = 1
                    # if the row is on the edge of the top, it only changes the value to 1 
                    # around it, no xdown coordinate exists because its at the edge and can't decrease past the grid
                    if (x == 0 and x != lgrid and y != 0):
                        if (self.g[x][yup] == 0):
                            self.g[x][yup] = 1
                        if (self.g[x][ydown] == 0):
                            self.g[x][ydown] = 1
                        if (self.g[xup][yup] == 0):
                            self.g[xup][yup] = 1
                        if (self.g[xup][ydown] == 0):
                            self.g[xup][ydown] = 1
                        if (self.g[xup][ydown] == 0):
                            self.g[xup][ydown] = 1
                    # if row is on the edge on the bottom, it only changes the value to 1
                    # around it, no xup coordinate because its at the edge and can't increase past the grid
                    if (x == lgrid and y != lgrid and y != 0):
                        if (self.g[xdown][y] == 0):
                            self.g[xdown][y] = 1
                        if (self.g[x][yup] == 0):
                            self.g[x][yup] = 1
                        if (self.g[x][ydown] == 0):
                            self.g[x][ydown] = 1
                        if (self.g[xdown][yup] == 0):
                            self.g[xdown][yup] = 1
                        if (self.g[xdown][ydown] == 0):
                            self.g[xdown][ydown] = 1
                    # if the column is on the edge of the left, it only changes the value to 1 
                    # around it, no ydown coordinate exists because its at the edge and can't decrease past the grid
                    if (y == 0 and x != lgrid and x != 0):
                         if (self.g[xup][y] == 0):
                             self.g[xup][y] = 1
                         if (self.g[xdown][y] == 0):
                             self.g[xdown][y] = 1
                         if (self.g[x][yup] == 0):
                             self.g[x][yup] = 1
                         if (self.g[xdown][yup] == 0):
                             self.g[xdown][yup] = 1
                         if (self.g[xup][yup] == 0):
                             self.g[xup][yup] = 1
                    # if column is on the edge on the right side, it only changes the value to 1
                    # around it, no yup coordinate because its at the edge and can't increase past the grid
                    if (y == lgrid and x != lgrid and x != 0):
                        if (self.g[xup][y] == 0):
                            self.g[xup][y] = 1
                        if (self.g[xdown][y] == 0):
                            self.g[xdown][y] = 1
                        if (self.g[x][ydown] == 0):
                            self.g[x][ydown] = 1
                        if (self.g[xup][ydown] == 0):
                            self.g[xup][ydown] = 1
                        if (self.g[xdown][ydown] == 0):
                            self.g[xdown][ydown] = 1  
                    #if coordinate is at the top left, it only changes the values to 1 
                    # to the values around it, no xdown or ydown exist because the grid would be
                    # out of range
                    if (x==0 and y==0):
                        if (self.g[xup][y] == 0):
                            self.g[xup][y] = 1
                        if (self.g[x][yup] == 0):
                            self.g[x][yup] = 1
                        if (self.g[xup][yup] == 0):
                            self.g[xup][yup] = 1
                    #if coordinate is at the bottom right, it only changes the values to 1 
                    # to the values around it, no xup or yup exist because the grid would be
                    # out of range
                    if (x == lgrid and y == lgrid):
                        if (self.g[xdown][y] == 0):
                            self.g[xdown][y] = 1
                        if (self.g[x][ydown] == 0):
                            self.g[x][ydown] = 1
                    #if coordinate is at the top right, it only changes the values to 1 
                    # to the values around it, no xdown or yup exist because the grid would be
                    # out of range
                    if (x == 0 and y == lgrid):
                        if (self.g[xup][y] == 0):
                            self.g[xup][y] = 1
                        if (self.g[x][ydown] == 0):
                            self.g[x][ydown] = 1
                        if (self.g[xup][ydown] == 0):
                            self.g[xup][ydown] = 1  
                    #if coordinate is at the bottom left, it only changes the values to 1 
                    # to the values around it, no xup or ydown exist because the grid would be
                    # out of range
                    if (x == lgrid and y == 0):
                        if (self.g[xdown][y] == 0):
                            self.g[xdown][y] = 1
                        if (self.g[x][yup] == 0):
                            self.g[x][yup] = 1
                        if (self.g[xdown][yup] == 0):
                            self.g[xdown][yup] = 1

