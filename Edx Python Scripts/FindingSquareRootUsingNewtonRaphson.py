# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 20:35:47 2018

"""
#Using Newton-Raphson algorithm to find the root of a number

print("FINDING THE SQUARE ROOT")
epsilon = 0.01 #This is the distance of how close i want to get to the answer

number = float(input("Enter a number: "))
numGuesses = 0
guess = number/2.0


while abs(guess**2 - number) >= epsilon:
    numGuesses += 1
    guess = guess - ((guess**2)-number)/(2*guess)

print("Number of Guesses: " + str(numGuesses))   
print("The Square: " + str(number) + "\nThe square root is about: " + str(guess))
