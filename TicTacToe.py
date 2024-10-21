# Print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print("-" * 5)

# Check if there is a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if row == [player, player, player]:
            return True
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Check if the board is full
def is_board_full(board):
    return all([cell != ' ' for row in board for cell in row])

# Main Tic Tac Toe game
def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter col (0, 1, 2): "))

        if board[row][col] != ' ':
            print("Cell already taken! Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

play_tic_tac_toe()
