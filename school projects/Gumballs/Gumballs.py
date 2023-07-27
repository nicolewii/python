# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 15:33:26 2021

@author: Nicole Lee
"""
'imports math and creates pi variable'
import math
pi = math.pi

'creates functions that calculates the volume of a sphere and a cube'
def find_volume_sphere(radius):
    return (4/3)*pi*(radius**3)
def find_volume_cube(side):
    return side**3

'gets the radius and weekly sales from the user'
rad = input("Enter the gum ball radius (in.) => ")
print(rad)
weeksale = input("Enter the weekly sales => ")
print(weeksale)

'converts inputs into floats for calculations'
rad = float(rad)
weeksale = float(weeksale)

if(rad == 0 and weeksale == 0):
    print("\nThe machine needs to hold 0 gum balls along each edge.\nTotal edge length is 0.00 inches.\nTarget sales were 0, but the machine will hold 0 extra gum balls. \nWasted space is 0.00 cubic inches with the target number of gum balls, \nor 0.00 cubic inches if you fill up the machine.")
else:
    'calculates the amount of gumballs that fit, target sales, edge length, extra gumballs, wasted space and filled space'
    gfit = weeksale*1.25
    gside = weeksale/(rad*2)
    ghold = math.ceil(gfit**(1/3))
    targsale = math.ceil(weeksale*1.25)
    gextra = (ghold**3) - targsale 
    gmax  = ghold**3
    edgeleng = (rad*2)*ghold
    wastedsp = find_volume_cube(edgeleng)-(targsale*find_volume_sphere(rad))
    nfilled = find_volume_cube(edgeleng)-(gmax*find_volume_sphere(rad))
    
    'prints the calculations'
    print("\nThe machine needs to hold {} gum balls along each edge.".format(ghold))
    print("Total edge length is {:.2f} inches.".format(edgeleng))
    print("Target sales were {}, but the machine will hold {} extra gum balls.".format(targsale, gextra))
    print("Wasted space is {:.2f} cubic inches with the target number of gum balls,\nor {:.2f} cubic inches if you fill up the machine.".format(wastedsp, nfilled))

