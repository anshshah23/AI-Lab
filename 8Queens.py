# Check if placing the queen at position (row, col) is safe
def is_safe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

# Solving the 8 Queens problem using backtracking
def solve_8_queens(board, col):
    # If all queens are placed, return True
    if col >= len(board):
        return True

    # Try placing the queen in all rows one by one
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place the queen
            board[i][col] = 1

            # Recur to place the rest of the queens
            if solve_8_queens(board, col + 1):
                return True

            # If placing the queen here leads to a solution, backtrack
            board[i][col] = 0

    return False

# Print the board
def print_board(board):
    for row in board:
        print(" ".join(['Q' if x == 1 else '.' for x in row]))

# Main function to run the 8 Queens problem
def solve():
    N = 8
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_8_queens(board, 0):
        print("No solution exists")
        return
    print_board(board)

solve()
