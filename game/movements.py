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
        if y == baseSquare and not board[y+(direction*2)][x] and not board[y+direction][x]:
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
        row,col = nightMove
        if 0 <= row < 8 and 0 <= col <8:
            if lookingForCheck:
                if board[row][col] == sameColor(color, board[row][col]):
                    availableMoves.append(strC(row, col))
                    break
                availableMoves.append(strC(row, col))  
            else:
                if sameColor(color, board[row][col]):
                    continue
                availableMoves.append(strC(row,col))
    
    return availableMoves


def straightLegalMoves(pieceCoordinates,board,color,lookingForCheck):
    x = int(pieceCoordinates[1])
    y = int(pieceCoordinates[0])

    availableMoves = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for direction in directions:
        row, col = y + direction[0], x + direction[1]
        while 0 <= row < 8 and 0 <= col < 8:
            if board[row][col]:
                if lookingForCheck:
                    if board[row][col] == sameColor(color, board[row][col]):
                        availableMoves.append(strC(row, col))
                        break
                    availableMoves.append(strC(row, col))
                else:
                    if sameColor(color, board[row][col]):
                        break
                    availableMoves.append(strC(row, col))
                break
            availableMoves.append(strC(row, col))
            row += direction[0]
            col += direction[1]
    return availableMoves

def diagonalLegalMoves(pieceCoordinates,board,color,lookingForCheck):
    x = int(pieceCoordinates[1])
    y = int(pieceCoordinates[0])    
    availableMoves = []
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    for direction in directions:
        row, col = y + direction[0], x + direction[1]
        while 0 <= row < 8 and 0 <= col < 8:
            if board[row][col]:

                if lookingForCheck:
                    if board[row][col] == sameColor(color, board[row][col]):
                        availableMoves.append(strC(row, col))
                        break
                    availableMoves.append(strC(row, col))
                else:
                    if sameColor(color, board[row][col]):
                        break
                    availableMoves.append(strC(row, col))
                break
            availableMoves.append(strC(row, col))
            row += direction[0]
            col += direction[1]
    return availableMoves

def kingLegalMoves(pieceCoordinates,board,color,lookingForCheck):
    x = int(pieceCoordinates[1])
    y = int(pieceCoordinates[0])    
    availableMoves = []
    allKingMoves = [(y+1, x),(y-1, x),(y, x+1),(y, x-1),
                    (y+1, x+1),(y-1, x+1),(y+1, x-1),(y-1, x-1),]
    for kingMove in allKingMoves:
        row,col = kingMove
        if 0 <= row < 8 and 0 <= col < 8:
            if lookingForCheck:
                if board[row][col] == sameColor(color, board[row][col]):
                    availableMoves.append(strC(row, col))
                    break
                availableMoves.append(strC(row, col))
            else: 
                if sameColor(color, board[row][col]):
                    continue
                availableMoves.append(strC(row,col))

    # if checkingForCastling:
    #     print('s')
    #     castleing(movedStatus, color, board)
    return availableMoves

# def castleing(movedStatus,color,board):
#     opponentPieces = []
#     canCastle = False
#     # Light
#     if color:
#         # Short Castle (king side)
#         if not movedStatus[1][1] and not movedStatus[1][2] and board[7][5] == '' and board[7][6] =='' and board[7][7]=='R':
#             for row in range(8):
#                 for col in range(8):
#                     if oppositeColor(color,board[row][col]):
#                         opponentPieces.append((board[row][col]),strC(row,col))
            
#             for piece in opponentPieces:
#                 moves = getLegalMoves(piece[1], board, lookingForCheck=True,kingMoves=None,getOutOfCheckMoves=None,pinnedLegalMoves=None,checkingForCastling=True)
#                 for move in moves:
#                     if move == board[7][4] or move == board[7][5] or move == board[7][6]:
#                         break
#                     else:
#                         canCastle = True


#     print(canCastle)
