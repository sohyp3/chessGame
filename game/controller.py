from .movements import pawnLegalMoves,knightLegalMoves,straightLegalMoves
def controller(pieceCoordinates,board,turn):
    return getLegalMoves(pieceCoordinates, board)

def getLegalMoves(pieceCoordinates,board):
    cords = pieceCoordinates
    x = int(pieceCoordinates[1])
    y = int(pieceCoordinates[0])
    pieceName = board[y][x]

    moves = []
    if pieceName.lower() == 'p':
        moves = pawnLegalMoves(cords, board, pieceName.isupper(), False)

    if pieceName.lower() == 'n':
        moves = knightLegalMoves(pieceCoordinates, board, pieceName.isupper(), False)
    
    if pieceName.lower() == 'r':
        moves = straightLegalMoves(pieceCoordinates, board, pieceName.isupper(), False)
    return moves