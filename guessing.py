# Guessing
# A number guessing game.

import random

def main():
  target = random.randint(1, 10)
  correct = False

  while  not correct:
    guess = input("Please enter an number between 1 & 10: ")

    if guess == target:
      print ("Correct - Great Guess!!!")
      correct = True
    elif guess > target:
      print("lower")
    else:
      print("higher")

    if correct:
      break

  print ("End of Game")

main()
