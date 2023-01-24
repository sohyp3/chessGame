from .extraFunctions import strC, up_inverse,low_inverse

def pawnLegalMoves(xCord,yCord,board,color,lFC):
    # color True is light || False is dark

    # dest is the direction
    dest = pawnColorMoves(color)[0]
    base = pawnColorMoves(color)[1]
        
    availableMoves = []
    

    if lFC:
        # capture diagonal
        if xCord > 0 :
            availableMoves.append(strC(yCord+ dest, xCord-1))

        if xCord < 7 :
            availableMoves.append(strC(yCord+ dest, xCord+1))
    else:
        # up moves
        if not board[yCord+dest][xCord]:
            availableMoves.append(strC(yCord+ dest, xCord))

        # first move
        if yCord == base and not board[yCord+ dest][xCord] and not board[yCord+ (dest*2)][xCord]:
            availableMoves.append(strC(yCord+(dest*2), xCord))


        # capture diagonal
        if xCord > 0 and board[yCord+ dest][xCord-1] and low_inverse(color,  board[yCord+ dest][xCord-1]):
            availableMoves.append(strC(yCord+ dest, xCord-1))

        if xCord < 7 and board[yCord+ dest][xCord+1] and low_inverse(color, board[yCord+ dest][xCord+1]):
            availableMoves.append(strC(yCord+ dest, xCord+1))
    return availableMoves    

def knightLegalMoves (xCord,yCord,board,color,lFC):
    # color True is light || False is dark

    availableMoves = []
    allNightMoves = [(yCord +1, xCord +2), (yCord -1, xCord +2), (yCord +1, xCord -2), (yCord -1, xCord -2),
                (yCord +2, xCord +1), (yCord +2, xCord -1), (yCord -2, xCord +1),(yCord -2, xCord -1)]

    for nightMove in allNightMoves:
        j,i = nightMove
        if 0 <= i < 8 and 0 <= j <8:
            if lFC:
                if up_inverse(color, board[j][i]):
                    availableMoves.append(strC(j, i))
            if up_inverse(color, board[j][i]):
                continue
            availableMoves.append(strC(j, i))
    return availableMoves

def diagonalLegalMoves(xCord,yCord,board,color,lFC):
    # color True is light || False is dark
    availableMoves = []

    # top-left
    i = xCord-1
    j = yCord-1
    while i >= 0 and j >= 0:
        if lFC:
            if up_inverse(color, board[j][i]):
                availableMoves.append(strC(j, i))
                break

        if up_inverse(color, board[j][i]):
            break
        elif low_inverse(color, board[j][i]):
            availableMoves.append(strC(j, i))
            break
        elif not board[j][i]:
            availableMoves.append(strC(j, i))

        i -= 1
        j -= 1

    # top-right
    i = xCord+1
    j = yCord-1

    while i < 8 and j >= 0:
        if lFC:
            if up_inverse(color, board[j][i]):
                availableMoves.append(strC(j, i))
                break
        if up_inverse(color, board[j][i]):
            break
        elif low_inverse(color, board[j][i]):
            availableMoves.append(strC(j, i))
            break
        elif not board[j][i]:
            availableMoves.append(strC(j, i))
        i += 1
        j -= 1

    # bottom right
    i = xCord + 1
    j = yCord + 1

    while i < 8 and j < 8:
        if lFC:
            if up_inverse(color, board[j][i]):
                availableMoves.append(strC(j, i))
                break
        if up_inverse(color, board[j][i]):
            break
        elif low_inverse(color, board[j][i]):
            availableMoves.append(strC(j, i))
            break
        elif not board[j][i]:
            availableMoves.append(strC(j, i))
        i += 1
        j += 1

    # bottom left
    i = xCord - 1
    j = yCord + 1

    while i >= 0 and j < 8:
        if lFC:
            if up_inverse(color, board[j][i]):
                availableMoves.append(strC(j, i))
                break
        if up_inverse(color, board[j][i]):
            break
        elif low_inverse(color, board[j][i]):
            availableMoves.append(strC(j, i))
            break
        elif not board[j][i]:
            availableMoves.append(strC(j, i))
        i -= 1
        j += 1    

    return availableMoves

