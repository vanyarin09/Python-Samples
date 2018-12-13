# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 15:09:11 2018

"""
import math

def polysum(n,s):
    """
    Input: n = number of sides, s = length of sides
    Output: sum of area and perimeter squared
    """
    area = (0.25*n*(s**2))/(math.tan(math.pi/n))
    perimeter = ((n*s)**2)
    
    return round(area + perimeter,4)
    
sides = int(input("Enter number of sides: "))
length = float(input("Enter length of sides: "))
print("The polysum is " + str(polysum(sides,length)))