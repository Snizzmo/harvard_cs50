"""
Tic Tac Toe Player
"""

import math
import copy

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
    xCount = 0
    yCount = 0
    for i in range(0, len(board)): 
        for j in range(0, len(board[0])):
            if board[i][j] == X: 
                xCount += 1
            if board[i][j] == O: 
                yCount += 1
    
    if xCount > yCount: 
        return O
    return X

    # Should never call
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()

    for i in range(0, len(board)): 
        for j in range(0, len(board[0])):
            if board[i][j] == EMPTY:
                moves.add((i,j))
    return(moves)

    # Should never call
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)
    if board_copy[action[0]][action[1]] is not EMPTY:
        raise ValueError
    board_copy[action[0]][action[1]]= player(board)
    
    return board_copy
    # Should never call
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check rows from https://stackoverflow.com/questions/39922967/python-determine-tic-tac-toe-winner
    for row in board: 
        if len(set(row)) == 1: 
            return row[0]
    
    # check columns
    [[row[i] for row in board] for i in range(len(board[0]))] #transposes the board, assumes it is square
    for column in board: 
        if len(set(column)) == 1: 
            return board[0]
    [[row[i] for row in board] for i in range(len(board[0]))] #flip it back
    
    # check diagonals from https://stackoverflow.com/questions/39922967/python-determine-tic-tac-toe-winner
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]
    
    # no win conditions met, return None
    return None

    # Should never call
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None: 
        return True
    elif (not any(EMPTY in row for row in board) and winner(board) is None): 
        return True
    else: 
        return False

    # Should never call
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0
    # Should never call
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # Should never call
    raise NotImplementedError
