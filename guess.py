# A Number Guessing Games


class Game (object):
    def set_level(self):
        self.level = 0

        print("-LEVELS-")
        print("1 = Easy, 2 = Medium, 3 = Hard")
        self.level = int(input("Pick a level: "))


def main():
    my_game = Game()
    my_game.set_level()


main()
