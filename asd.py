def convert(x, b):
    if x == 0:
        return "0"
    elif x < 0:
        return "-" + convert(-x, b)
    else:
        return convert(x // b, b) + str(x % b)
print (convert(5, 3))

def perfect_squares(n):
    squares = []
    for i in range(1, n):
        if i * i < n:
            squares.append(i * i)
    return squares
print(perfect_squares(300))



def tic_tac_toe():
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    player = 'X'
    for i in range(9):
        print_board(board)
        print("Player " + player + " turn")
        move = input("Enter a number between 1 and 9: ")
        move = int(move)
        if move < 1 or move > 9:
            print("Invalid move")
            continue
        row = (move - 1) // 3
        col = (move - 1) % 3
        if board[row][col] == ' ':
            board[row][col] = player
        else:
            print("Invalid move")
            continue
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
    print_board(board)

def print_board(board):
    for row in board:
        print(row)

print(tic_tac_toe())
