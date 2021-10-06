# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 02:58:42 2021

@author: shubhransu
"""
for i in range(1,101):
    if(i%3 == 0):
        print("Fizz")
    elif(i%5 == 0):
        print("Buzz")
    elif(i%3 == 0 & i%5 == 0):
        print("FizzBuzz")
    else:
        print(i)

