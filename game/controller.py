from .movements import pawnLegalMoves,knightLegalMoves,straightLegalMoves,diagonalLegalMoves,kingLegalMoves
# from . import checkCheck
from .helpers import oppositeColor,kingName,strC

def controller(pieceCoordinates,board,turn):
    isKingOnCheck(board, turn)
    return getLegalMoves(pieceCoordinates, board,lookingForCheck=False)

def getLegalMoves(pieceCoordinates,board,lookingForCheck):
    cords = pieceCoordinates
    x = int(pieceCoordinates[1])
    y = int(pieceCoordinates[0])
    pieceName = board[y][x]

    moves = []
    if pieceName.lower() == 'p':
        moves = pawnLegalMoves(cords, board, pieceName.isupper(), lookingForCheck)

    if pieceName.lower() == 'n':
        moves = knightLegalMoves(pieceCoordinates, board, pieceName.isupper(), lookingForCheck)
    
    if pieceName.lower() == 'r':
        moves = straightLegalMoves(pieceCoordinates, board, pieceName.isupper(), lookingForCheck)

    if pieceName.lower() == 'b':
        moves = diagonalLegalMoves(cords, board, pieceName.isupper(), lookingForCheck)

    if pieceName.lower() == 'q':
        moves = straightLegalMoves(cords, board, pieceName.isupper(), lookingForCheck)
        moves += diagonalLegalMoves(cords, board, pieceName.isupper(), lookingForCheck)
    
    if pieceName.lower() == 'k':
        moves = kingLegalMoves(cords, board, pieceName.isupper(), lookingForCheck)

    return moves



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
                    if move == kingCords:
                        isChecked = True

                    if move == kingMove:
                        kingMoves.remove(kingMove)
                        print(f'here.. piece {piece[0]} at {piece[1]} is attacking the king king' )
    return isChecked, kingMoves