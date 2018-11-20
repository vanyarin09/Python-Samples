# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 20:48:48 2018

"""
#Finding a cube root using Newton Raphson algorithm
#root = g - p(g)/p'(g)

print("FINDING THE CUBE ROOT")
epsilon = 0.01
cube = float(input("Enter a number: "))
numberGuesses = 0
guess = cube/3.0

while abs((guess**3)- cube) >= epsilon:
    numberGuesses += 1
    guess = guess - ((guess**3)-cube)/(3*guess**2) #Use the power rule in getting the derivative
    
print("The number of guess is: " + str(numberGuesses))
print("The Cube:" + str(cube) + "\nThe cube root is about: " + str(guess))  
    
