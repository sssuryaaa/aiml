def is_valid(board, row, col):
    # Check if placing a queen at (row, col) violates any constraints
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(board, col):
    # Base case: All queens are placed
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_valid(board, i, col):
            board[i][col] = 1
            if solve_n_queens(board, col + 1):
                return True
            board[i][col] = 0

    return False

def print_board(board):
    for row in board:
        print(' '.join(str(cell) for cell in row))

def solve_eight_queens():
    board = [[0] * 8 for _ in range(8)]
    if solve_n_queens(board, 0):
        print_board(board)
    else:
        print("No solution exists.")

solve_eight_queens()