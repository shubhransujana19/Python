# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 16:49:49 2021

@author: shubhransu
"""

print("Welcome to python pizza")
size = input("which size of pizza do you want? S M L ?")
bill=0
if size == "S" or size =="s":
    bill = 15
    print("small pizza $15")
elif size == "M" or size =="m":
    bill = 20
    print("Medium pizza $20")
elif size == "L" or size =="l":
    bill = 25
    print("Large pizza $25")
else:
    print("Wrong input")    

pepperoni =input("Do you want to add pepperoni ?\n For small pizza +$2 and for MEdium and Large pizza +$3 Y N ? ")
if pepperoni == "Y" or pepperoni =="y":
    if size == "s" or size =="s":
        bill += 2
    elif size == "L" or size =="l" or size == "M" or size =="m":
        bill+=3
    else:
        print("Wrong input")

       
extra_cheese = input("Do you want extra cheese? For extra cheese +$1 Y N")
if extra_cheese == "Y" or extra_cheese =="y":
    bill+=1

print(f"Total bill is ${bill}")