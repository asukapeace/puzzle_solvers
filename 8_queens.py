def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, num_rows, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(board, col):
    if col >= num_cols:
        return True
    for i in range(num_rows):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens(board, col + 1):
                return True
            board[i][col] = 0
    return False

num_rows = int(input("Enter number of rows: "))
num_cols = int(input("Enter number of columns: "))
board = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

if solve_n_queens(board, 0):
    print("Solution:")
    for row in board:
        print(row)
else:
    print("No solution found.")