import random
import sys


class error(Exception):
    pass


class Exit(error):
    pass


def rock_paper_scissors(counter):
    options = input("Do you want to play? (Yes, No or Q)").lower()

    if options == "yes":
        pass
        
    elif options == "no":
        #sys.tracebacklimit = 0
        #raise Exit()
        print("Goodbye..see you later!")
        counter = 1
        return counter
        
    elif options == "q":
        #sys.tracebacklimit = 0
        # raise Exit()]
        print("Goodbye..see you later!")
        counter = 1
        return counter
        # break
    else:
        print("Invalid Input")
        counter = 1
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


counter = 0
while counter < 1:
    value = rock_paper_scissors(counter)
    if value >= 1:
        break
    # options = input("Do you want to play? (Yes, No or Q)").lower()
    # if options == "yes":
    #     pass
    # elif options == "no":
    #     print("Goodbye..see you later!")
    #     counter = 1
    #     break
    # elif options == "q":
    #     print("Goodbye..see you later!")
    #     counter = 1
    #     break
    # else:
    #     print("Invalid Input")
    #     counter = 1

    # game = ['r', 'p', 's']
    # player = input("Rock (r), Paper (p) or Scissors (s) ? ")
    # ai = random.choice(game)
    # print(player + " vs " + ai)

    # if player == "r" and ai == "s":
    #     print("You have won the game!")
    # elif player == "p" and ai == "r":
    #     print("You have won the game!")
    # elif player == "s" and ai == "s":
    #     print("That was a tie! Try again!")
    # elif player == "r" and ai == "r":
    #     print("That was a tie! Try again!")
    # elif player == "r" and ai == "p":
    #     print("The AI beat you! Try again!")
    # elif player == "p" and ai == "p":
    #     print("That was a tie! Try again!")
    # elif player == "s" and ai == "p":
    #     print("You have won the game!")
    # elif player == "p" and ai == "s":
    #     print("The AI beat you! Try again!")
    # else:
    #     print("The AI beat you! Try again!")
