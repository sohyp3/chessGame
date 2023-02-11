from .helpers import strC, kingName,piecesName,oppositeColor,sameColor
from .controller import getLegalMoves

def isKingOnCheck(board,color):
    opponentPieces = []
    kingMoves = []
    attackPieces = []
    isChecked = False

    for row in range(8):
        for col in range(8):
            if oppositeColor(color, board[row][col]):
                opponentPieces.append((board[row][col],strC(row,col)))

            if board[row][col] == kingName(color):
                kingCords = strC(row, col)
                kingMoves = getLegalMoves(kingCords, board,lookingForCheck=False)
    
    for piece in opponentPieces:
        moves = getLegalMoves(piece[1], board, lookingForCheck=True)
        if not moves:
            continue
        for move in moves:
            if kingMoves:
                for kingMove in kingMoves:
                    if move == kingMove:
                        print(f'here.. piece {piece[0]} at {piece[1]} is attacking the king king' )
    return isChecked, kingMoves