# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:14:16 2018


"""
print ("FACTORIAL CALCULATOR")
num = int(input("Enter a number: "))


def recurFact(num):
    if num == 1:
        return num
    else:
        return num*recurFact(num-1) #recursion

print ("The factorial of " + str(num) + ": " + str(recurFact(num)))