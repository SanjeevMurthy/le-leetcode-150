"""
Problem Statement
Determine if a 9 x 9 Sudoku board is valid.

Rules:
Each row must contain digits 1-9 without repetition
Each column must contain digits 1-9 without repetition
Each 3 x 3 sub-box must contain digits 1-9 without repetition

. means empty cell.

board =
[
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]
"""

board = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]

def is_valid_sudoku(board, n):
    rows = [set() for _ in range(n)]
    cols = [set() for _ in range(n)]
    boxes = [set() for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            val = board[row][col]
            
            if val == ".":
                continue

            if val in rows[row]:
                return False
            
            if val in cols[col]:
                return False
            
            box_index = (row//3) * 3 + (col//3)
            if val in boxes[box_index]:
                return False
            
            rows[row].add(val)
            cols[col].add(val)
            boxes[box_index].add(val)
    return True


if is_valid_sudoku(board,9):
    print("Valid Sudoku board")
else:
    print("Invalid Sudoku Board")