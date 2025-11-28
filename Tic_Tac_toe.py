import random

def show_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_for_win(board, player):
    if board[0] == player and board[1] == player and board[2] == player: return True
    if board[3] == player and board[4] == player and board[5] == player: return True
    if board[6] == player and board[7] == player and board[8] == player: return True
    
    if board[0] == player and board[3] == player and board[6] == player: return True
    if board[1] == player and board[4] == player and board[7] == player: return True
    if board[2] == player and board[5] == player and board[8] == player: return True
    
    if board[0] == player and board[4] == player and board[8] == player: return True
    if board[2] == player and board[4] == player and board[6] == player: return True

    return False

def start_game():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    player = "X" 
    
    print("--- You (X) vs Computer (O) ---")
    
    for turn in range(9):
        show_board(board)
        
        if player == "X":
            while True:
                try:
                    choice = int(input(f"Your turn (X). Pick a spot (1-9): "))
                    
                    # Convert user input (1-9) to list index (0-8)
                    index = choice - 1 
                    
                    if 0 <= index <= 8 and board[index] == " ":
                        board[index] = player
                        break 
                    else:
                        print("Spot taken or invalid.")
                except ValueError:
                    print("Numbers only!")
        else:
            print("Computer (O) is thinking...")
            while True:
                # Computer keeps picking random spots until it finds an empty one
                comp_choice = random.randint(0, 8)
                
                if board[comp_choice] == " ":
                    board[comp_choice] = player
                    break

        if check_for_win(board, player):
            show_board(board)
            if player == "X":
                print("You won!")
            else:
                print("Computer won!")
            return

        if player == "X":
            player = "O"
        else:
            player = "X"

    show_board(board)
    print("It's a draw!")

start_game()