# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 16:04:17 2021

@author: shubhransu
"""
year = int(input("Enter any year:"))
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
           print(f"{year} is a Leapyear")
        else:
           print(f"{year} is not a Leapyear")
    else:
         print(f"{year} is a leapyear")
else:
    print(f"{year} is not a Leapyear")
