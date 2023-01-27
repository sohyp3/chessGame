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
    if color:
        king = 'k'
    else:
        king='K'

    # color True is light || False is dark
    availableMoves = []

    # top-left
    i = xCord-1
    j = yCord-1
    while i >= 0 and j >= 0:
        if lFC:
            if low_inverse(color, board[j][i]):
                if board[j][i] == king:

                    m = i-1
                    n = j-1
                    while m >= 0 and n >=0:
                        availableMoves.append(strC(n, m))
                        n -=1
                        m -=1
                

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
            if low_inverse(color, board[j][i]):
                if board[j][i] == king:

                    m = i+1
                    n = j-1
                    while m < 8 and n >=0 :
                        availableMoves.append(strC(n, m))
                        m +=1
                        n -=1
                    
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
            if low_inverse(color, board[j][i]):
                if board[j][i] == king:
                    m = i-1
                    n = j-1
                    while m < 8 and n <8:
                        availableMoves.append(strC(n, m))
                        n +=1
                        m +=1
                    
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
            if low_inverse(color, board[j][i]):
                if board[j][i] == king:
                    m = i-1
                    n = j+1
                    while m >= 0 and n <8:
                        availableMoves.append(strC(n, m))
                        n +=1
                        m -=1
                    
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
    
    if color:
        king = 'k'
    else:
        king='K'
    # color True is light || False is dark
    availableMoves = []
    # upper move
    for i in range(yCord-1, -1, -1):
        if lFC:
            if low_inverse(color, board[i][xCord]): 
                if board[i][xCord] == king:
                    for j in range(i,-1,-1):
                        availableMoves.append(strC(j, xCord))
                    
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
            if low_inverse(color,board[i][xCord]):
                if board[i][xCord] == king:

                    for j in range(i,8):
                        availableMoves.append(strC(j, xCord))
                
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
            continueformore = False
            if low_inverse(color,board[yCord][i]):
                if board[yCord][i] == king:

                    for j in range(i,8):
                        availableMoves.append(strC(yCord, j))

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
            if low_inverse(color,board[yCord][i]):
                if board[yCord][i] == king:
                    
                    for j in range(i,-1,-1):

                        availableMoves.append(strC(yCord, j))

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
    isChecked,kingEscapeMoves,kingCords,attackers = isKingOnCheck(board, turn)
    pinLegalMove, pin = kingSight(turn, board,kingCords,square)

    checkEscape= []
    if isChecked:
        checkEscape = getOutofCheck(square, attackers, board,kingCords)
        if checkEscape == []:
            checkEscape = 0
    if kingEscapeMoves == []:
        kingEscapeMoves = 0
    
    if pinLegalMove == [] and pin:
        pinLegalMove = 0
    return getLegalMoves(square, board,kingEscapeMoves,False,pinLegalMove,checkEscape)

