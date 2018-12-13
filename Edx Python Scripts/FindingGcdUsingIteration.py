# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 19:02:50 2018


"""
#Finding GCD using iteration


def gcd(a,b):
    if a < b:
        gcd = a
    else:
        gcd = b
    isSearching = True
    while isSearching:
        if a % gcd == 0 and b % gcd == 0:
            isSearching = False
        else:
            gcd -= 1
    return gcd
    

ans = gcd(17,12)
print ("The answer is: " + str(ans))
    
    
         
