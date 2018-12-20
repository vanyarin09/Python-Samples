# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 18:27:46 2018

"""

balance = 999999 #Unpaid Balance

annualInterestRate = 0.18 #Annual interest rate
monthlyInterestRate = annualInterestRate/12.0

lowerBound = balance/12
upperBound = (balance*(1 + monthlyInterestRate)**12)/12.0

guess = (lowerBound + upperBound)/2

remainBalance = balance

epsilon = 0.01

while(remainBalance >= epsilon):
    
    guess = (lowerBound + upperBound) / 2
    
    
    for i in range(12):   #Iterate for 1 year
        newBalance = remainBalance - guess
        remainBalance = newBalance + (monthlyInterestRate*newBalance)
        
    #After 1 year check if remaining balance is less than 0 means that you are paying too much   
    if(remainBalance < 0):
        upperBound = guess
        remainBalance = balance
    
    #After 1 year check if remaining balance is greater than epsilon means that you are paying less
    elif (remainBalance > epsilon):
        lowerBound = guess
        remainBalance = balance
        
        
print("Your lowest monthly payment is : " + str(round(guess,2)))
        
        
  
  

    

    
    
    