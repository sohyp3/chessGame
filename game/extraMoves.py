from .helpers import oppositeColor,strC,pawnColorMoves
from .getLegalMoves import getLegalMoves

def castleing(movedStatus,color,board):
    opponentPieces = []
    availableMoves = []
    lightShort = False
    lightLong = False
    darkShort = False
    darkLong = False
    # Light
    if color:
        # Short Castle (king side)
        if not movedStatus[1][1] and not movedStatus[1][2] and board[7][5] == '' and board[7][6] =='' and board[7][7]=='R':
            lightShort = True
            for row in range(8):
                for col in range(8):
                    if oppositeColor(color,board[row][col]):
                        opponentPieces.append(((board[row][col]),strC(row,col)))
            
            for piece in opponentPieces:
                moves = getLegalMoves(piece[1], board)
                if '74' in moves or '75' in moves or '76' in moves:
                    lightShort = False
                    break


            # Long Caslte (queen side)
        opponentPieces = []
        if not movedStatus[1][1] and not movedStatus[1][0] and board[7][1] == '' and board[7][2] =='' and board[7][3] =='' and board[7][0]=='R':
            lightLong = True
            for row in range(8):
                for col in range(8):
                    if oppositeColor(color,board[row][col]):
                        opponentPieces.append(((board[row][col]),strC(row,col)))
            for piece in opponentPieces:
                moves = getLegalMoves(piece[1], board)
                if '74' in moves or '73' in moves or '72' in moves:
                    lightLong = False
                    break
        
        # Dark
    elif not color:
        # Short Castle (king side)
        if not movedStatus[0][1] and not movedStatus[0][2] and board[0][5] == '' and board[0][6] =='' and board[0][7]=='r':
            darkShort = True
            for row in range(8):
                for col in range(8):
                    if oppositeColor(color,board[row][col]):
                        opponentPieces.append(((board[row][col]),strC(row,col)))
            for piece in opponentPieces:
                moves = getLegalMoves(piece[1], board)
                if '04' in moves or '05' in moves or '06' in moves:
                    darkShort = False
                    break
                    
        # Long Caslte (queen side)
        opponentPieces = []
        if not movedStatus[0][1] and not movedStatus[0][0] and board[0][1] == '' and board[0][2] =='' and board[0][3] =='' and board[0][0]=='r':
            darkLong = True
            for row in range(8):
                for col in range(8):
                    if oppositeColor(color,board[row][col]):
                        opponentPieces.append(((board[row][col]),strC(row,col)))
            
            for piece in opponentPieces:
                moves = getLegalMoves(piece[1], board)
                if '04' in moves or '03' in moves or '02' in moves:
                    darkLong = False
                    break
    
    if lightShort == True:
        availableMoves.append('77')
    if lightLong == True:
        availableMoves.append('70')
    if darkShort == True:
        availableMoves.append('07')
    if darkLong == True:
        availableMoves.append('00')
    
    if availableMoves == []:
        availableMoves = None
    return availableMoves

def enPassantHandler(piece,enPassant,color,board):
    x = int(piece[1])
    y = int(piece[0])

    dest = pawnColorMoves(color)[0]
    if enPassant[0]:
        if y == enPassant[1] :
            if x+1 == enPassant[2] or x-1 == enPassant[2]:
                if x> enPassant[2]:
                    return strC(y+dest, x-1)
                else:
                    return strC(y+dest,x+1)

    return None