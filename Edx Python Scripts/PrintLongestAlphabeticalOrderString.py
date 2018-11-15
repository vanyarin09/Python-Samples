# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

word = str(input("Enter a string: " ))
prevLetter = ""
currentString = ""
longestString = ""

for currentletter in word:
    if prevLetter <= currentletter:
        currentString += currentletter
        if len(currentString) > len(longestString):
                longestString = currentString
    else:
        currentString = currentletter
    prevLetter = currentletter
print(longestString)






    
        
        
