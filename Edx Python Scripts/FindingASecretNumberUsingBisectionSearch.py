# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 19:24:03 2018


"""
#This program finds the secret number between 0 and 100 but not including 100 using the bisection search


print("Please think of a number betwween 0 and 100")
low = 0
high = 100
guess = (high + low)//2
isSearching = True
while (isSearching):
    print("Is this your secret number? " + str(guess))
    ans = input("Enter 'h' if the guess is too big, 'l' if it's too small and 'c' if it's correct: ")
    if(ans == "h"):
        high = guess
    elif(ans == "l"):
        low = guess
    elif(ans == "c"):
        isSearching = False
        print("Game Over!\nYour secret number is: " + str(guess))
        break
    else:
        print("Sorry I did not understand your input")
    guess = (high + low)//2
    

