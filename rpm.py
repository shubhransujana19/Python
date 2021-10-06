# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 00:14:24 2021

@author: shubhransu
"""
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
human_no = int(input("What do you choose? Type 0 rock and 1 for paper ,2 for scissors"))
computer_no = random.randint(0,2)
if human_no == 0:
    print(f"You choose {human_no} that is rock")
    print(rock)
elif human_no == 1:
    print(f"You choose {human_no} that is paper")
    print(paper)
elif human_no == 2:
    print(f"You choose {human_no} that is scissor")
    print(scissors) 
    
if computer_no == 0:
    print(f"You choose {computer_no} that is rock")
    print(rock)
elif computer_no == 1:
    print(f"You choose {computer_no} that is paper")
    print(paper)
elif computer_no == 2:
    print(f"You choose {computer_no} that is scissor")
    print(scissors)     

if (human_no == computer_no):
   print("The match is tie!")
elif (human_no == 0 & computer_no == 2 or human_no == 2 & computer_no ==1 or human_no == 1 & computer_no == 0):
    print("You win!")
else:
    print("computer win!")
    
         

