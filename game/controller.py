from .checkCheck import isKingOnCheck,getOutOfCheck,isPinned
from .getLegalMoves import getLegalMoves

def controller(pieceCoordinates,board,turn,movedStatus):
    isCheck, kingMoves, kingCords, attackerPieces= isKingOnCheck(board, turn)
    getOutOfCheckMoves = None
    pinnedLegalMoves = isPinned(pieceCoordinates, turn, board)
    if isCheck:
        getOutOfCheckMoves = getOutOfCheck(pieceCoordinates, attackerPieces, board, kingCords)
    
        
    return getLegalMoves(pieceCoordinates, board,lookingForCheck=False,kingMoves=kingMoves,getOutOfCheckMoves=getOutOfCheckMoves,pinnedLegalMoves=pinnedLegalMoves)
