from random import randrange

def display_board(board):
    for i in board:
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        print(f"|   {i[0]}   |   {i[1]}   |   {i[2]}   |")
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")


def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move: "))
            if move < 1 or move > 9:
                print("Invalid Move(Choose a number between 1 and 9)")
                continue
            for i in range(3):
                for j in range(3):
                    if board[i][j] == move:
                        board[i][j] = "O"
                        return
            print("That Square is already taken.Try again")
        except ValueError:
            print("Please enter a number.")


def make_list_of_free_fields(board):
    free = []
    for i in range(3):
        for j in range(3):
            if isinstance(board[i][j], int):
                free.append((i, j))
    return free


def victory_for(board, sign):
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)) or all(board[j][i] == sign for j in range(3)):
            return True

        if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
            return True


def draw_move(board):
    free = make_list_of_free_fields(board)
    if free:
        row, col = free[randrange(len(free))]
        board[row][col] = 'X'


board = [[(3 * i + j + 1) for j in range(3)] for i in range(3)]

board[1][1] = 'X'

while True:
    display_board(board)
    if victory_for(board, 'X'):
        print("Computer wins!")
        break

    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break

    enter_move(board)
    display_board(board)

    if victory_for(board, 'O'):
        print("You won!")
        break

    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break

    draw_move(board)