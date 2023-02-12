from .movements import pawnLegalMoves,knightLegalMoves,straightLegalMoves,diagonalLegalMoves,kingLegalMoves
# from . import checkCheck
from .helpers import oppositeColor,kingName,strC

def controller(pieceCoordinates,board,turn):
    isCheck, kingMoves, kingCords, attackerPieces= isKingOnCheck(board, turn)
    if isCheck:
        pass
    return getLegalMoves(pieceCoordinates, board,lookingForCheck=False,kingMoves=kingMoves)

def getLegalMoves(pieceCoordinates,board,lookingForCheck,kingMoves):
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
        if kingMoves != None:
            moves = kingMoves            

    return moves

def getOutOfCheck(pieceCoordinates,attackingPieces,kingCordinates,board):
    x = int(pieceCoordinates[1])
    y = int (pieceCoordinates[0])
    availablemoves = []

    for attacker in attackingPieces:
        print(attacker)
    

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
                kingMoves = getLegalMoves(kingCords, board,lookingForCheck=False,kingMoves=None)

    
    for piece in opponentPieces:
        moves = getLegalMoves(piece[1], board, lookingForCheck=True,kingMoves=None)
        if not moves:
            continue
        for move in moves:
            if kingMoves:
                for kingMove in kingMoves:
                    if move == kingCords:
                        isChecked = True
                        attackPieces.append(piece)
                        print(f'here.. piece {piece[0]} at {piece[1]} is attacking the king king' )
                        break
                    if move == kingMove:
                        kingMoves.remove(kingMove)
                        attackPieces.append(piece)
    return isChecked, kingMoves, kingCords, attackPieces