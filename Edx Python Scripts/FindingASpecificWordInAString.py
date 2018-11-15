# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 19:51:26 2018
"""

s = str(input("Enter a string: "))
wordToFind = str(input("Enter the word you want to find: "))
for c in range(len(s)):
    if s[c:c+len(wordToFind)] == wordToFind:
        print("The word: " + wordToFind + " is found within the string")
        break
    else:
        print("There is no " + wordToFind + " found within the string")

