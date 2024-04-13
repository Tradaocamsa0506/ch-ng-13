def is_valid_sudoku(board):
    # Check rows
    for row in board:
        if has_duplicates(row):
            return False
    
    # Check columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if has_duplicates(column):
            return False
    
    # Check blocks
    for block_row in range(3):
        for block_col in range(3):
            block = [board[row][col] for row in range(block_row*3, (block_row+1)*3) for col in range(block_col*3, (block_col+1)*3)]
            if has_duplicates(block):
                return False
    
    return True

def has_duplicates(lst):
    seen = set()
    for num in lst:
        if num != 0 and num in seen:
            return True
        seen.add(num)
    return False
board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

print(is_valid_sudoku(board))  # Output: True