from .helpers import strC, sameColor, oppositeColor, pawnColorMoves, kingName


def pawnLegalMoves(pieceCoordinates, board, color, lookingForCheck):
    x = int(pieceCoordinates[1])
    y = int(pieceCoordinates[0])
    direction, baseSquare = pawnColorMoves(color)
    availableMoves = []

    if lookingForCheck:
        # diagonal attacks
        if x > 0:
            availableMoves.append(strC(y+direction, x-1))
        if x < 7:
            availableMoves.append(strC(y+direction, x+1))

    else:
        # forward move
        if not board[y+direction][x]:
            availableMoves.append(strC(y+direction, x))
        if y == baseSquare and not board[y+(direction*2)][x]:
            availableMoves.append(strC(y+(direction*2), x))

        # capture diagonal
        if x > 0 and board[y+direction][x-1] and oppositeColor(color, board[y+direction][x-1]):
            availableMoves.append(strC(y+direction, x-1))
        if x < 7 and board[y+direction][x+1] and oppositeColor(color, board[y+direction][x+1]):
            availableMoves.append(strC(y+direction, x+1))

    return availableMoves


def knightLegalMoves(pieceCoordinates, board, color, lookingForCheck):
    x = int(pieceCoordinates[1])
    y = int(pieceCoordinates[0])

    availableMoves = []
    allNightMoves = [(y + 1, x + 2), (y - 1, x + 2), (y + 1, x - 2), (y - 1, x - 2),
                    (y + 2, x + 1), (y + 2, x - 1), (y - 2, x + 1), (y - 2, x - 1)]
    for nightMove in allNightMoves:
        j,i = nightMove
        if 0 <= j < 8 and 0 <= i <8:
            if sameColor(color, board[j][i]):
                continue
            availableMoves.append(strC(j,i))
    
    return availableMoves


def straightLegalMoves(pieceCoordinates,board,color,lookingForCheck):
    x = int(pieceCoordinates[1])
    y = int(pieceCoordinates[0])

    availableMoves = []

    # Upper Moves
    for i in range(y-1,-1,-1):
        if sameColor(color, board[i][x]):
            break
        elif oppositeColor(color, board[i][x]):
            if lookingForCheck and board[i][x]:
                return 'onCheck' 
                
            availableMoves.append(strC(i,x))
            break
        elif not board[i][x]:
            availableMoves.append(strC(i,x))
    
    return availableMoves