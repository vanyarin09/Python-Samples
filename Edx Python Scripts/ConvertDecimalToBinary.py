# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 20:52:16 2018


"""

dec = int(input("Input a whole number: "))
binary = ""
deci = dec
isNegative = False

if dec < 0:
    isNegative = True
    dec = abs(dec)
else:
    isNegative = False
        
if dec == 0:
    binary = str(dec)
while dec > 0:
    binary = str(dec%2) + binary
    dec = dec//2
    
if isNegative:
    binary = '-' + binary    
    
print("Decimal: " + str(deci) + "\nBinary: " + binary)
    