def straightLegalMoves(xCord,yCord,board,color,lFC):
    # color True is light || False is dark
    availableMoves = []
    # upper move
    for i in range(yCord-1, -1, -1):
        if lFC:
            if up_inverse(color, board[i][xCord]): 
                availableMoves.append(strC(i, xCord))
                break    
        if up_inverse(color, board[i][xCord]): 
            break
        if low_inverse(color, board[i][xCord]):
            availableMoves.append(strC(i, xCord))
            break
        elif not board[i][xCord]:
            availableMoves.append(strC(i, xCord))
    # lower moves
    for i in range(yCord+1, 8):
        if lFC:
            if up_inverse(color,board[i][xCord]):
                # print(f"{color} long boi ttacking dis {strC(yCord, i)} -- {board[yCord][i]}")

                availableMoves.append(strC(i, xCord))
                # print(availableMoves)
                break
        if up_inverse(color,board[i][xCord]):
            break
        elif low_inverse(color, board[i][xCord]):
            availableMoves.append(strC(i, xCord))
            break
        elif not board[i][xCord]:
            availableMoves.append(strC(i, xCord))

    # right moves
    for i in range(xCord+1, 8):
        if lFC:
            if up_inverse(color,board[yCord][i]):
                availableMoves.append(strC(yCord, i))
                break            
        if up_inverse(color,board[yCord][i]):
            break
        elif low_inverse(color, board[yCord][i]):
            availableMoves.append(strC(yCord, i))
            break
        elif not board[yCord][i]:
            availableMoves.append(strC(yCord, i))

    # left moves
    for i in range(xCord-1, -1, -1):
        if lFC:
            if up_inverse(color,board[yCord][i]):
                availableMoves.append(strC(yCord, i))

                # print(f"{color} long boi ttacking dis {strC(yCord, i)} -- {board[yCord][i]}")
                break

        if up_inverse(color,board[yCord][i]):
            break
        elif low_inverse(color, board[yCord][i]):
            availableMoves.append(strC(yCord, i))
            break
        elif not board[yCord][i]:
            availableMoves.append(strC(yCord, i))    
    
    return availableMoves

def kingLegalMoves(xCord,yCord,board,color,lFC):
    # color True is light || False is dark
    availableMoves = []
    allKingMoves = [(yCord+1, xCord),(yCord-1, xCord),(yCord, xCord+1),(yCord, xCord-1),
                    (yCord+1, xCord+1),(yCord-1, xCord+1),(yCord+1, xCord-1),(yCord-1, xCord-1),]
    
    for kingMove in allKingMoves:
        j,i = kingMove
        if 0 <= i < 8 and 0 <= j <8:
            if lFC:
                if up_inverse(color, board[j][i]):
                    availableMoves.append(strC(j, i))

            if up_inverse(color, board[j][i]):
                continue
            availableMoves.append(strC(j, i))
    return availableMoves

def pawnColorMoves(color):
    results = []
    if color:
        results.append(-1)
        results.append(6)
    else:
        results.append(1)
        results.append(1)
    return results


def moveController(square,board,turn):
    isChecked,kingEscapeMoves,kingCords = isKingOnCheck(board, turn)
    # print(kingEscapeMoves)
    pinned = kingSight(turn, board,kingCords,square)
    if kingEscapeMoves == []:
        kingEscapeMoves = 0
    
    if pinned == []:
        pinned = 0
    return getLegalMoves(square, board,kingEscapeMoves,False,pinned)

