async function createBoard() {
    responseInfo = await getBoard()
    let board = responseInfo.board

    window.turn = responseInfo.turn
    
    console.log(window.turn)

    window.boardVar = board

    for (let i = 0; i < 8; i++) {
        for (let j = 0; j < 8; j++) {
            let sqColor
            let uiNum
            let uiLet
            if ((i + j) % 2 == 0) {
                sqColor = 'light'
            }
            else {
                sqColor = 'dark'
            }
            piece = board[i][j]
            cords = i + "" + j
            if (j == 0) {
                uiNum = 8 - i
            }
            if (i == 7) {
                uiLet = String.fromCharCode(97 + j)
            }
            drawSquares(sqColor, piece, cords, uiNum, uiLet)
        }
    }

}

createBoard()


// sends get request to get the board position
async function getBoard() {
    let board;

    await $.get('/board', function (data) {
        reData = data
    })
    return reData
}


// get the legal moves.
function getMoves(sqId) {
    const formdata = new FormData()
    const csrf = document.getElementsByName('csrfmiddlewaretoken')
    formdata.append('csrfmiddlewaretoken', csrf[0].value)
    formdata.append('sqId', sqId)

    $.ajax({
        type: "POST",
        url: "/board",
        enctype: 'multipart/form-data',
        data: formdata,
        success: function (res) {
            highlightAvailableMoves(res.moves)
        },

        cache: false,
        contentType: false,
        processData: false,

    });
}


// Send the new piece places
function sendNewPlace(oldID, newID) {
    const formdata = new FormData()
    const csrf = document.getElementsByName('csrfmiddlewaretoken')
    formdata.append('csrfmiddlewaretoken', csrf[0].value)
    formdata.append('newSqId', newID)
    formdata.append('oldSqId', oldID)


    $.ajax({
        type: "POST",
        url: "/board",
        enctype: 'multipart/form-data',
        data: formdata,
        success: function (res) {
            window.turn = res.turn
            console.log(turn)
            compareBoard(res.board)
        },

        cache: false,
        contentType: false,
        processData: false,

    });
}


// 

function drawImages(piece) {
    const isUpperCase = (string) => /^[A-Z]*$/.test(string)
    let color
    if (isUpperCase(piece)) {
        color = 'w'
    }
    else {
        color = 'b'
    }

    const piecee = piece.toUpperCase()
    if (piece) {
        return `images/${color}${piecee}.png`
    }
}

function drawSquares(sqColor, piece, cords, uiNum, uiLet) {

    let board = document.getElementById('board')
    let square = document.createElement('div')

    square.classList.add('square', sqColor)
    square.id = cords
    board.appendChild(square)

    let squarePieceName = document.createElement('p')
    squarePieceName.innerText = piece
    square.appendChild(squarePieceName)

    if (drawImages(piece)) {
        let img = document.createElement('img')
        img.src = drawImages(piece)
        square.appendChild(img)
    }

    // Draw the board Cordiants 
    if (uiNum) {
        let cordNumber = document.createElement('span')
        cordNumber.classList.add('uiNum')
        cordNumber.innerText = uiNum
        square.appendChild(cordNumber)
    }

    if (uiLet) {
        let cordLetter = document.createElement('span')
        cordLetter.classList.add('uiLet')
        cordLetter.innerText = uiLet
        square.appendChild(cordLetter)
    }


    // handle the click events
    square.addEventListener('click', function () {
        let selected = document.querySelectorAll('.selected')
        let highlighted = document.querySelectorAll('.highlightAvailable')
        pieceClickHandler(this, selected, highlighted)
    })
}


function pieceClickHandler(selectedPiece, selected, highlighted) {
    turn = window.turn
    
    if (selectedPiece.classList.contains('highlightAvailable')) {
        sendNewPlace(selected[0].id, selectedPiece.id)
    }
    removeHighlights(selected, highlighted)
    if (upInverse(turn, selectedPiece.innerText)) {
        selectedPiece.classList.add('selected')
        getMoves(selectedPiece.id)

    }
}



function removeHighlights(selected, highlighted) {
    selected.forEach(function (sq) {
        sq.classList.remove('selected')
    })
    highlighted.forEach(function (sq) {
        sq.classList.remove('highlightAvailable')
    })
}


function highlightAvailableMoves(moves) {
    for (let move in moves) {
        let square = document.getElementById(moves[move])
        square.classList.add('highlightAvailable')
    }
}

function movePieces(differences, newBoard) {
    for (let i = 0; i < differences.length; i++) {
        let square = document.getElementById(differences[i]['c'])
        let squareText = square.querySelector('p')
        let SquareImage = square.querySelector('img')
        let squareNewImage = document.createElement('img')

        if (differences[i]['n'] !== "") {
            squareNewImage.src = drawImages(differences[i]['n'])
            square.appendChild(squareNewImage)

            if (SquareImage) {
                square.removeChild(SquareImage)
            }
            squareText.innerText = differences[i]['n']

        }
        else {
            square.removeChild(SquareImage)
            squareText.innerText = differences[i]['n']
        }
        window.boardVar = newBoard
    }

    turn = window.turn
    let turns = document.getElementById('turns')
    console.log(turn)
    if (turn == true) {
        turns.innerText = "White's Turn ⚪"
    }
    else {
        turns.innerHTML = "Black's Turn ⚫"
    }


}

function compareBoard(newBoard) {
    oldBoard = window.boardVar
    changesArr = []

    for (let i = 0; i < newBoard.length; i++) {
        for (let j = 0; j < newBoard[i].length; j++) {
            if (newBoard[i][j] !== oldBoard[i][j]) {
                changesArr.push({ 'o': oldBoard[i][j], 'n': newBoard[i][j], 'c': String(i) + String(j) })
            }

        }
    }
    movePieces(changesArr, newBoard)
}


function upInverse(switcher, string) {
    const isUpperCase = (string) => /^[A-Z]*$/.test(string)

    if (switcher == true) {
        return isUpperCase(string[0])
    }
    else if (switcher == false) {

        if (string) {
            return !isUpperCase(string[0])
        }
    }

}