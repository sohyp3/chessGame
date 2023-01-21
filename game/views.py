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
        if square:
            return JsonResponse({'moves': getLegalMoves(square, board)})
        return JsonResponse({'data': board})


def getLegalMoves(square, board):
    cords = int(square)
    xCord = int(square[1])
    yCord = int(square[0])

    piece = board[yCord][xCord]
    availableMoves = []

    # Light Pawn Moves
    if piece == 'P':
        # up moves
        if not board[yCord-1][xCord]:
            availableMoves.append(strC(yCord-1, xCord))

        # first move
        if yCord == 6 and not board[yCord-1][xCord] and not board[yCord-2][xCord]:
            availableMoves.append(strC(yCord-2, xCord))

        # capture diagonal
        if xCord > 0 and board[yCord-1][xCord-1] and board[yCord-1][xCord-1].islower():
            availableMoves.append(strC(yCord-1, xCord-1))

        if xCord < 7 and board[yCord-1][xCord+1] and board[yCord-1][xCord+1].islower():
            availableMoves.append(strC(yCord-1, xCord+1))

    # Light Rook Move
    if piece == 'R':
        # upper move
        for i in range(yCord-1, -1, -1):
            if board[i][xCord].isupper():
                break
            elif board[i][xCord].islower():
                availableMoves.append(strC(i, xCord))
                break
            elif not board[i][xCord]:
                availableMoves.append(strC(i, xCord))
        # lower moves
        for i in range(yCord+1, 8):
            if board[i][xCord].isupper():
                break
            elif board[i][xCord].islower():
                availableMoves.append(strC(i, xCord))
                break
            elif not board[i][xCord]:
                availableMoves.append(strC(i, xCord))

        # right moves
        for i in range(xCord+1, 8):
            if board[yCord][i].isupper():
                break
            elif board[yCord][i].islower():
                availableMoves.append(strC(yCord, i))
                break
            elif not board[yCord][i]:
                availableMoves.append(strC(yCord, i))

        # left moves
        for i in range(xCord-1, -1, -1):
            if board[yCord][i].isupper():
                break
            elif board[yCord][i].islower():
                availableMoves.append(strC(yCord, i))
                break
            elif not board[yCord][i]:
                availableMoves.append(strC(yCord, i))

    # Light Bishop Moves
    if piece == 'B':
        # top-left
        i = xCord-1
        j = yCord-1
        while i >= 0 and j >= 0:
            if board[j][i].isupper():
                break
            elif board[j][i].islower():
                availableMoves.append(strC(j, i))
            elif not board[j][i]:
                availableMoves.append(strC(j, i))

            i -= 1
            j -= 1

        # top-right
        i = xCord+1
        j = yCord-1

        while i < 8 and j >= 0:
            if board[j][i].isupper():
                break
            elif board[j][i].islower():
                availableMoves.append(strC(j, i))
                break
            elif not board[j][i]:
                availableMoves.append(strC(j, i))
            i += 1
            j -= 1

        # bottom right
        i = xCord + 1
        j = yCord + 1

        while i < 8 and j < 8:
            if board[j][i].isupper():
                break
            elif board[j][i].islower():
                availableMoves.append(strC(j, i))
                break
            elif not board[j][i]:
                availableMoves.append(strC(j, i))
            i += 1
            j += 1

        # bottom left
        i = xCord - 1
        j = yCord + 1

        while i >= 0 and j < 8:
            if board[j][i].isupper():
                break
            elif board[j][i].islower():
                availableMoves.append(strC(j, i))
                break
            elif not board[j][i]:
                availableMoves.append(strC(j, i))
            i -= 1
            j += 1

    # Light kNite Moves
    if piece == 'N':
        allNightMoves = [(yCord +1, xCord +2), (yCord -1, xCord +2), (yCord +1, xCord -2), (yCord -1, xCord -2),
                        (yCord +2, xCord +1), (yCord +2, xCord -1), (yCord -2, xCord +1),(yCord -2, xCord -1)]

        for nightMove in allNightMoves:
            j,i = nightMove
            if 0 <= i < 8 and 0 <= j <8:
                if board[j][i].isupper():
                    continue
                availableMoves.append(strC(j, i))



    return availableMoves


# i send and recieve the cords in 2 diget string for example 50
# first diget (5) is the y value, and second diget (0) is the x value
# instead of converting evertime while appending the available moves
# i send it here for to be less messy..
# instead of str(yCord-1)+str(xCord)  strC(yCord-1,xCord)
def strC(y, x):
    return str(y)+str(x)


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
