from .extraFunctions import strC, up_inverse,low_inverse

def pawnLegalMoves(xCord,yCord,board,color):
    # color True is light || False is dark

    # dest is the direction
    dest = pawnColorMoves(color)[0]
    base = pawnColorMoves(color)[1]
        
    availableMoves = []
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

def knightLegalMoves (xCord,yCord,board,color):
    # color True is light || False is dark

    availableMoves = []
    allNightMoves = [(yCord +1, xCord +2), (yCord -1, xCord +2), (yCord +1, xCord -2), (yCord -1, xCord -2),
                (yCord +2, xCord +1), (yCord +2, xCord -1), (yCord -2, xCord +1),(yCord -2, xCord -1)]

    for nightMove in allNightMoves:
        j,i = nightMove
        if 0 <= i < 8 and 0 <= j <8:
            if up_inverse(color, board[j][i]):
                continue
            availableMoves.append(strC(j, i))
    return availableMoves

def diagonalLegalMoves(xCord,yCord,board,color):
    # color True is light || False is dark
    availableMoves = []

    # top-left
    i = xCord-1
    j = yCord-1
    while i >= 0 and j >= 0:
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

def straightLegalMoves(xCord,yCord,board,color):
    # color True is light || False is dark

    availableMoves = []
    # upper move
    for i in range(yCord-1, -1, -1):
        if up_inverse(color, board[i][xCord]): 
            break
        if low_inverse(color, board[i][xCord]):
            availableMoves.append(strC(i, xCord))
            break
        elif not board[i][xCord]:
            availableMoves.append(strC(i, xCord))
    # lower moves
    for i in range(yCord+1, 8):
        if up_inverse(color,board[i][xCord]):
            break
        elif low_inverse(color, board[i][xCord]):
            availableMoves.append(strC(i, xCord))
            break
        elif not board[i][xCord]:
            availableMoves.append(strC(i, xCord))

    # right moves
    for i in range(xCord+1, 8):
        if up_inverse(color,board[yCord][i]):
            break
        elif low_inverse(color, board[yCord][i]):
            availableMoves.append(strC(yCord, i))
            break
        elif not board[yCord][i]:
            availableMoves.append(strC(yCord, i))

    # left moves
    for i in range(xCord-1, -1, -1):
        if up_inverse(color,board[yCord][i]):
            break
        elif low_inverse(color, board[yCord][i]):
            availableMoves.append(strC(yCord, i))
            break
        elif not board[yCord][i]:
            availableMoves.append(strC(yCord, i))    
    
    return availableMoves

def kingLegalMoves(xCord,yCord,board,color):
    # color True is light || False is dark
    availableMoves = []
    allKingMoves = [(yCord+1, xCord),(yCord-1, xCord),(yCord, xCord+1),(yCord, xCord-1),
                    (yCord+1, xCord+1),(yCord-1, xCord+1),(yCord+1, xCord-1),(yCord-1, xCord-1),]
    
    for kingMove in allKingMoves:
        j,i = kingMove
        if 0 <= i < 8 and 0 <= j <8:
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