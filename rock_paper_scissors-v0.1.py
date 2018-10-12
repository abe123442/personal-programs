import random
import sys


class error(Exception):
    pass
class Exit(error):
    pass


def rock_paper_scissors():
    options = input("Do you want to play? (Yes, No or Q)").lower()

    if options == "yes":
        pass
        
    elif options == "no":
        sys.tracebacklimit = 0
        raise Exit()
       
        
    elif options == "q":
        sys.tracebacklimit = 0
        raise Exit()
   
    else:
        print("Invalid Input")
        return()
        
    game = ['r', 'p', 's']
    player = input("Rock (r), Paper (p) or Scissors (s) ? ")
    ai = random.choice(game)
    print(player + " vs " + ai)

    if player == "r" and ai == "s":
        print("You have won the game!")
    elif player == "p" and ai == "r":
        print("You have won the game!")
    elif player == "s" and ai == "s":
        print("That was a tie! Try again!")
    elif player == "r" and ai == "r":
        print("That was a tie! Try again!")
    elif player == "r" and ai == "p":
        print("The AI beat you! Try again!")
    elif player == "p" and ai == "p":
        print("That was a tie! Try again!")
    elif player == "s" and ai == "p":
        print("You have won the game!")
    elif player == "p" and ai == "s":
        print("The AI beat you! Try again!")
    else:
        print("The AI beat you! Try again!")


while 0 < 1:
    rock_paper_scissors()
  