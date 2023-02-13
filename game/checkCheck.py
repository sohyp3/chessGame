from .helpers import strC, kingName,oppositeColor
from .getLegalMoves import getLegalMoves
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
                kingMoves = getLegalMoves(kingCords, board,lookingForCheck=False,kingMoves=None,getOutOfCheckMoves=None)
                board[row][col]= ''
                

    for piece in opponentPieces:
        moves = getLegalMoves(piece[1], board, lookingForCheck=True,kingMoves=None,getOutOfCheckMoves=None)
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

    # Setting the King on the board again
    board[int(kingCords[0])][int(kingCords[1])] = kingName(color)
    return isChecked, kingMoves, kingCords, attackPieces

def getOutOfCheck(piece,attackerPieces,board,kingCords):
    x = int(piece[1])
    y = int(piece[0])

    availableMoves = []
    if len(attackerPieces)< 2:
        if board[y][x].lower() == 'k':
            print('shing')
        else:
            moves = getLegalMoves(piece, board, lookingForCheck= False, kingMoves=None,getOutOfCheckMoves=None)
            for move in moves:
                # in attackerPieces [0] pieceName [1] pieceCords
                # first [0] to select the first and only item in the list second [1] to select the cords of the attacker piecew

                # Capture
                if move == attackerPieces[0][1]:
                    availableMoves.append(move)

                # block
                attackLine = getLine(kingCords, attackerPieces[0][1])
                if attackLine and move in attackLine:
                    availableMoves.append(move)
    else:
        for attacker in attackerPieces:
            if board[y][x].lower() == 'k':
                continue

            else:
                moves = getLegalMoves(piece, board, lookingForCheck= False, kingMoves=None,getOutOfCheckMoves=None)
        
    print(availableMoves)
    return availableMoves

def getLine(start, end):
    startX = int(start[1])
    startY = int(start[0])
    endX = int(end[1])
    endY = int(end[0])
    line = []

    # straight X axis
    if startX == endX:
        # step is the direction 
        if endY > startY:
            step = 1
        else:
            step = -1
        for i in range(startY+step, endY, step):
            line.append(strC(i, startX))

    # straight Y axis
    elif startY == endY:
        if endX > startX:
            step = 1
        else: 
            step = -1
        for i in range(startX+step, endX, step):
            line.append(strC(startY, i))

    # diagonal 

    elif abs(startX - endX) == abs(startY - endY):
        if endX > startX:
            stepX = 1
        else:
            stepX = -1
        if endY > startY:
            stepY = 1
        else:
            stepY = -1

        for i in range(startX+stepX, endX, stepX):
            startY +=  stepY
            line.append(strC(startY, i))


    return line