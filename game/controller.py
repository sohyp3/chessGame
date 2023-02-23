from .checkCheck import isKingOnCheck,getOutOfCheck,isPinned,isCheckmated,isStaleMate,isDraw
from .getLegalMoves import getLegalMoves
from .extraMoves import castleing,enPassantHandler



def controller(pieceCoordinates,board,turn,movedStatus,enPassant):
    getOutOfCheckMoves = None
    castleMoves = None
    enPassantMove = None
    isCheck, kingMoves, kingCords, attackerPieces= isKingOnCheck(board, turn)
    pinnedLegalMoves = isPinned(pieceCoordinates, turn, board)
    
    if isCheck:
        getOutOfCheckMoves = getOutOfCheck(pieceCoordinates, attackerPieces, board, kingCords)
    
    # Castling Moves
    if pieceCoordinates == '74':
        castleMoves = castleing(movedStatus, turn, board)
    elif pieceCoordinates == '04':
        castleMoves = castleing(movedStatus, turn, board)
    #  En Passant Moves
    if enPassant:
        move = enPassantHandler(pieceCoordinates,enPassant, turn,board)
        if move != None:
            enPassantMove = move

    # Draw Moves
    if isCheck and kingMoves == []:
        if isCheckmated(turn,attackerPieces,board,kingCords):
            return [],True,False
    if not isCheck and kingMoves == []:
        if isStaleMate(turn, board):
            return [],False,True
    if isDraw(board, turn):
        return [],False,True

    # ----
    return getLegalMoves(pieceCoordinates, board,kingMoves=kingMoves,getOutOfCheckMoves=getOutOfCheckMoves,pinnedLegalMoves=pinnedLegalMoves,castleMoves=castleMoves,enPassantMove = enPassantMove),False,False
