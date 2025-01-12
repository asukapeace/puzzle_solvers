import random

def is_valid(board, row, col, num):
    """
    Check if it's possible to place a number in a given position
    """
    # row
    for x in range(9):
        if board[row][x] == num:
            return False

    # column
    for x in range(9):
        if board[x][col] == num:
            return False

    # box
    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True


def solve_sudoku(board):
    """
    Solve the Sudoku puzzle using backtracking
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        board[i][j] = 0
                return False
    return True


def print_board(board):
    """
    Print the Sudoku board in a nice format
    """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def get_board_from_user():
    """
    Get a Sudoku board from the user
    """
    board = []
    for i in range(9):
        row = input(f"Enter row {i+1} (space-separated numbers): ")
        row = [int(x) if x != '0' else 0 for x in row.split()]
        if len(row) != 9:
            print("Invalid input. Please enter 9 numbers separated by spaces.")
            return get_board_from_user()
        board.append(row)
    return board

def generate_random_board():
    """
    Generate a random Sudoku board
    """
    board = [[0]*9 for _ in range(9)]
    def is_valid(num, row, col):
        for x in range(9):
            if board[row][x] == num:
                return False
        for x in range(9):
            if board[x][col] == num:
                return False
        start_row, start_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False
        return True
    def solve():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    numbers = list(range(1, 10))
                    random.shuffle(numbers)
                    for num in numbers:
                        if is_valid(num, i, j):
                            board[i][j] = num
                            if solve():
                                return True
                            board[i][j] = 0
                    return False
        return True
    solve()
    # Remove some numbers
    for i in range(9):
        for j in range(9):
            if random.random() < 0.7:
                board[i][j] = 0
    return board

def main():
    print("Welcome to the Sudoku solver!")
    while True:
        print("Options:")
        print("1. Enter a Sudoku board manually")
        print("2. Generate a random Sudoku board")
        print("3. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            board = get_board_from_user()
            if solve_sudoku(board):
                print("Solution:")
                print_board(board)
            else:
                print("No solution exists")
        elif choice == "2":
            board = generate_random_board()
            print("Random board:")
            print_board(board)
            if solve_sudoku(board):
                print("\nSolution:")
                print_board(board)
            else:
                print("No solution exists")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()