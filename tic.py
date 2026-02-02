import random
def display_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")
def check_win(board, mark):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == mark:
            return True
    return False
def check_draw(board):
    return " " not in board
def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move. Choose a number from 1 to 9.")
            elif board[move] != " ":
                print("Spot already taken. Choose another one.")
            else:
                board[move] = "X"
                break
        except ValueError:
            print("Please enter a valid number.")
def bot_move(board):
    print("Bot is making a move...")
    # 1. Try to win
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_win(board, "O"):
                return
            board[i] = " "
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_win(board, "X"):
                board[i] = "O"
                return
            board[i] = " "
    available = [i for i in range(9) if board[i] == " "]
    move = random.choice(available)
    board[move] = "O"
def play_game():
    board = [" "] * 9
    print("Welcome to Tic Tac Toe!")
    print("You are X, Bot is O")
    display_board(board)
    while True:
        player_move(board)
        display_board(board)
        if check_win(board, "X"):
            print("🎉 You win! Congratulations!")
            break
        if check_draw(board):
            print("It's a draw!")
            break
        bot_move(board)
        display_board(board)
        if check_win(board, "O"):
            print("🤖 Bot wins! Better luck next time.")
            break
        if check_draw(board):
            print("It's a draw!")
            break
if __name__ == "__main__":
    play_game()
