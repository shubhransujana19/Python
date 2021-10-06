# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 01:35:39 2021

@author: shubhransu
"""
peoples_heights = input("Enter the height of peoples:").split()

for i in range(0,len(peoples_heights)):
    peoples_heights[i] = int(peoples_heights[i])
    
count = 0
sum1 = 0    
for j in range(0,len(peoples_heights)):
    sum1 += peoples_heights[j]
    count+=1
 
avg = round(int(sum1/count))    
print(f"average is {avg}")                         
                         
  
 

