# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 17:50:20 2021

@author: shubhransu
"""
boy_name = input("Enter your boyfriend name")
girl_name = input("Enter your girlfriend name")

t= int(boy_name.count("t")) + int(girl_name.count("t"))
r= int(boy_name.count("r")) + int(girl_name.count("r"))
u= int(boy_name.count("u")) + int(girl_name.count("u"))
e= int(boy_name.count("e")) + int(girl_name.count("e"))
l= int(boy_name.count("l")) + int(girl_name.count("l"))
o= int(boy_name.count("o")) + int(girl_name.count("o"))
v= int(boy_name.count("v")) + int(girl_name.count("v"))
e= int(boy_name.count("e")) + int(girl_name.count("e"))

n1 =(t+r+u+e)*10
n2 = (l+o+v+e)
love_percentage = (n1+n2)
print("Your love percentage is:",love_percentage)

if (love_percentage<10 & love_percentage>90):
    print(f"Your score is{love_percentage},you go together like coke and mentos ")
elif(love_percentage>40 & love_percentage<50):
    print(f"Your score is {love_percentage}, you are alright together.")
else:
    print(f"Your score is{love_percentage}")    
    



