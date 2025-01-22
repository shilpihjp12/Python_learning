#randomly dicing the number from 1 to 6
import random

roll = random.randint(1, 6)

guess = int(input("Guess the number: "))

if(guess == roll):
  print("You guessed correctly! The number was " + str(roll) + ".")
else:
  print("You guessed wrong! The number was " + str(roll) + ".")