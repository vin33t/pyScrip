import os
#import randint method
from random import randint

from pip._vendor.distlib.compat import raw_input

board = []

for x in range(5):
    board.append(["O"] * 5)
#Defining functions

def print_board(board):
    for row in board:
        print(" ".join(row))


print("Let's play Battleship!")
print_board(board)


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)

#loop to get input from user 4 times and displaying output accordingly

for i in range(4):
    print("Turn ", i + 1)
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.")
        elif (board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            if (i == 3):
                print("Game Over")
        print_board(board)

#Asking the users if they want to run the file again or Go to main men or Exit the Program
print("Enter 0 to Play again or 1 to got to Main Menu or 2 to exit or Terminate the program")
option_selected_by_user=int(input("My option is : "))
if option_selected_by_user==0:
    print("Battleship Will be started again")
    os.system('python battleship.py')
elif option_selected_by_user==1:
    print("Redirecting to Main Menu")
    os.system('python main.py')
elif option_selected_by_user==2:
    exit()
else:
    os.system('python main.py')
