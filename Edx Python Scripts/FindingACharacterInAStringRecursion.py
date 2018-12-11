# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 23:20:48 2018


FINDING A CHARACTER IN A STRING USING RECURSION
"""
def isIn(char, aStr):
    
    if len(aStr) == 0:
        return False
    
    if len(aStr) == 1:
        return char == aStr
    
    elif len(aStr) > 1:
        if char < aStr[len(aStr)//2]:
            return isIn(char, aStr[:len(aStr)//2])
        else:
            return isIn(char, aStr[len(aStr)//2:])
 
    
        
    
print (isIn("a","abcdefg"))
            
    
