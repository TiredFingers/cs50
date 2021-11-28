"""
Tic Tac Toe Player
"""

import copy

X = "X"
O = "O"
EMPTY = None
res_action = None


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

    x = 0
    o = 0

    for i in range(3):
        for j in range(3):

            if board[i][j] == X:
                x += 1
            elif board[i][j] == O:
                o += 1

    if x > o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    res = set()

    for i in range(3):
        for j in range(3):

            if board[i][j] != X and board[i][j] != O:
                res.add((i, j))

    return res


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    b = copy.deepcopy(board)

    if action is None:
        t = ''

    x_idx = action[0]
    y_idx = action[1]

    b[x_idx][y_idx] = player(board)

    return b


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]

    if board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]

    if board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]

    if board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]

    if board[1][0] == board[1][1] == board[1][2]:
        return board[1][0]

    if board[2][0] == board[2][1] == board[2][2]:
        return board[2][0]

    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    return winner(board) is not None or len(actions(board)) == 0


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    who = winner(board)

    if who == X:
        return 1

    if who == O:
        return -1

    return 0


def _minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    global res_action
    if terminal(board):
        return utility(board)

    utilities = []
    moves = []

    for action in actions(board):
        res_board = result(board, action)
        utilities.append(_minimax(res_board))
        moves.append(action)

    if player(board) == X:
        max_score_index = utilities.index(max(utilities))
        res_action = moves[max_score_index]
        return utilities[max_score_index]
    else:
        min_score_index = utilities.index(min(utilities))
        res_action = moves[min_score_index]
        return utilities[min_score_index]


def minimax(board):

    global res_action

    _minimax(board)

    return res_action

