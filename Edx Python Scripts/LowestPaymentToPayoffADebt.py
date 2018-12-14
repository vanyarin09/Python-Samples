# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 17:21:38 2018
"""

balance = float(input("Enter your balance: ")) #Unpaid Balance
realBalance = balance 
annualInterestRate = float(input("Enter annual interest rate: ")) #Annual interest rate
annualInterestRate = annualInterestRate/100
initialPayment = 10
month = 0

while month <= 12:   
    if month == 12 and balance > 0: #If there is still remaining balance reset
        month = 0
        initialPayment = initialPayment + 10 #Increses the payment to find the minimum to payoff the debt in a year
        balance = realBalance
    else:
        balance -= initialPayment
        balance = balance + ((annualInterestRate/12) * balance)
        month += 1
    
print("Lowest Payment per month should be: " + str(initialPayment))
    
   
    

        
    
    