def getLegalMoves(square, board,kingEscape,lookingForChecks,notPinnedMoves,checkEscapeMoves):
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
        
        if checkEscapeMoves:
            availableMoves = checkEscapeMoves
        if checkEscapeMoves == 0:
            availableMoves = []

    # Rook Moves
    if piece == 'R' or piece == 'r':
        availableMoves =  straightLegalMoves(xCord, yCord, board,piece.isupper(),lookingForChecks)
        
        if notPinnedMoves:
            availableMoves = notPinnedMoves
        
        if notPinnedMoves == 0:
            availableMoves = []
        
        if checkEscapeMoves:    
            availableMoves = checkEscapeMoves
        if checkEscapeMoves == 0:
            availableMoves = []

    # Bishop Moves
    if piece == 'B' or piece == 'b':
        availableMoves = diagonalLegalMoves(xCord, yCord, board, piece.isupper(),lookingForChecks)
        if notPinnedMoves:
            availableMoves = notPinnedMoves
        
        if notPinnedMoves == 0:
            availableMoves = []     

        if checkEscapeMoves:
            availableMoves = checkEscapeMoves   

        if checkEscapeMoves == 0:
            availableMoves = []

    # Knight Moves
    if piece == 'N' or piece == 'n':
        availableMoves =  knightLegalMoves(xCord, yCord, board,piece.isupper(),lookingForChecks)
        if notPinnedMoves:
            availableMoves = notPinnedMoves
        
        if notPinnedMoves == 0:
            availableMoves = []

        if checkEscapeMoves:
            availableMoves = checkEscapeMoves

        if checkEscapeMoves == 0:
            availableMoves = []
    # Queen Moves
    if piece == 'Q' or piece == 'q':
        availableMoves = straightLegalMoves(xCord, yCord, board, piece.isupper(),lookingForChecks)
        availableMoves += diagonalLegalMoves(xCord, yCord, board, piece.isupper(),lookingForChecks)
        
        if notPinnedMoves:
            availableMoves = notPinnedMoves
        
        if notPinnedMoves == 0:
            availableMoves = []
            
        if checkEscapeMoves:
            availableMoves = checkEscapeMoves    
        if checkEscapeMoves == 0:
            availableMoves = []        

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
    
    # Check if its on the same y axisis 

    pieceBetween = False
    friendlyPieceTop = False
    isPinned = False
    newLegalMoves = []
    # (top)   
    if xCord == xSquare and yCord > ySquare:     
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
                        isPinned = True

                        currentLegalMoves = getLegalMoves(square, board,None,False,None,None)
                        #  to remove any move that goes to other y axis
                        for move in currentLegalMoves:
                            if move[1] == str(xCord):
                                newLegalMoves.append(move)
                    else:
                        break


    # Bottom
    if xCord == xSquare and yCord < ySquare:
        for i in range(yCord+1,ySquare):
            if board[i][xCord]:
                pieceBetween = True
                break
        if not pieceBetween:
            for i in range(ySquare+1,8):
                if up_inverse(color, board[i][xCord]):
                    friendlyPieceTop = True
                    break

                if low_inverse(color, board[i][xCord]):
                    if board[i][xCord] == queen or board[i][xCord] == rook :
                        isPinned = True

                        currentLegalMoves = getLegalMoves(square, board,None,False,None,None)
                        #  to remove any move that goes to other y axis
                        for move in currentLegalMoves:
                            if move[1] == str(xCord):
                                newLegalMoves.append(move)
                    else:
                        break
                    
    # Right
    if yCord == ySquare and xCord < xSquare:
        for i in range(xCord+1,xSquare):
            if board[yCord][i]:
                pieceBetween = True
                break
        if not pieceBetween:
            for i in range(xSquare+1,8):
                if up_inverse(color, board[yCord][i]):
                    friendlyPieceTop = True
                    break

                if low_inverse(color, board[yCord][i]):
                    if board[yCord][i] == queen or board[yCord][i] == rook :
                        isPinned = True

                        currentLegalMoves = getLegalMoves(square, board,None,False,None,None)
                        #  to remove any move that goes to other x axis
                        for move in currentLegalMoves:
                            if move[0] == str(yCord):
                                newLegalMoves.append(move)
                    else:
                        break

    # left
    if yCord == ySquare and xCord > xSquare:
        for i in range(xCord-1,xSquare,-1):
            if board[yCord][i]:
                pieceBetween = True
                break
        if not pieceBetween:
            for i in range(xSquare-1,-1,-1):
                if up_inverse(color, board[yCord][i]):
                    friendlyPieceTop = True
                    break

                if low_inverse(color, board[yCord][i]):
                    if board[yCord][i] == queen or board[yCord][i] == rook :
                        isPinned = True

                        currentLegalMoves = getLegalMoves(square, board,None,False,None,None)
                        #  to remove any move that goes to other x axis
                        for move in currentLegalMoves:
                            if move[0] == str(yCord):
                                newLegalMoves.append(move)
                    else:
                        break
    
    # diagonal 
    i = xCord -1
    j = yCord -1

    # pieceBetween = True
    # friendlyPieceTop = False
    # isPinned = False
    # newLegalMoves = []


    if abs(yCord - ySquare) == abs(xCord - xSquare):
        if yCord > ySquare and xCord < xSquare:
            i = xCord +1
            j = yCord -1

            n = xSquare +1
            m = ySquare -1

            while i < n-1 and j >= 0:
                if board[j][i]:
                    pieceBetween = True
                    break

                i +=1
                j -=1

            if not pieceBetween:
                while n < 8 and m > 0:
                    if up_inverse(color, board[m][n]):
                        friendlyPieceTop = True
                        break
                    if low_inverse(color, board[m][n]):
                        if board[m][n] == queen or board[m][n] == bishop:
                            isPinned = True
                            currentLegalMoves = getLegalMoves(square, board,None,False,None,None)

                            for move in currentLegalMoves:
                                if abs(int(move[0])-yCord) == abs(int(move[1])-xCord) and yCord > int(move[0]) and xCord < int(move[1]):
                                    newLegalMoves.append(move)               
                    n +=1
                    m -=1

        elif yCord > ySquare and xCord> xSquare:
            i = xCord -1
            j = yCord -1

            n = xSquare -1
            m = ySquare -1

            while i > n+1 and j > m:
                if board[j][i]:
                    pieceBetween = True
                    break

                i -=1
                j -=1

            if not pieceBetween:
                while n >=0  and m >= 0:
                    if up_inverse(color, board[m][n]):
                        friendlyPieceTop = True
                        break
                    if low_inverse(color, board[m][n]):
                        if board[m][n] == queen or board[m][n] == bishop:
                            isPinned = True
                            currentLegalMoves = getLegalMoves(square, board,None,False,None,None)

                            for move in currentLegalMoves:
                                if abs(int(move[0])-yCord) == abs(int(move[1])-xCord) and yCord > int(move[0]) and xCord > int(move[1]):
                                    newLegalMoves.append(move)               
                    n -=1
                    m -=1

        elif yCord < ySquare and xCord < xSquare:
            i = xCord +1
            j = yCord +1

            n = xSquare +1
            m = ySquare +1
            while i < n-1 and j < m-1:
                if board[j][i]:
                    pieceBetween = True
                    break

                i +=1
                j +=1

            if not pieceBetween:
                while n < 8 and m < 8:
                    if up_inverse(color, board[m][n]):
                        friendlyPieceTop = True
                        break
                    if low_inverse(color, board[m][n]):
                        if board[m][n] == queen or board[m][n] == bishop:
                            isPinned = True
                            currentLegalMoves = getLegalMoves(square, board,None,False,None,None)

                            for move in currentLegalMoves:
                                if abs(int(move[0])-yCord) == abs(int(move[1])-xCord) and yCord < int(move[0]) and xCord < int(move[1]):
                                    newLegalMoves.append(move)               
                    n +=1
                    m +=1        
        elif yCord < ySquare and xCord > xSquare:
            i = xCord -1
            j = yCord +1

            n = xSquare -1
            m = ySquare +1
            while i > n+1 and j < m-1:
                if board[j][i]:
                    pieceBetween = True
                    break

                i -=1
                j +=1

            if not pieceBetween:
                while n >= 0 and m < 8:
                    if up_inverse(color, board[m][n]):
                        friendlyPieceTop = True
                        break
                    if low_inverse(color, board[m][n]):
                        if board[m][n] == queen or board[m][n] == bishop:
                            isPinned = True
                            currentLegalMoves = getLegalMoves(square, board,None,False,None,None)

                            for move in currentLegalMoves:
                                if abs(int(move[0])-yCord) == abs(int(move[1])-xCord) and yCord < int(move[0]) and xCord > int(move[1]):
                                    newLegalMoves.append(move)               
                    n -=1
                    m +=1    


        
    return newLegalMoves, isPinned
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
                kingEscapeMoves = getLegalMoves(kingCords, board,None,False,None,None)


    
    for piece in opponentPiecesCords:
        if not getLegalMoves(piece[1], board,None,True,None,None):
            # print(piece[1])
            continue
        for move in getLegalMoves(piece[1], board,None,True,None,None):
            if kingEscapeMoves:
                for kingMove in kingEscapeMoves:
                    
                    if move == kingMove:
                        # print(f'the piece {piece[0]} at {piece[1]} is attacking the king at {move} ')
                        kingEscapeMoves.remove(kingMove)
                
            if move == kingCords:
                attackerPieces.append(piece)
                isChecked = True
                print(f"{piece[0]} at {piece[1]} is attacking {king} ")



    return isChecked, kingEscapeMoves,kingCords,attackerPieces
    

            



