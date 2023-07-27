# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 16:07:04 2021

@author: leen8
"""
#imports json, BerryField file & class created, Bear file & class created, 
# & Tourist file & class created
import json
import BerryField
import Bear
import Tourist

#ensures the json file is a valid input and takes the input from the user
if __name__ == "__main__":
    jfile = input("Enter the json file name for the simulation => ")
    print(jfile)
#opens the json file and reads the file and changes the file into a valid 
#dictionary using the json module
f = open(jfile)
data = json.loads(f.read())
#gets the data/lists of the berry field, active and reserve bears, and active
# and reserve tourists from the dictionary of data in the json file
berryf = (data["berry_field"])
abears = (data["active_bears"])
rbears =(data["reserve_bears"])
atour = (data["active_tourists"])
rtour = (data["reserve_tourists"])

#creates a list of bears from using the bear module created in Bear.py, sending in the coordinates and direction of the bear
# from the list of lists in the "active_bears" item in the dictionary and appending them to the list
bearl =[]
for bd in abears:
    bearl.append(Bear.Bear(bd[0],bd[1],bd[2]))
#creates a list of the reserve bears by taking the bears from the reserve bears data, 
# sending them into the Bears class to create the bear 
rbearl=[]
for rbd in rbears:
    rbearl.append(Bear.Bear(rbd[0],rbd[1],rbd[2]))
#creates a list of tourists from using the bear module created in Tourists.py, sending in the coordinates of the tourist
# from the list of lists in the "active_tourists" item in the dictionary and appending them to the list
tourl = []
for td in atour:
    tourl.append(Tourist.Tourist(td[0],td[1]))
rtourl= []
for rtd in rtour:
    rtourl.append(Tourist.Tourist(rtd[0],rtd[1]))
    
print("\nStarting Configuration")   
#creates the berry field from the BerryField class by sending in the list of lists
# of the berry field, the list of active tourists, and list of active bears 
bf = BerryField.BerryField(berryf,tourl,bearl)

#prints the total number of berries from the grid by using the total berries function from the BerryField class
# and prints the grid
print("Field has {} berries.".format(bf.total()))
print(bf)

#prints the active bears in te field with their coordinates and direction from the list of bears created above
print("Active Bears:")
for b in bearl:
    print(b)

#prints the active tourists in te field with their coordinates number of turns from the list of tourists created above
print("\nActive Tourists:")
for t in tourl:
    print(t)

#creates a turn counter variable 
turn = 1

#creates a loop that loops until the turns are done
while True:
    #prints what turn we are on within the loop
    if turn == 1:
        print("\nTurn: {}".format(turn))
    else:
        print("\n\nTurn: {}".format(turn))
    #grows and spreads berries by using the functions from the BerryField class
    bf.grow()
    bf.spread()
    
    #determines if the bear or tourist are in the same spot from the coordinates
    # of the list of tourists and bears, if so:
    for b in bearl:
         for t in tourl:
             if  b.x == t.x and b.y == t.y:
                 #if they are in the same location, the tourist dies, and the
                 # bear gains a kill
                 t.die = True
                 b.kill = True
   
    #creats counter variable to keep track of how many tourists left the field
    ct = 0
    #checks in the list of tourists if they die from a bear or get scared from the bear
    # they leave the field on this turn and increases the number of tourists that left the field
    for t in range(len(tourl)):
        #creates a variable that gets the tourist from the list in the field
        tfield = tourl[t-ct]
        if tfield.die == True or tfield.scared == True:
            print("{} - Left the Field".format(tfield))
            tourl.remove(tfield)
            ct += 1
    #changes the movement of the bears in the list of 
    # bears based on certain conditions that occur
    for b in bearl:
        #if the bear got a kill it sleeps for 4 turns, then resets the kill to false, so it doesn't only apply to one bear
        if b.kill == True:
            b.sleep = True
            b.turns = 4
            b.kill = False
        #if bear is asleep it stays asleep until its turns go to 0, so it decreases on each turn
        if b.sleep == True:
            b.turns -= 1
        #when the bear's turns goes to 0, it's no longer asleep
        if b.turns == 0:
            b.sleep = False
        #if the bear wakes up and hasn't left the field yet, it keeps moving. 
        if b.sleep == False and b.left == False:
            while True:
                #the bear eats all the berries at the certain coordinate it adds how many it's eaten to the bear, 
                # then changes its value to 0 because the bear has eaten everything
                b.eat += bf.g[b.x][b.y]
                bf.g[b.x][b.y] = 0
                #then it moves the bear after it's eaten all of the berries
                b.move()
                
                #checks if the tourist gets eaten when the bear moves into a tourist, causing the tourist to die
                # and if the bear to die at that coordinate
                for t in tourl:
                    if  b.x == t.x  and b.y == t.y:
                        t.die = True
                        b.kill = True 
                #if the bear has a kill it breaks from the loop of moving the bear 
                # and goes back to checking its kill and turn conditions 
                if b.kill == True:
                    break
                #if the bear leaves, it sets that it left value to true and breaks from the loop
                #left at the bottom of the grid
                if b.x > len(bf.g)-1:
                    b.left = True
                    break
                #left at the top of the grid
                elif b.x < 0:
                    b.left = True   
                    break
                #left at the right side of the grid
                elif b.y > len(bf.g)-1:
                    b.left = True
                    break
                #left at the left side of the grid
                elif b.y < 0:
                    b.left = True
                    break
                #if the bear didn't leave, it continues to eat all the berries, leaving spaces at 0
                b.eat += bf.g[b.x][b.y]
                bf.g[b.x][b.y] = 0
                # if the bear eats more than 30 berries, then it stops eating and moving, and leaves the remaining berries
                # on the grid. 
                if b.eat >= 30:
                    bf.g[b.x][b.y] = b.eat - 30
                    break
        #resets what the bears have eaten for the next turn
        b.eat = 0
    
    
    # if the bear goes to the same location as the tourist, it kills the tourist, and the tourist dies and the bear gains a kill
    for b in bearl:
         for t in tourl:
             if  b.x == t.x  and b.y == t.y:
                 t.die = True
                 b.kill = True
    # loop that checks the status of the tourists                 
    for t in tourl:
        # if the tourist is alive, it checks its surroundings for a bear
        if t.die == False:
            #if the tourist sees the bear 3 or more times, the tourist flees
            if t.see(bearl) >= 3:
                t.scared = True
            #if the tourist sees the bear, it changes its turns to 0, because it saw a bear
            if t.see(bearl) > 0:
                t.turns = 0
            #if the tourist doesn't see the bear, it adds a turn of how many times they have not seen a bear
            if t.see(bearl) == 0:
                t.turns += 1
        # if the tourist doesn't see a bear for 3 turns, it gets bored and leaves 
        if t.turns == 3:
            t.bored = True
         #if the tourist sees the bear 3 or more times, the tourist flees
        if t.see(bearl) >= 3:
            t.scared = True
    #if bear gets a kiil it goes to sleep for three turns and restarts the bear, so it is possible for the bear to kill
    # again         
    for b in bearl:
        if b.kill == True:
            b.sleep = True
            b.turns = 3
            b.kill = False
    #creates a counter variable to count how many bears have left the field
    cb = 0 
    for b in range(len(bearl)):
        #creates a variable that gets the bear from the list in the field
        bfield = bearl[b-cb]
        #if the bear left, print that it left the field, and remove it from the active bears list
        # and incriment that a bear has left
        if bfield.left == True:
            print("{} - Left the Field".format(bfield))
            bearl.remove(bfield)
            cb +=1
    #creates a counter variable to count how many tourists have left the field
    ct = 0
    for t in range(len(tourl)):
        #creates a variable that gets the tourist from the list in the field
        tfield = tourl[t-ct]
        # if the tourist dies, gets scared, or gets bored, it leaves the field, it prints 
        # that a tourist left then removes them  from the active tourist list and incriment 
        # that a tourist has left
        if tfield.die == True or tfield.scared == True or tfield.bored == True:
            print("{} - Left the Field".format(tfield))
            tourl.remove(tfield)
            ct += 1
    #takes the bear from the reserve bear list and if there are more than 500 berries left, 
    # it adds the reserve bear to the active bear list, and removes it from the reserve bear list
    lenreserve = len(rbearl)
    if lenreserve > 0 and bf.total() > 500:
        bearl.append(rbearl[0])
        rbearl.remove(rbearl[0])
        #also prints that the reserve bear has entered the field 
        print(("{} - Entered the Field".format(bearl[-1]))) #-1 because it is the latest bear appended to the active bear list
    # if there is at least one active bear and at least one reserve tourist in the list, then it
    # adds the tourist to the active tourist list
    lenactive = len(bearl)
   
    if len(rtourl)>0 and lenactive > 0:
        tourl.append(rtourl[0])
        rtourl.remove(rtourl[0])
        #also prints that the tourist has entered the field
        print(("{} - Entered the Field".format(tourl[-1]))) #-1 because it is the latest tourist appended to the active tourist list
    #prints the updated grid, total berries, active or asleep bears, and active tourists every 5 turns
    if turn % 5 == 0:
        print("Field has {} berries.".format(bf.total()))
        print(bf)
        print("Active Bears:")
        for b in bearl: 
            if b.sleep == True and b.turns -1 >0:
                print("{} - Asleep for {} more turns".format(b,(b.turns-1)))
            else:
                print(b)
        print("\nActive Tourists:")
        for tourist in range(len(tourl)):
            print(tourl[tourist])   
    #incriments the turn
    turn += 1
    #if there are no more active or reserve bears left, the simulation ends at the remaining turn
    if lenactive == 0 and lenreserve == 0:
        break
#prints the final grid after all of bears have left the field
print("\nField has {} berries.".format(bf.total()))
print(bf)
print("Active Bears:")
for b in bearl: 
    if b.sleep == True and b.turns -1 >0:
        print("{} - Asleep for {} more turns".format(b,(b.turns-1)))
    else:
        print(b)
print("\nActive Tourists:")
for t in tourl:
    print(t)   



