from .checkCheck import isKingOnCheck,getOutOfCheck,isPinned,isCheckmated
from .getLegalMoves import getLegalMoves
from .extraMoves import castleing

def controller(pieceCoordinates,board,turn,movedStatus):
    isCheck, kingMoves, kingCords, attackerPieces= isKingOnCheck(board, turn)
    getOutOfCheckMoves = None
    pinnedLegalMoves = isPinned(pieceCoordinates, turn, board)
    if isCheck:
        getOutOfCheckMoves = getOutOfCheck(pieceCoordinates, attackerPieces, board, kingCords)
    castleMoves = None

    if pieceCoordinates == '74':
        castleMoves = castleing(movedStatus, turn, board)
    elif pieceCoordinates == '04':
        castleMoves = castleing(movedStatus, turn, board)

    if isCheck and kingMoves == []:
        if isCheckmated(turn,attackerPieces,board,kingCords):
            return [],True

    return getLegalMoves(pieceCoordinates, board,kingMoves=kingMoves,getOutOfCheckMoves=getOutOfCheckMoves,pinnedLegalMoves=pinnedLegalMoves,castleMoves=castleMoves),False
