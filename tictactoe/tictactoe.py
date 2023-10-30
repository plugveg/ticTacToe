"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
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
    winner=None
    for i in range(3):
        if numberOfPlayerMovesOnLine(board, X, i)==3:
            winner=X
        elif numberOfPlayerMovesOnLine(board, O, i)==3:
            winner=O
        elif numberOfPlayerMovesOnCol(board, X, i)==3:
            winner=X
        elif numberOfPlayerMovesOnCol(board, O, i)==3:
            winner=O
    for i in range(2):
        if numberOfPlayerMovesOnDiag(board, X, i)==3:
            winner=X
        elif numberOfPlayerMovesOnDiag(board, O, i)==3:
            winner=O
    return winner


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
def numberOfPlayerMovesOnLine(board, player, l):
    count=0
    for i in range(3): 
        if board[l][i]== player: 
            count+=1
    return count 

def numberOfPlayerMovesOnCol(board , player , c): 
    count=0
    for i in range(3):
        if board[i][c]== player: 
            count+=1
    return count 


def numberOfPlayerMovesOnDiag(board , player , dia):
    offset=0
    if dia ==0 :
        offset=2
    for i in range(3):
        if board[i][-offset+i]== player: 
            count+=1
    return count 