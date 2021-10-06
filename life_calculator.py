# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 10:09:40 2021

@author: shubhransu
"""
age = int(input("What is your age?"))
left_years = int(90-age)
left_days = int(left_years*365)
left_months = int(left_days/30)
left_weeks = int(left_months*4)
print(f"You have {left_years} years and  {left_days} days and {left_months} months and {left_weeks} weeks")
print(left_years,left_days,left_months,left_weeks)

