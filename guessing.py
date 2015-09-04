# Guessing
# A number guessing game.

import random

def main():
  replay = True

  while replay:
    if replay:
      target = random.randint(1, 10)
      correct = False

      while not correct:
        if not correct:
          guess = input("Please enter an number between 1 & 10: ")

          if guess == target:
            print ("Correct - Great Guess!!!")
            correct = True
            replay_input = raw_input("Do you want to play again? (Y/N)")
            if replay_input.lower() == "n":
              replay = False

          elif guess > target:
            print("lower")
          else:
            print("higher")


  print ("End of Game")

main()
