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
    
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    
    return X if x_count <= o_count else O
  

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    current_player = player(board)

    if not (0 <= i < 3 and 0 <= j < 3) or board[i][j] != EMPTY or terminal(board):
        raise ValueError("Invalid action")

    new_board = [row.copy() for row in board]
    new_board[i][j] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player in [X, O]:
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == player:
                return player
            if board[0][i] == board[1][i] == board[2][i] == player:
                return player

        if board[0][0] == board[1][1] == board[2][2] == player:
            return player
        if board[2][0] == board[1][1] == board[0][2] == player:
            return player

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True 
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        max_utility = float("-inf")
        best_move = None
        for action in actions(board):
            new_board = result(board, action)
            utility_value = min_value(new_board)
            if utility_value > max_utility or (utility_value == max_utility and best_move is None):
                max_utility = utility_value
                best_move = action
                if max_utility == 1:
                    break
    else:
        min_utility = float("inf")
        best_move = None
        for action in actions(board):
            new_board = result(board, action)
            utility_value = max_value(new_board)
            if utility_value < min_utility or (utility_value == min_utility and best_move is None):
                min_utility = utility_value
                best_move = action
                if min_utility == -1:
                    break

    return best_move
 
    
def min_value(board):
    if terminal(board):
        return utility(board)

    v = float("inf")
    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v


def max_value(board):
    if terminal(board):
        return utility(board)

    v = float("-inf")
    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v