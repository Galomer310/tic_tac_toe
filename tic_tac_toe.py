board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

def display_board():
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print("--+---+--")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print("--+---+--")
    print(f"{board[7]} | {board[8]} | {board[9]}")

def player_input(player):
    while True:
        choice = input(f"{player},where would you like to put your mark 1-9 ?\n")
        if choice in [str(i) for i in range(1, 10)] and board[int(choice)] == ' ':
            board[int(choice)] = 'x' if player == 'player1' else 'o'
            break
        else:
            print("Invalid input, please try again.")


def check_win(player):
    mark = 'x' if player == 'player1' else 'o'

    win_conditions = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
        [1, 5, 9], [3, 5, 7]              # Diagonals
    ]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == mark:

            return True
    return False

def play():
    display_board()
    for turn in range(9):
        player = 'player1' if turn % 2 == 0 else 'player2'
        player_input(player)
        display_board()

        if check_win(player):
            print(f"{player} wins!")
            return
    print("it's a draw!")

play()
