from .handlers import promotionHandler,enPassantHandler,castleHandler
from .helpers import pawnColorMoves

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

    dest = pawnColorMoves(color)[0]
    base = pawnColorMoves(color)[1]

    piece = promotionHandler(piece, base, dest, color, nY)    
    enPassantHandler(oldPlace, newPlace, board,base,dest,enPassant,captureStatus)
    if castleHandler(oldPlace, newPlace, movedStatus, board):
        if board[nY][nX]:
            if color:
                captureStatus[1] += board[nY][nX]
            else:
                captureStatus[0] += board[nY][nX]
        board[oY][oX] = ""
        board[nY][nX] = piece

    return board