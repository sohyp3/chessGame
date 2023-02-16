from .movements import pawnLegalMoves,knightLegalMoves,straightLegalMoves,diagonalLegalMoves,kingLegalMoves


def getLegalMoves(pieceCoordinates,board,**kwargs):
    cords = pieceCoordinates
    x = int(pieceCoordinates[1])
    y = int(pieceCoordinates[0])
    pieceName = board[y][x]


    # Variables that i need to pass

    lookingForCheck = False
    kingMoves = None
    getOutOfCheckMoves = None
    pinnedLegalMoves = None
    castleMoves = None
    enPassantMove = None

    if 'lookingForCheck' in kwargs:
        lookingForCheck = kwargs['lookingForCheck']
    if 'kingMoves' in kwargs:
        kingMoves = kwargs['kingMoves']
    if 'getOutOfCheckMoves' in kwargs:
        getOutOfCheckMoves = kwargs['getOutOfCheckMoves']
    if 'pinnedLegalMoves' in kwargs:
        pinnedLegalMoves = kwargs['pinnedLegalMoves']        
    if 'castleMoves' in kwargs:
        castleMoves = kwargs['castleMoves']
    if 'enPassantMove' in kwargs:
        enPassantMove = kwargs['enPassantMove']
    

    moves = []
    if getOutOfCheckMoves != None:
        moves = getOutOfCheckMoves
    elif pinnedLegalMoves != None:
        moves = pinnedLegalMoves
    else:

        if pieceName.lower() == 'p':
            moves = pawnLegalMoves(cords, board, pieceName.isupper(), lookingForCheck)
            if enPassantMove != None:
                moves.append(enPassantMove)
        if pieceName.lower() == 'n':
            moves = knightLegalMoves(pieceCoordinates, board, pieceName.isupper(), lookingForCheck)
        
        if pieceName.lower() == 'r':
            moves = straightLegalMoves(pieceCoordinates, board, pieceName.isupper(), lookingForCheck)

        if pieceName.lower() == 'b':
            moves = diagonalLegalMoves(cords, board, pieceName.isupper(), lookingForCheck)

        if pieceName.lower() == 'q':
            moves = straightLegalMoves(cords, board, pieceName.isupper(), lookingForCheck)
            moves += diagonalLegalMoves(cords, board, pieceName.isupper(), lookingForCheck)
        
    if pieceName.lower() == 'k':
        moves = kingLegalMoves(cords, board, pieceName.isupper(), lookingForCheck)
            
        if kingMoves != None:
            moves = kingMoves  
            
        if castleMoves != None:
            moves+=(castleMoves)
    return moves