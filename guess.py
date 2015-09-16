# A Number Guessing Games


class Game (object):
    def description(self):
        print()
        print("This is a number guessing game.")
        print("You will have a certian amount of guesses to figure out my number.")
        print("The harder the level the more guesses you get, but the bigger the range of possible numbers.")
        self.level_descript()

    def level_descript(self):
        print()
        print("Easy - 5 guesses to pick a number between 1 & 10")
        print("Medium - 8 guesses to pick a number between 1 & 100")
        print("Hard - 10 guesses to pick a number between 1 & 1,000")

    def set_level(self):
        self.level = 0

        print()
        print("--LEVELS--")
        print("1 = Easy, 2 = Medium, 3 = Hard")
        self.level = str(input("Pick a level: "))
        if(not(self.check_level())):
            self.set_level()
        self.define_difficulty()

    def check_level(self):
        if (self.level == '1'):
            return True
        elif (self.level == '2'):
            return True
        elif (self.level == '3'):
            return True
        elif (self.level.lower() == 'h' or self.level.lower() == "help"):
            self.level_descript()
            return False

        else:
            return False

    def define_difficulty(self):
        if (self.level == '1'):
            self.numb_of_guess = 5
            self.top_numb = 10
        elif (self.level == '2'):
            self.numb_of_guess = 8
            self.top_numb = 100
        elif (self.level == '3'):
            self.numb_of_guess = 10
            self.top_numb = 1000
        else:
            self.numb_of_guess = 1
            self.top_numb = 1

    def set_random(self):
        import random
        self.target = random.randint(1, self.top_numb)

    def guess_number(self):
        guess = int(input("Guess a number between 1 & " + str(self.top_numb) + ": "))
        if (guess == self.target):
            print("Great Guess!!! You are correct!")
        else:
            if(guess > self.target):
                print("LOWER")
            else:
                print("HIGHER")

            self.numb_of_guess -= 1
            if (self.numb_of_guess == 1):
                print("Look Buddy! You have just one guess left. You better make it count.")
                self.guess_number()
            elif (self.numb_of_guess > 1):
                print("You now have " + str(self.numb_of_guess) + " guesses left.")
                self.guess_number()
            else:
                print("Sorry, you are out of guesses.")
                print("The correct number was " + str(self.target))


def main():
    my_game = Game()
    my_game.description()
    my_game.set_level()
    my_game.set_random()
    my_game.guess_number()


main()
