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
            cords = i+""+j
            
            drawSquares(sqColor,piece,cords)
        }
    }

}

createBoard()



function drawSquares (sqColor,piece,cords){

    let board = document.getElementById('board')
    let square = document.createElement('div')
    square.classList.add('square', sqColor)
    square.id = cords
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

    square.addEventListener('click',function(){
        let selected = document.querySelectorAll('.selected')
        selected.forEach(function(sq){
            sq.classList.remove('selected')
        })
        console.log(this.id)
        this.classList.add('selected')
    })
}


async function getFen(){
    let board;

    await $.get ('/fen', function(data){
        board = data.data
    })
    return board
}



function getMoves(){
    const formdata = new FormData()
    const csrf = document.getElementsByName('csrfmiddlewaretoken')
    formdata.append('csrfmiddlewaretoken', csrf[0].value)

    $.ajax({
        type: "POST",
        url: "",
        enctype: 'multipart/form-data',
        data: formdata,
        success: function (res) {
            if (res.data =='verified'){
                modal.classList.add('is-active')


                setTimeout(function() {
                    window.location.href = redirectURL.value
                }, 1500);
            }
            else if (res.data =='wrong'){
                wrongNot.classList.remove('is-hidden')
                
            }

            
        },

        cache: false,
        contentType: false,
        processData: false,

    });
}