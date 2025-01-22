#import python random module
# all standard libraries: https://docs.python.org/3/library/index.html

import random

#define list that needs to be selected
computer_choice = random.choice(['rock', 'paper', 'scissors'])

# computer_choice = "scissors"

user_choice = input("Do you want to choose rock, paper or scissors? ")

print("computer chose: " + computer_choice)

if computer_choice == user_choice:
  print("It's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
  print("You win! The computer chose scissors.")
elif user_choice == "paper" and computer_choice == "rock":
  print("You win! The computer chose rock.")
elif user_choice == "scissors" and computer_choice == "paper":
  print("You win! The computer chose paper.")
else:
  print("You lose! The computer chose " + computer_choice + ".")
  