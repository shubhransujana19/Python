# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 10:43:45 2021

@author: shubhransu
"""
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage would you like to give? 10,12,or 15?$"))
split_bill = int(input("How many people to split the bill?"))
print(f"Each person should pay: {round((total_bill+(total_bill*percentage/100))/split_bill,2)} ")


