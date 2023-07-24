# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 22:40:02 2021

@author: Nicole Lee
"""
'informs the user to play Mad Libs'
print("Let's play Mad Libs for Homework 1\nType one word responses to the following:")
'prompts and intakes the inputs from the user'
name = input('\nproper_name ==> ')
print(name)
adj1 = input('adjective ==> ')
print(adj1)
noun1 = input('noun ==> ')
print(noun1)
verb1 = input('verb ==> ')
print(verb1)
verb2 = input('verb ==> ')
print(verb2)
noun2 = input('noun ==> ')
print(noun2)
emo1 = input('emotion ==> ')
print(emo1)
verb3 = input('verb ==> ')
print(verb3)
noun3 = input('noun ==> ')
print(noun3)
seas = input('season ==> ')
print(seas)
adj2 = input('adjective ==> ')
print(adj2)
emo2 = input('emotion ==> ')
print(emo2)
team = input('team-name ==> ')
print(team)
noun4 = input('noun ==> ')
print(noun4)
adj3 = input('adjective ==> ')
print(adj3)

'prints the mad libs'
print("\n Here is your Mad Lib...")
print("\n Good morning {}!".format(name))
print("\n\tThis will be a/an {} {}! Are you {} forward to it?".format(adj1, noun1, verb1))
print("\tYou will {} a lot of {} and feel {} when you do.".format(verb2, noun2, emo1))
print("\tIf you do not, you will {} this {}.".format(verb3, noun3))
print("\n\tThis {} was {}. Were you {} when {} won".format(seas, adj2, emo2, team))
print("\tthe {}?".format(noun4))
print("\n\tHave a/an {} day!".format(adj3))