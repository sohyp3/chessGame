from django.shortcuts import render, redirect
from django.http import JsonResponse

from .extraFunctions import is_ajax

from .controller import controller
from .helpers import pawnColorMoves
from .handlers import promotionHandler,enPassantHandler,castleHandler
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

    if 'movedStatus' in request.session:
        movedStatus = request.session['movedStatus']
    else:
        # First element for dark, second for light
        # 00r - 04k - 07r || 70R - 74K - 77R 
        request.session['movedStatus'] = [(False,False,False),(False,False,False)]
        movedStatus = request.session['movedStatus']

    if 'enPassant' in request.session:
        enPassant = request.session['enPassant']
    else:
        request.session['enPassant'] = False,"",""
        enPassant = request.session['enPassant']

    if 'captureStatus' in request.session:
        captureStatus = request.session['captureStatus']
    else:
        request.session['captureStatus'] = [(),()]
        enPassant = request.session['captureStatus']


    if is_ajax(request):
        square = request.POST.get('sqId')

        newSquare = request.POST.get('newSqId')
        oldSquare = request.POST.get('oldSqId')

        jsResponseInfo = {
            'board': board,
            'turn': turn
        }

        if square:
            moves, checkMate,draw = controller(square, board, turn,movedStatus,enPassant)
            return JsonResponse({'moves': moves,'checkMate':checkMate, 'draw':draw})

        if newSquare:
            request.session['board'] = movePieces(oldSquare, newSquare, board,movedStatus,enPassant)
            request.session['turn'] = not request.session['turn']
            turn = request.session['turn']
            newRs= {
                'board':board,
                'turn':turn
            }
            return JsonResponse(newRs)

        return JsonResponse(jsResponseInfo)


def movePieces(oldPlace, newPlace, board,movedStatus,enPassant):

# check for legal moves

    oldCords = int(oldPlace)
    oX = int(oldPlace[1])
    oY = int(oldPlace[0])

    piece = board[oY][oX]
    color = piece.isupper()

    newCords = int(newPlace)
    nX = int(newPlace[1])
    nY = int(newPlace[0])

    dest = pawnColorMoves(color)[0]
    base = pawnColorMoves(color)[1]

    piece = promotionHandler(piece, base, dest, color, nY)    
    enPassantHandler(oldPlace, newPlace, board,base,dest,enPassant)
    if castleHandler(oldPlace, newPlace, movedStatus, board):
        board[oY][oX] = ""
        board[nY][nX] = piece


    return board

def resetBoard(request):
    request.session['board'] = [
            ["r", "n", "b", "q", "k", "b", "n", ""],
            ["p", "p", "p", "p", "p", "p", "p", "P"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "", "", "", "K", "", "", "R"]
        ]
    request.session['turn'] = True
    request.session['movedStatus'] = [(False,False,False),(False,False,False)]

    request.session['enPassant'] = False,"",""
    request.session['captureStatus'] = [(),()]

    return redirect('boardView')