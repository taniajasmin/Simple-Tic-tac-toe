def win(s):
    board = [cells[0:3], cells[3:6], cells[6:9]]
    if board[0][0] == s and board[0][1] == s and board[0][2] == s: return True
    if board[1][0] == s and board[1][1] == s and board[1][2] == s: return True
    if board[2][0] == s and board[2][1] == s and board[2][2] == s: return True
    if board[0][0] == s and board[1][0] == s and board[2][0] == s: return True
    if board[0][1] == s and board[1][1] == s and board[2][1] == s: return True
    if board[0][2] == s and board[1][2] == s and board[2][2] == s: return True
    if board[0][0] == s and board[1][1] == s and board[2][2] == s: return True
    if board[0][2] == s and board[1][1] == s and board[2][0] == s: return True
    return False


cells = input("Enter cells:")
print("---------", end="\r")
print('|', *cells[0:3], sep=" ", end=" |\r")
print('|', *cells[3:6], sep=" ", end=" |\r")
print('|', *cells[6:9], sep=" ", end=" |\r")
print("---------")

nb_X = cells.count("X")
nb_O = cells.count("O")
nb_empty_grid = cells.count("_") + cells.count(" ")

if (win("X") and win("O")) or (abs(nb_O - nb_X) >= 2):
    print("Impossible")
    exit()

if not win("X") and not win("O"):
    if nb_empty_grid > 0:
        print("Game not finished")
        exit()
    if nb_empty_grid == 0:
        print("Draw")
        exit()

if win("X"):
    print("X wins")
    exit()

if win("O"):
    print("O wins")
    exit()
