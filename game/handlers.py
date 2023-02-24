from .helpers import pawnColorMoves

def promotionHandler(piece,color,nY):
    dest = pawnColorMoves(color)[0]
    base = pawnColorMoves(color)[1]

    if piece.lower() == 'p' and nY == 6 + (base * dest):
        if color:
            piece = 'Q'
        else:
            piece = 'q'
    return piece

def enPassantHandler(oldPlace,newPlace,color,board,enPassant,captureStatus):
    dest = pawnColorMoves(color)[0]
    base = pawnColorMoves(color)[1]
    
    oX = int(oldPlace[1])
    oY = int(oldPlace[0])

    nX = int(newPlace[1])
    nY = int(newPlace[0])

    piece = board[oY][oX]
    color = piece.isupper()
    
    if piece.lower() == 'p' and oY == base and nY == base + (dest * 2):
        enPassant[0] = True
        enPassant[1] = nY
        enPassant[2] = nX
    else:
        enPassant[0] = False
        enPassant[1] = ''
        enPassant[2] = ''

    if piece.lower() == 'p' and oX != nX and board[nY][nX] == '':
    
        if color:
            captureStatus[1] += 'p'
        else:
            captureStatus[0] += 'P'
        board[nY-(dest)][nX] = ''

def castleHandler(oldPlace,newPlace,movedStatus,board):
    oldCords = int(oldPlace)

    oX = int(oldPlace[1])
    oY = int(oldPlace[0])

    piece = board[oY][oX]
    color = piece.isupper()

    newCords = int(newPlace)
    nX = int(newPlace[1])
    nY = int(newPlace[0])
    # Castling
    # Light Short Castle
    if piece == 'K' and oldCords == 74 and newCords == 77:
        print('ere')
        board[7][4] = ""
        board[7][7] = ""
        board[7][5] = "R"
        board[7][6] = 'K'
    # Light Long Castle
    elif piece == 'K' and oldCords == 74 and newCords == 70:
        board[7][4] = ""
        board[7][0] = ""
        board[7][3] = "R"
        board[7][2] = 'K'      
    # Dark short Castle
    elif piece == 'k' and oldCords == 4 and newCords == 7:
        board[0][4] = ""
        board[0][7] = ""
        board[0][5] = "r"
        board[0][6] = 'k'
    # Dark Long Castle
    elif piece == 'k' and oldCords == 4 and newCords == 0:
        board[0][4] = ""
        board[0][0] = ""
        board[0][3] = "r"
        board[0][2] = 'k'      
    else:
        return True

    # Check if kings or rooks moved
    if oY == 0 and oX ==0:
        movedStatus[0][0] = True
    elif oY == 0 and oX == 4:
        movedStatus[0][1] = True
    elif oY == 0 and oX == 7:
        movedStatus[0][2] = True

    if oY == 7 and oX == 0:
        movedStatus[1][0] = True
    elif oY == 7 and oX == 4:
        movedStatus[1][1] = True
    elif oY == 7 and oX == 7:
        movedStatus[1][2] = True
