from random import randint

from pip._vendor.distlib.compat import raw_input

board = []

for x in range(5):
    board.append(["O"] * 5)


def print_board(board):
    for row in board:
        print
        " ".join(row)


print
"Let's play Battleship!"
print_board(board)


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)

