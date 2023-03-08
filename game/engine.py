from .helpers import sameColor,strC
from .getLegalMoves import getLegalMoves

from .controller import controller
from .handlers import promotionHandler

import math,random

def evaluate(board,color):
    pieceVal = {
        'P':1,
        'N':3,
        'B':3,
        'R':5,
        'Q':9,
        'K':90,
        'p':-1,
        'n':-3,
        'b':-3,
        'r':-5,
        'q':-9,
        'k':-90,
    }

    whitePieces = allMoves(board, color)
    blackPieces = allMoves(board, not color)

    pieces = whitePieces + blackPieces
    evalBar = 0

    for piece in pieces:
        evalBar += pieceVal[piece[0]]

    return evalBar
    
counter = 0
def MiniMax(board, depth, alpha, beta, color):
    global counter

    checkMate = False
    Draw = False

    if depth == 0 or checkMate or Draw:
        counter += 1
        return evaluate(board, color), None, counter

    pieces, moves, checkMate, Draw = allMoves(board, color, req='all')

    bestMove = random.choice(moves)
    eval = None

    if color:
        max_eval = -math.inf
        for move in moves:
            for newPlace in move[2]:
                counter += 1
                oX = int(newPlace[1])
                oY = int(newPlace[0])
                oldPiece = board[oY][oX]

                mover(move[1], newPlace, board, color)
                eval = MiniMax(board, depth-1, alpha, beta, False)[0]
                mover(newPlace, move[1], board, color)
                board[oY][oX] = oldPiece

                if eval > max_eval:
                    max_eval = eval
                    bestMove = (move[0], move[1], newPlace)

                alpha = max(alpha, eval)
                if beta <= alpha:
                    break

        return max_eval, bestMove, counter

    else:
        min_eval = math.inf
        for move in moves:
            for newPlace in move[2]:
                oX = int(newPlace[1])
                oY = int(newPlace[0])
                oldPiece = board[oY][oX]

                mover(move[1], newPlace, board, color)
                eval = MiniMax(board, depth-1, alpha, beta, True)[0]
                mover(newPlace, move[1], board, color)
                board[oY][oX] = oldPiece

                if eval < min_eval:
                    bestMove = (move[0], move[1], newPlace)
                    min_eval = eval

                beta = min(beta, eval)
                if beta <= alpha:
                    break

        return min_eval, bestMove, counter

def allMoves(board,color,**kwargs):
    movedStatus = [(False,False,False),(False,False,False)]
    enPassant = False,"",""

    req = None
    if 'req' in kwargs:
        req = kwargs['req']
    

    pieces = []
    moves = []
    for row in range(8):
        for col in range(8):
            if sameColor(color,board[row][col]):
                pieces.append((board[row][col],strC(row,col)))
    
    if req == 'all':
        for piece in pieces:
            # pieceMoves = getLegalMoves(piece[1], board)
            controllerResult = controller(piece[1], board, color, movedStatus, enPassant)
            pieceMoves = controllerResult[0]
            checkMate = controllerResult[1]
            Draw = controllerResult[2]
            moves.append((piece[0],piece[1],pieceMoves))
        return  pieces ,moves,checkMate,Draw
        
    return pieces


def mover(oldPlace,newPlace,board,color):
    nX = int(newPlace[1])
    nY = int(newPlace[0])

    oX = int(oldPlace[1])
    oY = int(oldPlace[0])

    piece = board[oY][oX]
    # piece = promotionHandler(piece, color, nY)

    board[oY][oX] = ""
    board[nY][nX] = piece