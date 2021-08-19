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
    board_copy[action[0]][action[1]] = player(board)
    
    return board_copy
    # Should never call
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    if all(i == board[0][0] for i in board[0]):
        return board[0][0]
    elif all(i == board[1][0] for i in board[1]):
        return board[1][0]
    elif all(i == board[2][0] for i in board[2]):
        return board[2][0]
    # Check columns
    elif board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[0][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[0][2] == board[2][2]:
        return board[0][2]
    # Check diagonals
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    else:
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
    # If the board is a terminal board, return None.
    if terminal(board): 
        return None
    
    if player(board) == X: 
        value = -99999
        for action in actions(board):
            k = minValue(result(board, action))
            if k > value:
                value = k
                bestMove = action
    elif player(board) == O: 
        value = 99999
        for action in actions(board):
            k = maxValue(result(board, action))    #FIXED
            if k < value:
                value = k
                bestMove = action
    return bestMove

    
    # Should never call
    raise NotImplementedError

def maxValue(board): 
    """
    Returns the value and (i, j) location for the action of maximal score.
    """
    if terminal(board):
        return utility(board)
    value = -99999 # arbitrary small number
    move = None # inital move is no move
    
    for action in actions(board): 
        value = max(value, minValue(result(board, action)))
    return value



def minValue(board): 
    """
    Returns the value and (i, j) location for the action of minimal score.
    """
    if terminal(board):
        return utility(board)
    value = 99999 # arbitrary large number
    move = None # inital move is no move
    for action in actions(board): 
        value = min(value, maxValue(result(board, action)))
    return value
