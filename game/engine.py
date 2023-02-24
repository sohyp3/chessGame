from .helpers import sameColor,strC
from .getLegalMoves import getLegalMoves

from .handlers import promotionHandler

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
    
def MiniMax(board,depth,color):
    if depth == 0 :
        return evaluate(board,color),None

    pieces, moves = allMoves(board, color,req = 'all')
    best_move = ''
    best_piece = ''


    if color:
        max_eval = -math.inf
        for move in moves:
            for newPlace in move[2]:
                oX = int(newPlace[1])
                oY = int(newPlace[0])
                oldPiece = board[oY][oX]
                mover(move[1], newPlace, board)
                eval = MiniMax(board, depth-1, False)[0]
                mover(newPlace, move[1], board)
                board[oY][oX] = oldPiece
                if eval > max_eval:
                    max_eval = eval
                    bestMove = (move[1],newPlace)
                    best_move = newPlace
                    best_piece = move[0]
                    best_piece_loc = move[1]


                # print(f"best move is moving {move[0]}  from {move[1]} to {best_move} || {move[2]}")
        # print(f'{best_piece} from {best_piece_loc} - to {best_move} eval is : {max_eval}' )
        return max_eval,bestMove
    else:
        min_eval = math.inf
        for move in moves:
            for newPlace in move[2]:
                oX = int(newPlace[1])
                oY = int(newPlace[0])
                oldPiece = board[oY][oX]

                mover(move[1], newPlace, board)
                eval = MiniMax(board, depth-1, True)[0]
                mover(newPlace, move[1], board)
                board[oY][oX] = oldPiece

                if eval < min_eval:
                    bestMove = (move[0],move[1],newPlace)

                    min_eval = eval
                    best_move = newPlace
                    best_piece = move[0]
                    best_piece_loc = move[1]
        # print(f'{best_piece} from {best_piece_loc} - to {best_move} eval {eval} ')
        return min_eval,bestMove

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

def printi(board,depth,color):
    print(MiniMax(board, depth, color))

def mover(oldPlace,newPlace,board):
    nX = int(newPlace[1])
    nY = int(newPlace[0])

    oX = int(oldPlace[1])
    oY = int(oldPlace[0])
    piece = board[oY][oX]
    
    board[oY][oX] = ""
    board[nY][nX] = piece