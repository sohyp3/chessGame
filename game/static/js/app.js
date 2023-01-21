async function createBoard (){
    board = await getBoard()
    for (let i =0; i<8; i++){
        for (let j = 0; j<8;j++){
            let sqColor
            let uiNum
            let uiLet
            if ((i+j)%2 == 0){
                sqColor = 'light'
            } 
            else{
                sqColor = 'dark'
            }
            piece = board[i][j]
            cords = i+""+j
            if (j == 0){
                uiNum = 8-i 
            }
            if(i == 7){
                uiLet = String.fromCharCode(97+j)
            }
            drawSquares(sqColor,piece,cords,uiNum,uiLet)
        }
    }

}

createBoard()



function drawSquares (sqColor,piece,cords,uiNum,uiLet){

    let board = document.getElementById('board')
    let square = document.createElement('div')
    square.classList.add('square', sqColor)
    square.id = cords
    board.appendChild(square)


    // Draw the images
    let img = document.createElement('img')

    switch (piece){
        case 'r':
            img.src = "images/bR.png"
            break
        case 'n':
            img.src = "images/bN.png"
            break
        case 'b':
            img.src = "images/bB.png"
            break
        case 'k':
            img.src = "images/bK.png"
            break
        case 'q':
            img.src = "images/bQ.png"
            break
        case 'p':
            img.src = "images/bP.png"
            break;
    

        case 'R':
            img.src = "images/wR.png"
            break
        case 'N':
            img.src = "images/wN.png"
            break
        case 'B':
            img.src = "images/wB.png"
            break
        case 'K':
            img.src = "images/wK.png"
            break
        case 'Q':
            img.src = "images/wQ.png"
            break
        case 'P':
            img.src = "images/wP.png"
            break;

    }
    square.appendChild(img)
    
    // Draw the board Cordiants
    if (uiNum){
        let cordNumber = document.createElement('span')
        cordNumber.classList.add('uiNum')
        cordNumber.innerText = uiNum
        square.appendChild(cordNumber)
    }

    if (uiLet){
        let cordLetter = document.createElement('span')
        cordLetter.classList.add('uiLet')
        cordLetter.innerText = uiLet
        square.appendChild(cordLetter)
    }

    
    // handle the click events
    square.addEventListener('click',function(){
        let selected = document.querySelectorAll('.selected')
        let highlighted = document.querySelectorAll('.highlightAvailable')
        selected.forEach(function(sq){
            sq.classList.remove('selected')
        })
        highlighted.forEach(function(sq){
            sq.classList.remove('highlightAvailable')
        })
        getMoves(this.id)
        console.log(this.id)
        this.classList.add('selected')
    })
}

// sends get request to get the board position
async function getBoard(){
    let board;

    await $.get ('/board', function(data){
        board = data.data
    })
    return board
}


// get the legal moves.
function getMoves(sqId){
    const formdata = new FormData()
    const csrf = document.getElementsByName('csrfmiddlewaretoken')
    formdata.append('csrfmiddlewaretoken', csrf[0].value)
    formdata.append('sqId',sqId)

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

function highlightAvailableMoves(moves){
    for (let move in moves){
        let square = document.getElementById(moves[move])
        square.classList.add('highlightAvailable')
        console.log(moves[move])
    }
}