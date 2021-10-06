# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 12:21:49 2021

@author: shubhransu
"""
no =int(input("Enter any number:"))
rev = 0
while(no>0):
    rem =no%10
    rev = rev*10+rem
    no = no//10
    
print(f"Reverse number is {rev}")    

