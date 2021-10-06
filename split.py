# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 17:33:23 2021

@author: shubhransu
"""
import random

names = input("Give any names by using comma: ")
names_list = names.split(", ")

bill = random.choice(names_list)

print(f"{bill} will pay the bill")

