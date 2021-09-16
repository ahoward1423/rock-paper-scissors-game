# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

# prompt for user input

user_choice = input("Choose 'rock' or 'paper' or 'scissors' : ")
print(user_choice)

# computer choice (at random)

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print(computer_choice)
