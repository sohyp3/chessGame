from .helpers import strC,sameColor, oppositeColor

def pawnLegalMoves(pieceCoordinates,board,color,lookingForCheck):
    x = int(pieceCoordinates[1])
    y = int(pieceCoordinates[0])
    direction,baseSquare = pawnColorMoves(color)
    availableMoves = []

    print('pawn')
    if lookingForCheck:
        # diagonal attacks
        if x > 0:
            availableMoves.append(strC(y+direction,x-1))
        if x <7:
            availableMoves.append(strC(y+direction,x+1))
    
    else:
        # forward move
        if not board[y+direction][x]:
            availableMoves.append(strC(y+direction, x))
        if y == baseSquare and not board[y+(direction*2)][x]:
            availableMoves.append(strC(y+(direction*2), x))
        
        # capture diagonal
        if x > 0 and board[y+direction][x-1] and oppositeColor(color, board[y+direction][x-1]):
            availableMoves.append(strC(y+direction,x-1))
        if x < 7 and board[y+direction][x+1] and oppositeColor(color, board[y+direction][x+1]):
            availableMoves.append(strC(y+direction,x+1))
        
    
    return availableMoves






# Dark Pieces move down 
# Light Pieces move up
def pawnColorMoves(color):
    if color:
        direction = -1
        baseSquare = 6
    else:
        direction =  1
        baseSquare = 1
    return direction,baseSquare
