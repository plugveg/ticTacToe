"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None

# création objet jeu et board

def initial_state():
    """
    Returns starting state of the board.
    """
    class Game:
        def __init__(self):
            self.numtour = 0
            self.playertour = X
            self.board = [[EMPTY, EMPTY, EMPTY],
                        [EMPTY, EMPTY, EMPTY],
                        [EMPTY, EMPTY, EMPTY]]

    return Game.board


def player(board, playertour, numtour):
    """
    Returns player who has the next turn on a board.
    """
    # compter le nombre de X et de O
    # si X > O alors O joue
    # si X = O alors X joue

    # parcourir le board
    X_count = 0
    O_count = 0

    for x in board:
        for y in x:
            if y == X:
                X_count += 1
            elif y == O:
                O_count += 1

    numtour = X_count + O_count

    if X_count == O_count:
        return playertour
    else:
        return playertour == O

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    liste_tuples = []
    for x in board:
        for y in x:
            if board[x][y] == EMPTY:
                liste_tuples += (x, y)

    return liste_tuples

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
