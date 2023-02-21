from .helpers import sameColor,strC

def evaluate(board,color):
    pieceVale = {
        'p':10,
        'n':30,
        'b':30,
        'r':50,
        'q':90,
        'k':900
    }

    if color:
        return whiteScore - blackScore
    else:
        return blackScore- whiteScore


def MiniMax(board,depth,color):
    if depth == 0:
        return None, evaluate(board, color)


def allMoves(board,color,**kwargs):
    req = None
    if 'req' in kwargs:
        req = kwargs['req']
    

    pieces = []
    moves = []
    for row in range(8):
        for col in range(8):
            if sameColor(color,board[row][col]):
                pieces.append((board[row][col],strC(row,col)))
    
    if req == 'all':
        for piece in pieces:
            pieceMoves = getLegalMoves(piece[1], board)
            moves.append((piece[1],piece[0],pieceMoves))

        
    return pieces, moves
