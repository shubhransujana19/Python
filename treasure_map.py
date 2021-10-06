# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 18:10:16 2021

@author: shubhransu
"""
row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}\n")

cross = input("Enter column and row: ")
column = int(cross[0])
row = int(cross[1])
selected_row = map[row-1]
selected_row[column-1]="X"
print(f"{row1}\n{row2}\n{row3}\n")