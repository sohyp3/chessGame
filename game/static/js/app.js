// for (let i =0; i<8; i++){
//     for (let j = 0; j<8;j++){
//         const squareEl = document.createElement("div");
//         squareEl.classList.add("square");    
        
//         // light or dark

//         if ((i + j) % 2 === 0) {
//             squareEl.classList.add("white");
//         } else {
//             squareEl.classList.add("black");
//         }    
    
//     }
// }


async function createBoard (){
    board = await getFen()
    console.log(board)
    for (let i =0; i<8; i++){
        for (let j = 0; j<8;j++){
            let sqColor
            if ((i+j)%2 == '0'){
                sqColor = 'dark'
            } 
            else{
                sqColor = 'light'
            }
            // console.log(i, j)
            piece = board[i][j]
            
            drawSquares(sqColor,piece)
        }
    }

}

createBoard()



function drawSquares (sqColor,piece){

    let board = document.getElementById('board')
    let square = document.createElement('div')
    square.classList.add('square', sqColor)

    board.appendChild(square)

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
}


async function getFen(){
    let board;

    await $.get ('/fen', function(data){
        board = data.data
    })
    return board
}
