# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 09:18:44 2021

@author: shubhransu
"""
print("Enter your weight:\n")
weight = float(input())
print("Enter your height:\n")
height = float(input())
bmi = int(weight/(height*height))
if bmi<18.5:
    print("They are underweight")
elif bmi<25:
    print("Normal weight")
elif bmi<30:
    print("Overweight")
elif bmi<35:
    print("Obese")
else:
    print("Clinically obese")

