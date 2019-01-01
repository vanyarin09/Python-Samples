# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 22:55:11 2019

"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def how_many(animalsDict):
    count = 0
    for key in animalsDict:
        count += len(animalsDict[key])
        
        
    return count


print(how_many(animals))
    