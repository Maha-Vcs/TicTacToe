import random

# Display the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    return any(
        all(cell == player for cell in row) for row in board
    ) or any(
        all(board[row][col] == player for row in range(3)) for col in range(3)
    ) or all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3))

# Check if the board is full (draw condition)
def is_draw(board):
    return all(cell != " " for row in board for cell in row)

# Get available moves
def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

# AI move (random)
def ai_move(board):
    return random.choice(get_available_moves(board))

# Main game loop
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = {"X": "Player", "O": "AI"}
    
    print("Welcome to Tic-Tac-Toe!")
    mode = input("Choose mode: 1 - Two Player, 2 - Play Against AI: ").strip()
    ai_enabled = mode == "2"

    current_player = "X"
    print_board(board)

    while True:
        if ai_enabled and current_player == "O":
            row, col = ai_move(board)
        else:
            try:
                move = input(f"{players[current_player]}'s turn ({current_player}), enter row and column (0-2 0-2): ")
                row, col = map(int, move.split())
                if board[row][col] != " ":
                    print("Cell already taken! Try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input! Enter row and column as two numbers (0-2).")
                continue
        
        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"{players[current_player]} ({current_player}) wins! 🎉")
            break
        elif is_draw(board):
            print("It's a draw! 🤝")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
