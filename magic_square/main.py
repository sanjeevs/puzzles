import board

"""
 Find a pattern of numbers from [1-9] that can be arranged in a 3x3 grid
 such that the sum of all the rows, cols and diagonals are the same.
 There are 9! total combinations and 8 valid solutions.
 Number of results=8
[[2, 7, 6, 9, 5, 1, 4, 3, 8], 
 [2, 9, 4, 7, 5, 3, 6, 1, 8], 
 [4, 3, 8, 9, 5, 1, 2, 7, 6], 
 [4, 9, 2, 3, 5, 7, 8, 1, 6], 
 [6, 1, 8, 7, 5, 3, 2, 9, 4], 
 [6, 7, 2, 1, 5, 9, 8, 3, 4], 
 [8, 1, 6, 3, 5, 7, 4, 9, 2], 
 [8, 3, 4, 1, 5, 9, 6, 7, 2]]
"""

if __name__ == "__main__":
    choices = []
    magic_board = []
    result = []

    for i in range(1, 10):
        choices.append(i)
    board.make_board(result, magic_board, choices, board.is_valid)

    print(f"Number of results={len(result)}")
    print(result)
    
