# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 10:17:22 2021

@author: leen8
"""
#function that gets and parses all the words in a file, taking out the special characters and digits
def get_words(file):
    s = open(file, encoding="UTF-8").read().strip().lower()
    ns = ' '.join(s.split())
    punct = '''!()-—[]{};:'"\,<>./?@#$%^&’*_~â€™”1234567890'''
    for x in ns:
        if x in punct or x == '':
            ns = ns.replace(x, "") 
    ns2 = ns.split(" ")
    for y in ns2:
        if y == '—':
            ns2.remove(y)
        if y == '':
            ns2.remove(y)
    #creates the stop.txt file into a list
    f = open("stop.txt").read().strip().lower()
    stopl = f
    for x in stopl:
        if x in punct or x == '':
            stopl = stopl.replace(x, "")
    stopl2 = stopl.replace("\t", "\n").split("\n")
    unique = []
    for x in ns2:
        if x not in stopl2:
            unique.append(x)
    return unique
#funation that gets the unique pairs of the words by working backwords from
# the max step and adding each tuple to a list, sorting them and changing it back into a tuple 
#  since sorted makes it a list
def get_pairs(wlist, sep):
    maxsep = sep
    tuples=[]
    while maxsep > 0:
        for x in range(len(wlist)-sep):
            if(x != len(wlist)-sep):
                w1 = wlist[x]
                w2 = wlist[x+maxsep]
                wtuple = ((w1, w2))
                tsort = sorted(wtuple)
                swtuple = tuple(tsort)
                tuples.append(swtuple)
        maxsep -= 1
    #compares the second to last and last value so that it ensures that the
    # last value can be added to the list of distinct pair
    if(wlist[len(wlist)-sep]<=wlist[len(wlist)-1]):
        tuples.append((wlist[len(wlist)-sep], wlist[len(wlist)-1]))
    elif(wlist[len(wlist)-sep]>=wlist[len(wlist)-1]):
        tuples.append((wlist[len(wlist)-1],wlist[len(wlist)-sep]))
    #since the tuples are in reverse, use the sort function to sort it back
    # in the right order and makes  making them a set to take out 
    #  duplicates
    tuples.sort(reverse = True)
    tuples = set(tuples)
    return tuples
#gets all the pairs of words, not putting them into a set in order to 
# keep the duplicates, but still sorts the tuple and list
def get_all_pairs(wlist, sep):
    maxsep = sep
    tuples=[]
    while maxsep > 0:
        for x in range(len(wlist)-sep):
            if(x != len(wlist)-sep):
                w1 = wlist[x]
                w2 = wlist[x+maxsep]
                wtuple = ((w1, w2))
                tsort = sorted(wtuple)
                swtuple = tuple(tsort)
                tuples.append(swtuple)
        maxsep -= 1
    #compares the second to last and last value so that it ensures that the
    # last value can be added to the list of distinct pair
    if(wlist[len(wlist)-sep]<=wlist[len(wlist)-1]):
        tuples.append((wlist[len(wlist)-sep], wlist[len(wlist)-1]))
    elif(wlist[len(wlist)-sep]>=wlist[len(wlist)-1]):
        tuples.append((wlist[len(wlist)-1],wlist[len(wlist)-sep]))

    tuples.sort(reverse = True)
    return tuples

# takes the file inputs from the user and the max sep
file1 = input("Enter the first file to analyze and compare ==> ")
print(file1)
file2 = input("Enter the second file to analyze and compare ==> ")
print(file2)
sep = input("Enter the maximum separation between words in a pair ==> ")
print(sep)
sep = int(sep)

#finds the average word length by going though the list and adding them to a 
# total and dividing it by the length of the list
list1 = get_words(file1)
tot1 = 0
for x in list1:
    tot1 += len(x)
avg1 = tot1/len(list1)

#finds the total words by getting all words and distinct words and 
# calculates the ratio by dividing the distinct by all
wlist1 = get_words(file1)
disw1 = set(wlist1)
ratio1 = len(disw1)/len(wlist1)

#prints the title, word length, ratio and word set title
print("\nEvaluating document {}".format(file1))
print("1. Average word length: {:.2f}".format(avg1))
print("2. Ratio of distinct words to total words: {:.3f}".format(ratio1))
print("3. Word sets for document {}:".format(file1))

#finds the max length from of all the words in the list
maxlen1 = len(wlist1[0])
for x in wlist1:
    if len(x) > maxlen1:
        maxlen1 = len(x)
#sets a variable to the length of 1, and creates a while loop that takes the words
# and adds them to a set, sorts the words, and makes the words list into a string
y = 1
while y <= maxlen1:
    words = set()
    for x in wlist1:
        if len(x) == y:
            words.add(x)
    swords = sorted(set(words))
    awords = ' '.join(swords)
    c = len(swords)
    #takes the length of the list and determines its proper formattng based on the length 
    # of the list and the word length
    if c == 0:
        if y < 10:
            print("   {}:   {}:".format(y, c))
        elif y >= 10:
            print("  {}:   {}:".format(y, c))
    elif c <= 6:
        if y < 10:
            print("   {}:   {}: {}".format(y, c, awords))
        elif y >= 10:
            print("  {}:   {}: {}".format(y, c, awords))
    elif c > 6:
        if y < 10:
            print("   {}:  {}: {} {} {} ... {} {} {}".format(y, c, swords[0],swords[1],swords[2],swords[-3],swords[-2],swords[-1]))
        elif y >= 10:
            print("  {}:  {}: {} {} {} ... {} {} {}".format(y, c, swords[0],swords[1],swords[2],swords[-3],swords[-2],swords[-1]))
    y+=1

#gets all unique pairs from the list of unique words, sorts them and gets the  
# length of the pairs (I have no idea why though)
tuplist1 = get_pairs(wlist1, sep)
stuplist1 = sorted(tuplist1)
pairlen1 = len(stuplist1) 

#prints the length of distinct pairs
print("4. Word pairs for document {}".format(file1))
print("  {} distinct pairs".format(pairlen1))

#determines if the pair length is longer or shorter than five so that it can print 
# the proper number of pairs 
if pairlen1 > 5:
    print("  {}".format(' '.join(stuplist1[0])))
    print("  {}".format(' '.join(stuplist1[1])))
    print("  {}".format(' '.join(stuplist1[2])))
    print("  {}".format(' '.join(stuplist1[3])))
    print("  {}".format(' '.join(stuplist1[4])))
    print("  ...")
    print("  {}".format(' '.join(stuplist1[-5])))
    print("  {}".format(' '.join(stuplist1[-4])))
    print("  {}".format(' '.join(stuplist1[-3])))
    print("  {}".format(' '.join(stuplist1[-2])))
    print("  {}".format(' '.join(stuplist1[-1])))
elif pairlen1 <=5:
    print("  {}".format(' '.join(stuplist1[0])))
    print("  {}".format(' '.join(stuplist1[1])))
    print("  {}".format(' '.join(stuplist1[2])))
    print("  {}".format(' '.join(stuplist1[3])))
    print("  {}".format(' '.join(stuplist1[4])))
    


#gets all the pairs of the words and gets the length of all the pairs
allpairs1 = get_all_pairs(wlist1, sep)
alllen1 = len(allpairs1) 

#calculates and prints the ratio
dratio1 = pairlen1/alllen1
print("5. Ratio of distinct word pairs to total: {:.3f}".format(dratio1))

#--------------------copies the same code for the second file---------------------------

#finds the average word length by going though the list and adding them to a 
# total and dividing it by the length of the list
list2 = get_words(file2)
tot2 = 0
for x in list2:
    tot2 += len(x)
avg2 = tot2/len(list2)

#finds the total words by getting all words and distinct words and 
# calculates the ratio by dividing the distinct by all
wlist2 = get_words(file2)
disw2 = set(wlist2)
ratio2 = len(disw2)/len(wlist2)

#prints the title, word length, ratio and word set title
print("\nEvaluating document {}".format(file2))
print("1. Average word length: {:.2f}".format(avg2))
print("2. Ratio of distinct words to total words: {:.3f}".format(ratio2))
print("3. Word sets for document {}:".format(file2))

#finds the max length from of all the words in the list 
maxlen2 = len(wlist2[0])
for x in wlist2:
    if len(x) > maxlen2:
        maxlen2 = len(x)
#sets a variable to the length of 1, and creates a while loop that takes the words
# and adds them to a set, sorts the words, and makes the words list into a string
y = 1
while y <= maxlen2:
    words = set()
    for x in wlist2:
        if len(x) == y:
            words.add(x)
    swords = sorted(set(words))
    awords = ' '.join(swords)
    c = len(swords)
    #takes the length of the list and determines its proper formattng based on the length 
    # of the list and the word length
    if c == 0:
        if y < 10:
            print("   {}:   0:".format(y))
        elif y >= 10:
            print("  {}:   0:".format(y))
    elif c <= 6 and c > 0:
        if y < 10:
            print("   {}:   {}: {}".format(y, c, awords))
        elif y >= 10:
            print("  {}:   {}: {}".format(y, c, awords))
    elif c > 6:
        if y < 10:
            print("   {}:  {}: {} {} {} ... {} {} {}".format(y, c, swords[0],swords[1],swords[2],swords[-3],swords[-2],swords[-1]))
        elif y >= 10:
            print("  {}: {}: {} {} {} ... {} {} {}".format(y, c, swords[0],swords[1],swords[2],swords[-3],swords[-2],swords[-1]))
    y+=1

#gets all unique pairs from the list of unique words, sorts them gets
# the length of the pairs 
tuplist2 = get_pairs(wlist2, sep)
stuplist2 = sorted(tuplist2)
pairlen2 = len(tuplist2) 
print("4. Word pairs for document {}".format(file2))
print("  {} distinct pairs".format(pairlen2))

#determines if the pair length is longer or shorter than five so that it can print 
# the proper number of pairs 
if pairlen2 > 5:
    print("  {}".format(' '.join(stuplist2[0])))
    print("  {}".format(' '.join(stuplist2[1])))
    print("  {}".format(' '.join(stuplist2[2])))
    print("  {}".format(' '.join(stuplist2[3])))
    print("  {}".format(' '.join(stuplist2[4])))
    print("  ...")
    print("  {}".format(' '.join(stuplist2[-5])))
    print("  {}".format(' '.join(stuplist2[-4])))
    print("  {}".format(' '.join(stuplist2[-3])))
    print("  {}".format(' '.join(stuplist2[-2])))
    print("  {}".format(' '.join(stuplist2[-1])))
elif pairlen2 <=5:
    print("  {}".format(' '.join(stuplist2[0])))
    print("  {}".format(' '.join(stuplist2[1])))
    print("  {}".format(' '.join(stuplist2[2])))
    print("  {}".format(' '.join(stuplist2[3])))
    print("  {}".format(' '.join(stuplist2[4])))

#gets all the pairs of the words and gets the length of all the pairs
allpairs2 = get_all_pairs(wlist2, sep)
alllen2 = len(allpairs2) 

#calculates and prints the ratio
dratio2 = pairlen2/alllen2
print("5. Ratio of distinct word pairs to total: {:.3f}".format(dratio2))

#creates a function that calculates jaccard similarity, but calculating
# the intersection and union of both lists, returning float values or 0
def jaccard(list1, list2):
    intersec = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersec
    if union == 0 or intersec == 0:
        return 0
    else:
        return float(intersec) / union

print("\nSummary comparison")
#determine and prints which file has longer average words, by taking the averages 
# calculated previously in the code
if avg1 > avg2:
    print("1. {} on average uses longer words than {}".format(file1, file2))
elif avg1 < avg2:
    print("1. {} on average uses longer words than {}".format(file2, file1))

#determines the maximum word length for both by checking which word length is 
# is longer
maxb = maxlen1
if maxlen2 > maxlen1:
    maxb = maxlen2

#makes a list from the sets in the previous code so they can be sent in the 
# jaccard function
list1 = list(disw1)
list2 = list(disw2)

#prints the overall similarity, from the lists
print("2. Overall word use similarity: {:.3f}".format(jaccard(list1, list2)))
print("3. Word use similarity by length:")

#make a while loop that initalizes a variable for the word length, and goes through
# the loop until the max word length it's searching for, finds the words of that length
# in both lists, and appends both to seperate lists. Then the lists get sent into the 
# jaccard function, which returns the proper formatting based on the word length value. 

z = 1
while z <= maxb:
    words1 = []
    words2 = []
    for i in list1:
        if len(i) == z:
            words1.append(i)
    for j in list2:
        if len(j) == z:
            words2.append(j)
    jcard = jaccard(words1, words2)
    if z < 10 and jcard == 0:
        print("   {}: 0.0000".format(z))
    elif z > 10 and jcard == 0:
        print("  {}: 0.0000".format(z))
    elif z <10:
        print("   {}: {:.4f}".format(z, jcard))
    elif z>=10:
        print("  {}: {:.4f}".format(z, jcard))
    z+=1 
# takes the list of tuple pairs previously found in the code, sends them into the jaccard function
# then returns the word pair similarity, with the proper formatting.
print("4. Word pair similarity: {:.4f}".format(jaccard(tuplist1, tuplist2))) 
