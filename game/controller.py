from .movements import pawnLegalMoves
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

    return moves