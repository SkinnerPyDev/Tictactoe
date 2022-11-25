board = ["_","_","_",
         "_","_","_",
         "_","_","_"]

player1 = input("Enter the name of player 1: ")
player2 = input("Enter the name of plaer 2: ")
print()
currentPlayer = "X"
player_names = player1
winner = None
game_running = True


def printBoard(board):
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("__________")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("__________")
    print(board[6]+" | "+board[7]+" | "+board[8])


def playerInput(board):
    inp = int(input(f"\n{player_names.capitalize()}'s ({currentPlayer}) turn enter 1-9: "))
    print()
    if inp >=1 and inp<=9:
        if board[inp-1]=="_":
            board[inp-1] = currentPlayer
        else:
            print("Player is already in that spot")
            print()
            switchplayer()
    else:
        print("Out of range please enter 1-9: ")
        print()
        switchplayer()


def checkHori(board):
    global winner

    if board[0] == board[1] == board[2] and board[1]!= "_":
        winner = board[0]
        return True

    elif board[3] == board[4] == board[5] and board[3]!= "_":
        winner = board[3]
        return True

    elif board[6] == board[7] == board[8] and board[6]!= "_":
        winner = board[6]
        return True
def checkRow(board):
    global winner

    if board[0] == board[3]==board[6] and board[0]!="_":
        winner = board[0]
        return True

    elif board[1] == board[4]==board[7] and board[1]!="_":
        winner = board[1]
        return True

    elif board[2] == board[5]==board[8] and board[2]!="_":
        winner = board[2]
        return True

def checkDiaa(baord):
    global winner

    if baord[0] == baord[4] == board[8] and board[0]!= "_":
        winner = baord[0]
        return True
    elif baord[2] == baord[4] == board[6] and board[2]!= "_":
        winner = baord[2]
        return True

def tie(baord):
    global game_running
    if "_" not in baord:
        printBoard(board)
        print("\nIts a tie")
        print()
        game_running = False

def cheakwin():
    global game_running
    if checkHori(board) or checkDiaa(board) or checkRow(board):
        printBoard(board)
        print(f'\nThe winner is {player_names.capitalize()}')
        game_running = False


def switchplayer():
    global currentPlayer
    global player_names
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
    if player_names == player1:
        player_names = player2
    else:
        player_names = player1


while game_running:
    printBoard(board)
    playerInput(board)
    cheakwin()
    tie(board)
    switchplayer()
print("Thank you for playing")
print()


