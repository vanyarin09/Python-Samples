# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 19:50:36 2018

"""
alphabet = "abcdefghijklmnopqrstuvwxyz"

def toChars(word):
    word = word.lower()
    letters = ""
    for character in word:
        if character in alphabet:
            letters = letters + character
    return letters

def isPalindrome(word):
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and isPalindrome(word[1:-1])
    
    return isPalindrome(word)
    
word = input("Enter a word or sentence: ")
letters = str(toChars(word))
print(isPalindrome(letters))

