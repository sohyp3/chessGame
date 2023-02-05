from django.shortcuts import render, redirect
from django.http import JsonResponse

from .extraFunctions import is_ajax
from .legalMoves import moveController ,getLegalMoves, kingLegalMoves, straightLegalMoves, diagonalLegalMoves, knightLegalMoves, pawnLegalMoves, pawnColorMoves, isKingOnCheck

from .controller import controller

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
        request.session['board'] = [
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

        jsResponseInfo = {
            'board': board,
            'turn': turn
        }

        if square:
            return JsonResponse({'moves': controller(square, board, turn)})

        if newSquare:
            request.session['board'] = movePieces(oldSquare, newSquare, board)
            request.session['turn'] = not request.session['turn']
            turn = request.session['turn']
            newRs= {
                'board':board,
                'turn':turn
            }
            return JsonResponse(newRs)

        return JsonResponse(jsResponseInfo)


def movePieces(oldPlace, newPlace, board):

# check for legal moves

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
    request.session['board'] = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "K", "", "r"],
            ["", "", "", "", "", "", "", ""],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "", "B", "N", "R"]
        ]
    request.session['turn'] = True
    return redirect('boardView')