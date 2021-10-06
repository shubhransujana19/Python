# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 02:24:08 2021

@author: shubhransu
"""
num = input("Enter Your Numbers:").split()

for i in range(0,len(num)):
    num[i] = int(num[i])
    
print(num)
max = num[0]
for j in range(0,len(num)):
     if max<num[j]:
         max = num[j]
         
print(f"Maximum value or number is {max}")            
    

