# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 19:33:26 2018


"""

num = int(input("Enter the position of the fibonacci number: "))


def fib(num):
    if num == 0 or num == 1:
        return 1
    else:
        return fib(num-1) + fib(num-2)

print(fib(num))