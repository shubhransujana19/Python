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
print(left_years,left_days,left_months,left_weeks)

