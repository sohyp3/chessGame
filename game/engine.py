from .helpers import sameColor,strC
from .getLegalMoves import getLegalMoves

from .movePieces import movePieces

import math

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

# def aiHandler(board,color):
#     depth = 3
#     pass

    
def MiniMax(board,depth,color,movedStatus,enPassant,captureStatus):
    print('?')
    if depth == 0 :
        return evaluate(board)

    legalMoves = []
    pieces, moves = allMoves(board, color,req = 'all')
    

    # for piece in moves:
    #     print(piece)  
    
    if color:
        max_eval = -math.inf
        for move in moves:
            pass



def allMoves(board,color,**kwargs):
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
            pieceMoves = getLegalMoves(piece[1], board)
            moves.append((piece[0],piece[1],pieceMoves))
        return  pieces ,moves
        
    return pieces