from .helpers import oppositeColor,strC
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
            for row in range(8):
                for col in range(8):
                    if oppositeColor(color,board[row][col]):
                        opponentPieces.append(((board[row][col]),strC(row,col)))
            
            for piece in opponentPieces:
                moves = getLegalMoves(piece[1], board)
                for move in moves:
                    if move == board[7][4] or move == board[7][5] or move == board[7][6]:
                        break
                    else:
                        lightShort = True
                        break
            # Long Caslte (queen side)
        if not movedStatus[1][1] and not movedStatus[1][0] and board[7][1] == '' and board[7][2] =='' and board[7][3] =='' and board[7][0]=='R':
            for row in range(8):
                for col in range(8):
                    if oppositeColor(color,board[row][col]):
                        opponentPieces.append(((board[row][col]),strC(row,col)))
            
            for piece in opponentPieces:
                moves = getLegalMoves(piece[1], board)
                for move in moves:
                    if move == board[7][4] or move == board[7][3] or move == board[7][2]:
                        break
                    else:
                        lightLong = True
                        break
        # Dark
    elif not color:
        # Short Castle (king side)
        if not movedStatus[0][1] and not movedStatus[0][2] and board[0][5] == '' and board[0][6] =='' and board[0][7]=='r':
            for row in range(8):
                for col in range(8):
                    if oppositeColor(color,board[row][col]):
                        opponentPieces.append(((board[row][col]),strC(row,col)))
            for piece in opponentPieces:
                moves = getLegalMoves(piece[1], board)
                for move in moves:
                    if move == board[0][4] or move == board[0][5] or move == board[0][6]:
                        break
                    else:
                        darkShort = True
                        break
            # Long Caslte (queen side)
        if not movedStatus[0][1] and not movedStatus[0][0] and board[0][1] == '' and board[0][2] =='' and board[0][3] =='' and board[0][0]=='r':
            for row in range(8):
                for col in range(8):
                    if oppositeColor(color,board[row][col]):
                        opponentPieces.append(((board[row][col]),strC(row,col)))
            
            for piece in opponentPieces:
                moves = getLegalMoves(piece[1], board)
                for move in moves:
                    if move == board[0][4] or move == board[0][3] or move == board[0][2]:
                        break
                    else:
                        darkLong = True
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