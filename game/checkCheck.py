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
                kingMoves = getLegalMoves(kingCords, board,lookingForCheck=False,kingMoves=None,getOutOfCheckMoves=None,pinnedLegalMoves=None)
                board[row][col]= ''
                

    attackPieces = []
    for piece in opponentPieces:
        moves = getLegalMoves(piece[1], board, lookingForCheck=True, kingMoves=None, getOutOfCheckMoves=None, pinnedLegalMoves=None)
        if not moves:
            continue
        for move in moves:
            if move == kingCords:
                isChecked = True
                if piece not in attackPieces:
                    attackPieces.append(piece)
                    # print(f'here.. piece {piece[0]} at {piece[1]} is attacking the king king')
                break
            if kingMoves:
                for kingMove in kingMoves:
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
            pass
        
        else:
            moves = getLegalMoves(piece, board, lookingForCheck= False, kingMoves=None,getOutOfCheckMoves=None,pinnedLegalMoves=None)
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
        pass
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

def isPinned(piece,turn,board):
    pieceX = int(piece[1])
    pieceY = int(piece[0])
    pieceName = board[pieceY][pieceX]
    availableMoves = []
    isPiecePinned = False
    if pieceName.lower() != 'k':

        # i will get the attackers on the king, then remove the piece and compare, does the attackers add? if yes that means it should be pinned
        oisCheck, okingMoves, okingCords, oattackerPieces= isKingOnCheck(board, turn)

        board[pieceY][pieceX] = ''

        nisCheck, nkingMoves, nkingCords, nattackerPieces = isKingOnCheck(board, turn)

        if len(oattackerPieces) ==len( nattackerPieces):
            availableMoves = None
        else:
            pinner = list(set(nattackerPieces) - set(oattackerPieces))[0][1]
            pinner = strC(pinner[0],pinner[1])
            pieceMoves = getLegalMoves(piece, board, lookingForCheck=False, kingMoves=None, getOutOfCheckMoves=None, pinnedLegalMoves=None)
            line = getLine(piece, pinner)
            line.append(pinner)
            for move in pieceMoves:
                if move in line:
                    availableMoves.append(move)
            isPiecePinned = True
        board[pieceY][pieceX] = pieceName
        return availableMoves
