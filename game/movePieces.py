from .handlers import promotionHandler,enPassantHandler,castleHandler

def movePieces(oldPlace, newPlace, board,movedStatus,enPassant,captureStatus):

# check for legal moves

    oldCords = int(oldPlace)
    oX = int(oldPlace[1])
    oY = int(oldPlace[0])

    piece = board[oY][oX]
    color = piece.isupper()

    newCords = int(newPlace)
    nX = int(newPlace[1])
    nY = int(newPlace[0])


    piece = promotionHandler(piece, color, nY)    
    enPassantHandler(oldPlace, newPlace, color,board,enPassant,captureStatus)
    if castleHandler(oldPlace, newPlace, movedStatus, board):
        if board[nY][nX]:
            if color:
                captureStatus[1] += board[nY][nX]
            else:
                captureStatus[0] += board[nY][nX]
        board[oY][oX] = ""
        board[nY][nX] = piece

    return board