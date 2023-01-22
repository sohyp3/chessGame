from django.shortcuts import render,redirect
from django.http import JsonResponse

from .extraFunctions import is_ajax
from .legalMoves import kingLegalMoves, straightLegalMoves, diagonalLegalMoves,knightLegalMoves,pawnLegalMoves,pawnColorMoves
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


