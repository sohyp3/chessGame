from .helpers import piecesName

def isUnderAttack(y, x, board, color):
    # Check if the square is under attack by pawns
    if color:
        if y < 7 and x > 0: 
            if board[y+1][x-1] == 'p':
                return True
        if y < 7 and x < 7:
            if board[y+1][x+1] == 'p':
                return True
    else:
        if y > 0 and x > 0:
            if board[y-1][x-1] == 'P':
                return True
        if y > 0 and x < 7:
            if board[y-1][x+1] == 'P':
                return True
    
    # Check if the square is under attack by diagonal
    for i, j in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        row = y + i
        col = x + j
        while 0 <= row < 8 and 0 <= col < 8:
            piece = board[row][col]
            if piece == 'B' or piece == 'Q':
                return True
            if piece:
                break
            row += i
            col += j
    
    # Check if the square is under attack by straight
    for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        row = y + i
        col = x + j
        while 0 <= row < 8 and 0 <= col < 8:
            piece = board[row][col]
            if piece == 'R' or piece == 'Q':
                return True
            if piece:
                break
            row += i
            col += j
    
    # Check if the square is under attack by knights
    for i, j in [(2, 1), (2, -1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (1, -2), (-1, -2)]:
        row = y + i
        col = x + j
        if 0 <= row < 8 and 0 <= col < 8:
            if board[row][col] == 'N':
                return True
    
    # Check if the square is under attack by the king
    for i, j in [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]:
        row = y + i
        col = x + j
        if 0 <= row < 8 and 0 <= col < 8:
            if board[row][col] == 'K':
                return True
    
    return False
