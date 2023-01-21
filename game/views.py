from django.shortcuts import render
from django.http import JsonResponse


def mainView(request):
    return render(request, 'mainPage.html')



def board(request):
    board = [ 
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
    ]

    if is_ajax(request):
        square = request.POST.get('sqId')
        print(square)
        if square:
            return JsonResponse({'moves':getLegalMoves(square, board)})
        return JsonResponse({'data':board})


def getLegalMoves(square,board):
    cords = int(square)
    xCord = int(square[1])
    yCord = int(square[0])

    piece = board[yCord][xCord]
    availableMoves = []

    if piece == 'P':
        # Up moves
        if not board[yCord-1][xCord]:
            availableMoves.append(strC(yCord-1,xCord))
        if yCord == 6 and not board[yCord-1][xCord] and not board[yCord-2][xCord]:
            availableMoves.append(strC(yCord-2,xCord))

        # Capture Diagonal
        if xCord > 0 and board[yCord-1][xCord-1]:
            availableMoves.append(strC(yCord-1, xCord-1))
        
        if xCord <7 and board[yCord-1][xCord+1]:
            availableMoves.append(strC(yCord-1,xCord+1))
        

        

    return availableMoves


#i send and recieve the cords in 2 diget string for example 50 
# first diget (5) is the y value, and second diget (0) is the x value
# instead of converting evertime while appending the available moves 
# i send it here for to be less messy..
# instead of str(yCord-1)+str(xCord)  strC(yCord-1,xCord)
def strC(y,x):
    return str(y)+str(x)


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'