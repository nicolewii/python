# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 20:12:42 2021

@author: Nicole Lee
"""

'imports a math function used to help find the placement of the text within the box'
import math
'gets and prints inputs from user'
char = str(input('Enter frame character ==> '))
print(char)
height = input('Height of box ==> ')
print(height)
width = input('Width of box ==> ')
print(width)

'converts inputs into integers and strings'
height = int(height)
width = int(width)
sheight = str(height)
swidth = str(width)

'prints the box through finding the dimensions and spaces of the box, then calculates the correct placement of the text within the box using the spaces, printing the left side, text, then right side of the box'
print("\nBox:")
print((char*width +("\n"+char+" "*(width-2)+char)*((height-3)//2))+"\n"+char+(" "*((width-3-len(swidth)-len(sheight))//2))+swidth+"x"+sheight+(" "*math.ceil((width-3-len(swidth)-len(sheight))/2))+char+("\n"+char+" "*(width-2)+char)*math.ceil((height-3)/2)+("\n"+char*width))



