def print_board(board):
    """Print the current state of the board"""
    print("\n   |   |   ")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("   |   |   \n")

def check_winner(board):
    """Check if there's a winner"""
    # Winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]]
    return None

def is_board_full(board):
    """Check if the board is full"""
    return ' ' not in board

def get_player_move(board, player):
    """Get valid move from player"""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                return move
            else:
                print("Invalid move! Choose an empty position (1-9).")
        except ValueError:
            print("Please enter a valid number (1-9).")

def play_tic_tac_toe():
    """Main game function"""
    print("Welcome to Tic-Tac-Toe!")
    print("Positions are numbered 1-9:")
    print("\n 1 | 2 | 3 ")
    print("___|___|___")
    print(" 4 | 5 | 6 ")
    print("___|___|___")
    print(" 7 | 8 | 9 ")
    print("\n")
    
    # Initialize empty board
    board = [' '] * 9
    current_player = 'X'
    
    while True:
        print_board(board)
        
        # Get player move
        move = get_player_move(board, current_player)
        board[move] = current_player
        
        # Check for winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"🎉 Player {winner} wins!")
            break
        
        # Check for tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'
    
    # Ask to play again
    play_again = input("\nWould you like to play again? (y/n): ").lower()
    if play_again == 'y':
        play_tic_tac_toe()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_tic_tac_toe()
