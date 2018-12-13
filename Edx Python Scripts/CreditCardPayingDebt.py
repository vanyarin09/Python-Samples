# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 21:41:06 2018
"""
balance = float(input("Input your balance: "))
annualInterestRate = float(input("Interest rate: "))
monthlyPaymentRate = float(input("Monthly Payment Rate: "))

def computeDebt(balance,annualInterestRate,monthlyPaymentRate):
    """
    Input: balance to be paid, the annual interest rate and the monthly payment rate
    Output: The remaining balance of the customer at the end of the year asuuming that the 
    customer pays the minimum rate per month
    
    
    """
    annualInterestRate = annualInterestRate / 100
    monthlyPaymentRate = monthlyPaymentRate / 100
    
    for i in range(12):
        balance = balance - (balance * monthlyPaymentRate)
        balance = balance + ((annualInterestRate/12)*balance)
        print("Month " + str(i+1) + " balance: " + str(round(balance,2)))
    return balance

remainingBalance = computeDebt(balance,annualInterestRate,monthlyPaymentRate)
print("Your remaining balance is: " + str(round(remainingBalance,2)))