def getLegalMoves(square, board,kingEscape,lookingForChecks,notPinnedMoves):
    cords = int(square)
    xCord = int(square[1])
    yCord = int(square[0])

    piece = board[yCord][xCord]
    availableMoves = []

    # Pawn Moves
    if piece == 'P' or piece == 'p':
        availableMoves = pawnLegalMoves(xCord, yCord, board, piece.isupper(),lookingForChecks)
        if notPinnedMoves:
            availableMoves = notPinnedMoves
        
        if notPinnedMoves == 0:
            availableMoves = []
    # Rook Moves
    if piece == 'R' or piece == 'r':
        availableMoves =  straightLegalMoves(xCord, yCord, board,piece.isupper(),lookingForChecks)

    # Bishop Moves
    if piece == 'B' or piece == 'b':
        availableMoves = diagonalLegalMoves(xCord, yCord, board, piece.isupper(),lookingForChecks)

    # Knight Moves
    if piece == 'N' or piece == 'n':
        availableMoves =  knightLegalMoves(xCord, yCord, board,piece.isupper(),lookingForChecks)

    # Queen Moves
    if piece == 'Q' or piece == 'q':
        availableMoves = straightLegalMoves(xCord, yCord, board, piece.isupper(),lookingForChecks)
        availableMoves += diagonalLegalMoves(xCord, yCord, board, piece.isupper(),lookingForChecks)

    # King Moves
    if piece =='K' or piece == 'k':
        availableMoves = kingLegalMoves(xCord, yCord, board, piece.isupper(),lookingForChecks)
        if kingEscape == 0:
            availableMoves = []
        if kingEscape:
            availableMoves = kingEscape
    return availableMoves



def pieceName(color):
    if color:
        queen = 'Q'
        rook = 'R'
        bishop = 'P'
    else:
        queen = 'q'
        rook = 'r'
        bishop = 'b' 
    return queen,rook,bishop
    

def kingSight(color,board,kingCords,square):
    if color:
        king = 'K'

    else:
        king = 'k'

    xCord = int(kingCords[1])
    yCord = int(kingCords[0])

    xSquare = int(square[1])
    ySquare = int(square[0])

    queen,rook,bishop = pieceName(not color)
    
    # Check if its on the same y axisis (top)
    
    pieceBetween = False
    friendlyPieceTop = False
    newLegalMoves = []
    if xCord == xSquare:
        for i in range(yCord-1,ySquare,-1):
            if board[i][xCord]:
                pieceBetween = True
                break
        
        if not pieceBetween:
            for i in range(ySquare-1,-1,-1):
                if up_inverse(color, board[i][xCord]):
                    friendlyPieceTop = True
                    break
                if low_inverse(color, board[i][xCord]):
                    if board[i][xCord] == queen or board[i][xCord] == rook :
                        currentLegalMoves = getLegalMoves(kingCords, board,None,False,None)
                        
                        #  to remove any move that goes to other y axis
                        for move in currentLegalMoves:
                            print(xCord)
                            if move[0] == str(yCord):
                                print('hi')
                                newLegalMoves.append(move)

    return newLegalMoves   
def isKingOnCheck(board,color):
    if color:
        king = 'K'
    else:
        king = 'k'

    opponentPiecesCords = []
    kingEscapeMoves =[]
    attackerPieces = []
    isChecked = False
    for i in range(8):
        for j in range(8):
            if low_inverse(color,board[j][i]):
                opponentPiecesCords.append((board[j][i],strC(j, i)))
            if board[j][i] == king:
                kingCords = strC(j,i)
                kingEscapeMoves = getLegalMoves(kingCords, board,None,False,None)


    
    for piece in opponentPiecesCords:
        if not getLegalMoves(piece[1], board,None,True,None):
            # print(piece[1])
            continue
        for move in getLegalMoves(piece[1], board,None,True,None):
            if kingEscapeMoves:
                for kingMove in kingEscapeMoves:
                    if move == kingMove:
                        # print(f'the piece {piece[0]} at {piece[1]} is attacking the king at {move} ')
                        kingEscapeMoves.remove(kingMove)
                
            if move == kingCords:
                attackerPieces.append(piece)
                isChecked = True
                print(f"{piece[0]} at {piece[1]} is attacking {king} ")



    return isChecked, kingEscapeMoves,kingCords
    

            



# to get out of check
# Kill the attacker
# Run away from the attacker 
# if its long range get infront of him

def getOutofCheck(attackingPieces,board):
    pass