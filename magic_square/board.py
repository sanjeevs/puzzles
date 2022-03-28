NUM_ROWS = 3
NUM_COLS = 3

import copy 

def make_board(result, board, choices, is_valid_pred):
    if len(choices) == 0:
        if is_valid_pred(board):
            result.append(board)
        return 
    else:
        for i in choices:
            dup_choices = copy.deepcopy(choices)
            dup_choices.remove(i)
            dup_board = copy.deepcopy(board)
            dup_board.append(i)
            make_board(result, dup_board, dup_choices, is_valid_pred)

def sum_row(board, row_idx):
    if row_idx >= NUM_ROWS:
        raise InvalidArgument("Exceeded row idx")
    result = 0
    for i in range(NUM_COLS):
        result += board[row_idx * NUM_COLS + i]
    return result

def sum_col(board, col_idx):
    if col_idx >= NUM_COLS:
        raise InvalidArgument("Exceeded col idx")
    result = 0
    for i in range(NUM_ROWS):
        result += board[col_idx + NUM_ROWS * i]
    return result

def sum_diagonal(board, left_diag):
    if left_diag:
        result = board[0] + board[4] + board[8]
    else:
        result = board[2] + board[4] + board[6]
    return result

def is_valid(board):
    magic_value = sum_row(board, 0)
    result = True 

    for i in range(NUM_ROWS):
        if sum_row(board, i) != magic_value:
            result = False
            break

    if result != False:
        for j in range(NUM_COLS):
            if sum_col(board, j) != magic_value:
                result = False
                break

    if result != False:
        for j in range(2):
            if sum_diagonal(board, j) != magic_value:
                result = False
                break

    return result

def test_sum():
    board = []
    for i in range(NUM_ROWS * NUM_COLS):
        board.append(i + 1)
    assert sum_row(board, 0) == 6
    assert sum_col(board, 0) == 12
    assert sum_row(board, 2) == 24
    assert sum_col(board, 2) == 18

def test_col():
    board = []
    for i in range(NUM_ROWS * NUM_COLS):
        board.append(i + 1)
    assert sum_diagonal(board, True) == 15
    assert sum_diagonal(board, False) == 15

def test_result0():
    board = []
    for i in range(NUM_ROWS * NUM_COLS):
        board.append(i + 1)
    assert is_valid(board) == False
