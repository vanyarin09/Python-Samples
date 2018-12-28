# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 17:24:36 2018

"""
#LONG METHOD
def oddTuple(aTuple):
    odd = ()
    i = 1
    for t in aTuple:
        if i%2 == 1:
            odd = odd + (t,)
        i += 1
    return odd
    

 
print (oddTuple(('I', 'am', 'a', 'test', 'tuple')))


#SHORT METHOD

"""
def oddTuple(aTuple):
    odd = aTuple[::2]
    return odd
"""



