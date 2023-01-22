from django.shortcuts import render,redirect
from django.http import JsonResponse


def mainView(request):
    return render(request, 'mainPage.html')


def board(request):
    if 'turn' in request.session:
        turn = request.session['turn']
    else:
        # True light, False dark
        request.session['turn'] = True
        turn = request.session['turn']


    if 'board' in request.session:
        board = request.session['board']
    else:
        request.session['board'] =[
        ["r", "n", "b", "q", "k", "b", "n", "r"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]
        board = request.session['board']


    if is_ajax(request):
        square = request.POST.get('sqId')
        newSquare = request.POST.get('newSqId')
        oldSquare = request.POST.get('oldSqId')
        
        if square:
            return JsonResponse({'moves': getLegalMoves(square, board)})
        if newSquare:
            request.session['board'] = movePieces(oldSquare, newSquare, board)
            request.session['turn'] = not request.session['turn']
            return JsonResponse({'data': ''})

        jsResponseInfo = {
            'board' : board,
            'turn': turn
        }

        return JsonResponse(jsResponseInfo)





def movePieces(oldPlace,newPlace,board):
    # for pawns


    oldCords = int(oldPlace)
    oX = int(oldPlace[1])
    oY = int(oldPlace[0])

    piece = board[oY][oX]
    color = piece.isupper()

    newCords = int(newPlace)
    nX = int(newPlace[1])
    nY = int(newPlace[0])


    # Promotion
    dest = pawnColorMoves(color)[0]
    base = pawnColorMoves(color)[1]
    # the promotion square
    if piece.lower() == 'p' and nY == 6 + (base * dest):
        if color:
            piece = 'Q'
        else:
            piece = 'q'


    board[oY][oX] = ""
    board[nY][nX] = piece
    return board

def resetBoard(request):
    request.session['board'] =[
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
    ]
    request.session['turn'] = True
    return redirect('boardView')

def getLegalMoves(square, board):
    cords = int(square)
    xCord = int(square[1])
    yCord = int(square[0])

    piece = board[yCord][xCord]
    availableMoves = []

    # Pawn Moves
    if piece == 'P' or piece == 'p':
        availableMoves = pawnLegalMoves(xCord, yCord, board, piece.isupper())

        
    # Rook Moves
    if piece == 'R' or piece == 'r':
        availableMoves =  straightLegalMoves(xCord, yCord, board,piece.isupper())

    # Bishop Moves
    if piece == 'B' or piece == 'b':
        availableMoves = diagonalLegalMoves(xCord, yCord, board, piece.isupper())

    # Knight Moves
    if piece == 'N' or piece == 'n':
        availableMoves =  knightLegalMoves(xCord, yCord, board,piece.isupper())

    # Queen Moves
    if piece == 'Q' or piece == 'q':
        availableMoves = straightLegalMoves(xCord, yCord, board, piece.isupper())
        availableMoves += diagonalLegalMoves(xCord, yCord, board, piece.isupper())

    # King Moves
    if piece =='K' or piece == 'k':
        availableMoves = kingLegalMoves(xCord, yCord, board, piece.isupper())

    return availableMoves


def pawnLegalMoves(xCord,yCord,board,color):
    # color True is light || False is dark

    # dest is the direction
    dest = pawnColorMoves(color)[0]
    base = pawnColorMoves(color)[1]
        
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

def kingLegalMoves(xCord,yCord,board,color):
    # color True is light || False is dark
    availableMoves = []
    allKingMoves = [(yCord+1, xCord),(yCord-1, xCord),(yCord, xCord+1),(yCord, xCord-1),
                    (yCord+1, xCord+1),(yCord-1, xCord+1),(yCord+1, xCord-1),(yCord-1, xCord-1),]
    
    for kingMove in allKingMoves:
        j,i = kingMove
        if 0 <= i < 8 and 0 <= j <8:
            if up_inverse(color, board[j][i]):
                continue
            availableMoves.append(strC(j, i))
    return availableMoves

def pawnColorMoves(color):
    results = []
    if color:
        results.append(-1)
        results.append(6)
    else:
        results.append(1)
        results.append(1)
    return results

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