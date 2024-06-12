import GuessGame
import MemoryGame
import CurrencyRouletteGame

def welcome(name):
    msg = f"""
         Hello {name} and welcome to the World of Games (WoG).
         Here you can find many cool games to play.
         """
    return msg


def load_game():
    msg = """
        Please choose a game to play:
        1. Memory Game - a sequence of numbers will appear for 1 second and you have to
        guess it back
        2. Guess Game - guess a number and see if you chose like the computer
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS
        """
    game = int(input(msg))
    if game < 1 or game > 3:
        exit(1)

    difficulty = int(input("Please choose game difficulty from 1 to 5:"))
    if difficulty < 1 or difficulty > 5:
        exit(2)


    if game == 1:
        MemoryGame.play(difficulty)
    elif game == 2:
        GuessGame.play(difficulty)
    elif game == 3:
        CurrencyRouletteGame.play(difficulty)