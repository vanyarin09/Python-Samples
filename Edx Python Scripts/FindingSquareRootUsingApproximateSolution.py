# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 21:21:57 2018

@author: Ardrey
"""

#Finding Square root using Approximate solution

print("FINDING A SQUARE ROOT USING APPROXIMATE SOLUTION\n")
square = int(input("Enter a number: "))
epsilon = 0.01
step = 0.001
guess = 0.0

while abs((guess**2 - square)) >= epsilon and guess <= square:
    guess += step

if abs(guess**2 - square) >= epsilon:
    print ("Failed to find the approximate square root of " + str(square))
else:
    print ("The approximate square root of " + str(square) + " is " + str(guess))
    


