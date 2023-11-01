board = [" " for _ in range(9)]


def table():
    for i in range(0, 9, 3):
        print(board[i] + " | " + board[i + 1] + " | " + board[i + 2])
        if i < 6:
            print("--+---+--")


def check_winner(player):

    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
        return True
    return False


current_player = "X"
while True:
    table()
    print("Игрок " + current_player)

    while True:
        move = input("Выберите место для хода (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move) - 1] == " ":
            move = int(move) - 1
            break
        else:
            print("Некорректный ход")

    board[move] = current_player

    if check_winner(current_player):
        table()
        print("Победил игрок " + current_player + "!")
        break

    if " " not in board:
        table()
        print("Ничья!")
        break

    current_player = "O" if current_player == "X" else "X"