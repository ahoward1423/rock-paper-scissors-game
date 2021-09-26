import os
from dotenv import load_dotenv

load_dotenv()

PLAYER_NAME = os.getenv("PLAYER_NAME", default="Player One")
print("Welcome", PLAYER_NAME, "to my Rock-Paper-Scissors game...")

# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

# prompt for user input

user_choice = input("Choose 'rock' or 'paper' or 'scissors' : ")
print("You Chose: ")
print(user_choice)

# computer choice (at random)

options = ["rock", "paper", "scissors"]

# below if statement adapted from Gianna in Slack

if user_choice not in options:
    print ("Not a valid option, please play again")
    exit()

computer_choice = random.choice(options)
print("Computer Chose: ")
print(computer_choice)

# worked with Arty on the below parts

if computer_choice == user_choice:
    print("You chose the same option, please pick again")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print ("Rock smashes scissors, congrats you won")
    else:
        print ("Paper covers rock, sorry you lost")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print ("Rock smashes scissors, sorry you lost")
    else:
        print ("Scissors cuts paper, congrats you won")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock, congrats you won") 
    else:
        print("Scissors cuts paper, sorry you lost")




