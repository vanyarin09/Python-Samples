# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 00:04:46 2018


"""

#dec stands for decimal

decFraction = float(input("Enter a number between 0 and 1: "))

power = 0 #power 

#This code block finds a power of 2 that can convert the decimal fraction into a wholeNumber
while ((2**power)*decFraction)%1 != 0:
    power += 1

#Converts the decimal fraction into a whole number using the power of 2
wholeNumber = int(decFraction*(2**power))
binaryString = '' #Stores the binary bits 1 and 0 into a string

if wholeNumber == 0:
    binaryString = '0'

#Converts the whole number to a binary  
while wholeNumber > 0:
    binaryString = str(wholeNumber%2) + binaryString
    wholeNumber = wholeNumber//2
 
    
for num in range(power - len(binaryString)):
    binaryString = "0" + binaryString

#Converts the binary representation of the whole number to a fraction    
binaryString = binaryString[0:-power] + "." + binaryString[-power:]  
 
print("Decimal Fraction: " + str(decFraction) + "\nBinary: " + str(binaryString)) 
    
    