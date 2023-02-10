# The mechanism i decide the friendly pieces vs enemy pieces is by checking if they are upper or lower
# Light Colored pieces are upper case, dark colored pieces are lower case
# Instead of rewriting the code for each color
# I can inverse the result when i call the function to check the legal move.
def sameColor(switcher,string):
    if switcher:
        return string.isupper()
    else:
        if string:
            return not string.isupper()

def oppositeColor(switcher,string):
    if  switcher:
        return  string.islower()
    else:
        if string:
            return not string.islower()

# i send and recieve the cords in 2 diget string for example 50
# first diget (5) is the y value, and second diget (0) is the x value
# instead of converting evertime while appending the available moves
# i send it here for to be less messy..
# instead of str(yCord-1)+str(xCord)  strC(yCord-1,xCord)
def strC(y, x):
    return str(y)+str(x)

# Dark Pieces move down
# Light Pieces move up
def pawnColorMoves(color):
    if color:
        direction = -1
        baseSquare = 6
    else:
        direction = 1
        baseSquare = 1
    return direction, baseSquare

def kingName(color):
    if color:
        return 'K'
    else:
        return 'k'

def piecesName(color):
    if color:
        queen = 'Q'
        rook = 'R'
        bishop = 'P'
    else:
        queen = 'q'
        rook = 'r'
        bishop = 'b' 
    return queen,rook,bishop

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'