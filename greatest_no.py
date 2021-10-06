# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 12:06:51 2021

@author: shubhransu
"""
a = []
for i in range(0,3):
    k =int(input())
    a.append(k)
    
max1 = a[0]

for j in range(0,3):
    if max1 < a[j]:
        max1 = a[j]
        
print(max1)