# to get out of check
# Kill the attacker
# Run away from the attacker 
# if its long range get infront of him

def getOutofCheck(piece,attackingPieces,board,kingCords):
    xCord = int(piece[1])
    yCord = int(piece[0])
    availabeMoves = []
    for attacker in attackingPieces:
        if board[yCord][xCord].lower() == 'k':
            continue
        else:
            print(attackingPieces)
            for move in getLegalMoves(piece, board, None, False, None,None):
                
                if move == attacker[1]:
                    availabeMoves.append(move)
                # Check on the Right
                if int(attacker[1][0]) == int(kingCords[0]) and int(attacker[1][1]) > int(kingCords[1]):
                    if int(move[0]) == int(kingCords[0]) and int(attacker[1][1]) > int(move[1]) > int(kingCords[1]):
                        availabeMoves.append(move)

                #  Check on the left
                if int(attacker[1][0]) == int(kingCords[0]) and int(attacker[1][1]) < int(kingCords[1]):
                    if int(move[0]) == int(kingCords[0]) and int(attacker[1][1]) < int(move[1]) < int(kingCords[1]):
                        availabeMoves.append(move)

                
                #  Check on the top
                if int(attacker[1][1]) == int(kingCords[1]) and int(attacker[1][0]) < int(kingCords[0]):
                    if int(move[1]) == int(kingCords[1]) and int(attacker[1][0]) < int(move[0]) < int(kingCords[0]):
                        availabeMoves.append(move)


                #  Check on the bottom
                if int(attacker[1][1]) == int(kingCords[1]) and int(attacker[1][0]) > int(kingCords[0]):
                    if int(move[1]) == int(kingCords[1]) and int(attacker[1][0]) > int(move[0]) > int(kingCords[0]):
                        availabeMoves.append(move)

                                
    return availabeMoves 