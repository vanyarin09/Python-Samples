# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 19:36:49 2018


"""

def gcd(a,b):
    
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

print (gcd(17,12))
        
        
