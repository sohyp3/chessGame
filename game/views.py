from django.shortcuts import render
from django.http import JsonResponse


def mainView(request):
    return render(request, 'mainPage.html')


def board(request):
    board = [
        ["r", "n", "b", "q", "k", "b", "n", "r"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["R", "N", "B", "Q", "K", "B", "N", "R"]
    ]

    if is_ajax(request):
        square = request.POST.get('sqId')
        if square:
            return JsonResponse({'moves': getLegalMoves(square, board)})
        return JsonResponse({'data': board})


def getLegalMoves(square, board):
    cords = int(square)
    xCord = int(square[1])
    yCord = int(square[0])

    piece = board[yCord][xCord]
    availableMoves = []

    # Light Pawn Moves
    if piece == 'P':
        availableMoves = pawnLegalMoves(xCord, yCord, board, True)
    if piece == 'p':
        availableMoves = pawnLegalMoves(xCord, yCord, board, False)
        

    # Rook Moves
    if piece == 'R':
        availableMoves =  straightLegalMoves(xCord, yCord, board,True)

    if piece == 'r':
        availableMoves =  straightLegalMoves(xCord, yCord, board,False)


    # Bishop Moves
    if piece == 'B':
        availableMoves = diagonalLegalMoves(xCord, yCord, board, True)

    if piece == 'b':
        availableMoves = diagonalLegalMoves(xCord, yCord, board, False)

    # Light kNite Moves
    if piece == 'N':
        availableMoves =  knightLegalMoves(xCord, yCord, board,True)
    
    if piece == 'n':
        availableMoves =  knightLegalMoves(xCord, yCord, board,False)


    # Light Queen



    return availableMoves


def pawnLegalMoves(xCord,yCord,board,color):
    # color True is light || False is dark

    if color:
        dest = -1
        base = 6
    else:
        dest = 1
        base = 1
        
    availableMoves = []
    # up moves
    if not board[yCord+dest][xCord]:
        availableMoves.append(strC(yCord+ dest, xCord))

    # first move
    if yCord == base and not board[yCord+ dest][xCord] and not board[yCord+ (dest*2)][xCord]:
        availableMoves.append(strC(yCord+(dest*2), xCord))

    # capture diagonal
    if xCord > 0 and board[yCord+ dest][xCord-1] and low_inverse(color,  board[yCord+ dest][xCord-1]):
        availableMoves.append(strC(yCord+ dest, xCord-1))

    if xCord < 7 and board[yCord+ dest][xCord+1] and low_inverse(color, board[yCord+ dest][xCord+1]):
        availableMoves.append(strC(yCord+ dest, xCord+1))
    return availableMoves    


def knightLegalMoves (xCord,yCord,board,color):
    # color True is light || False is dark

    availableMoves = []
    allNightMoves = [(yCord +1, xCord +2), (yCord -1, xCord +2), (yCord +1, xCord -2), (yCord -1, xCord -2),
                (yCord +2, xCord +1), (yCord +2, xCord -1), (yCord -2, xCord +1),(yCord -2, xCord -1)]

    for nightMove in allNightMoves:
        j,i = nightMove
        if 0 <= i < 8 and 0 <= j <8:
            if up_inverse(color, board[j][i]):
                continue
            availableMoves.append(strC(j, i))
    return availableMoves


def diagonalLegalMoves(xCord,yCord,board,color):
    # color True is light || False is dark
    availableMoves = []

    # top-left
    i = xCord-1
    j = yCord-1
    while i >= 0 and j >= 0:
        if up_inverse(color, board[j][i]):
            break
        elif low_inverse(color, board[j][i]):
            availableMoves.append(strC(j, i))
            break
        elif not board[j][i]:
            availableMoves.append(strC(j, i))

        i -= 1
        j -= 1

    # top-right
    i = xCord+1
    j = yCord-1

    while i < 8 and j >= 0:
        if up_inverse(color, board[j][i]):
            break
        elif low_inverse(color, board[j][i]):
            availableMoves.append(strC(j, i))
            break
        elif not board[j][i]:
            availableMoves.append(strC(j, i))
        i += 1
        j -= 1

    # bottom right
    i = xCord + 1
    j = yCord + 1

    while i < 8 and j < 8:
        if up_inverse(color, board[j][i]):
            break
        elif low_inverse(color, board[j][i]):
            availableMoves.append(strC(j, i))
            break
        elif not board[j][i]:
            availableMoves.append(strC(j, i))
        i += 1
        j += 1

    # bottom left
    i = xCord - 1
    j = yCord + 1

    while i >= 0 and j < 8:
        if up_inverse(color, board[j][i]):
            break
        elif low_inverse(color, board[j][i]):
            availableMoves.append(strC(j, i))
            break
        elif not board[j][i]:
            availableMoves.append(strC(j, i))
        i -= 1
        j += 1    

    return availableMoves

def straightLegalMoves(xCord,yCord,board,color):
    # color True is light || False is dark

    availableMoves = []
    # upper move
    for i in range(yCord-1, -1, -1):
        if up_inverse(color, board[i][xCord]): 
            break
        if low_inverse(color, board[i][xCord]):
            availableMoves.append(strC(i, xCord))
            break
        elif not board[i][xCord]:
            availableMoves.append(strC(i, xCord))
    # lower moves
    for i in range(yCord+1, 8):
        if up_inverse(color,board[i][xCord]):
            break
        elif low_inverse(color, board[i][xCord]):
            availableMoves.append(strC(i, xCord))
            break
        elif not board[i][xCord]:
            availableMoves.append(strC(i, xCord))

    # right moves
    for i in range(xCord+1, 8):
        if up_inverse(color,board[yCord][i]):
            break
        elif low_inverse(color, board[yCord][i]):
            availableMoves.append(strC(yCord, i))
            break
        elif not board[yCord][i]:
            availableMoves.append(strC(yCord, i))

    # left moves
    for i in range(xCord-1, -1, -1):
        if up_inverse(color,board[yCord][i]):
            break
        elif low_inverse(color, board[yCord][i]):
            availableMoves.append(strC(yCord, i))
            break
        elif not board[yCord][i]:
            availableMoves.append(strC(yCord, i))    
    
    return availableMoves


# The mechanism i decide the friendly pieces vs enemy pieces is by checking if they are upper or lower
# Light Colored pieces are upper case, dark colored pieces are lower case
# Instead of rewriting the code for each color
# I can inverse the result when i call the function to check the legal move.
def up_inverse(switcher,string):
    if switcher:
        return string.isupper()
    else:
        if string:
            return not string.isupper()

def low_inverse(switcher,string):
    if  switcher:
        return  string.islower()
    else:
        if string:
            return not string.islower()

# i send and recieve the cords in 2 diget string for example 50
# first diget (5) is the y value, and second diget (0) is the x value
# instead of converting evertime while appending the available moves
# i send it here for to be less messy..
# instead of str(yCord-1)+str(xCord)  strC(yCord-1,xCord)
def strC(y, x):
    return str(y)+str(x)


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
