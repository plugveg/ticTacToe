"""
Tic Tac Toe Player
Eliott Garnier, Enzo Chavalier, Jean Barbet, Thomas Siest
"""


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
    # compter le nombre de X et de O
    # si X > O alors O joue
    # si X = O alors X joue

    X_count = 0
    O_count = 0

    for x in board:
        for y in x:
            if y == X:
                X_count += 1
            elif y == O:
                O_count += 1

    if X_count == O_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    liste_tuples = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                liste_tuples.append((i, j))

    return liste_tuples


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = []
    for row in board:
        new_row = []
        for cell in row:
            new_row.append(cell)
        new_board.append(new_row)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def check_rows(board, player):
    """
    Check if the player has won on the rows
    """
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
    return False


def check_columns(board, player):
    """
    Check if the player has won on the columns
    """
    for i in range(3):
        if all(board[j][i] == player for j in range(3)):
            return True
    return False


def check_diagonals(board, player):
    """
    Check if the player has won on the diagonals
    """
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player in ['X', 'O']:
        if check_rows(board, player) or check_columns(board, player) or check_diagonals(board, player):
            return player
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in board:
        if None in row:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def max_value(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if player(board) == X:
        v = float("-inf")
        best_action = None
        for action in actions(board):
            min_val = min_value(result(board, action))
            if min_val > v:
                v = min_val
                best_action = action
        return best_action
    else:
        v = float("inf")
        best_action = None
        for action in actions(board):
            max_val = max_value(result(board, action))
            if max_val < v:
                v = max_val
                best_action = action
        return best_action
