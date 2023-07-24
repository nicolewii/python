# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 22:51:15 2021

@author: Nicole Lee
"""
'creates happy and sad functions that search the sentence and returns a number that corresponds with its positve or negative word count'
def number_happy(sentence):
     plsent = ""
     for plsent in sentence:
         c1 = sentence.count('laugh')
         c2 = sentence.count('happiness')
         c3 = sentence.count('love')
         c4 = sentence.count('excellent')
         c5 = sentence.count('good')
         c6 = sentence.count('smile')
     return c1+c2+c3+c4++c5+c6
#laugh happiness love excellent good smile
def number_sad(sentence):
    msent = ""
    for msent in sentence:
         c1 = sentence.count('bad')
         c2 = sentence.count('sad')
         c3 = sentence.count('terrible')
         c4 = sentence.count('horrible')
         c5 = sentence.count('problem')
         c6 = sentence.count('hate')
         return c1+c2+c3+c4++c5+c6
# bad sad terrible horrible problem hate

'takes and printsthe sentace from the user'
sent = input("Enter a sentence => ")
print(sent)

'converts all letters in the sentence to lower, so it can find any word in any case (upper or lower)'
sent = sent.lower()

'calls and assigns the functions to get the number of positve and negative words'
plsentnum = number_happy(sent)
msentnum = number_sad(sent)

'multiplies the number from the functions to characters for the sentiment'
plsign = plsentnum*"+"
misign = msentnum*"-"
print("Sentiment: {}{}".format(plsign, misign))

'determines if the sentence is happy or sad by comparing the number of positive and negative words in the given sentence'
if plsentnum > msentnum:
    print("This is a happy sentence.")
elif msentnum > plsentnum:
    print("This is a sad sentence.")
else:
    print("This is a neutral sentence.")


