import random
NUM_DIGITS = 3
MAX_GUSSES = 10

def main():
    print('''Bagels, a deductive logic game.
          By Siddhant Doshi
          
        I am thinking of a {} - digit number with no repeated digits.
        try to guess what it is. Here are some clues:
        When i say:     That means:
            Pico            One digit is correct but position is wrong.
            Fermi           One digit is correct and in right position.
            ''')
