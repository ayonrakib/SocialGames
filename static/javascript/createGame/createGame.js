function selectGameBlock(){
    // console.log("creategame js is loaded");

    gameForm = getContainer() + "<form id = 'createGameForm'>" + getRowHeader() + getColumnHeader() + "Game Title: " + getDivEnding() + getColumnHeader() + getInputText("gameTitle","Game Title") + getDivEnding() + getDivEnding()
             + getRowHeader() + getColumnHeader() + "Game Code: " + getDivEnding() + getColumnHeader() + getInputText("gameCode","Game Code") + getDivEnding() + getDivEnding()
             + getRowHeader() + getColumnHeader() + "Number of Players: " + getDivEnding() + getColumnHeader() + getInputText("numberOfPlayers","Number of Players") + getDivEnding() + getDivEnding()
             + getRowHeader() + getColumnHeader() + "Game Icon: " + getDivEnding() + getColumnHeader() + `<input type="file" id="gameIcon">` + getDivEnding() + getDivEnding()
             + getRowHeader() + getColumnHeader() + getDivEnding() + getColumnHeader() + getButton() + getDivEnding() + "</form>"  + getDivEnding() + getDivEnding();
    $("#gameBlock").html(gameForm);
    
    $(document).ready(function(){
        console.log($( "#createGameForm" ));
        $( "#createGameForm" ).submit(function( event ) {
            alert("The submit button has been clicked");
            event.preventDefault();
            console.log("form submit button has been clicked");
            var gameFormData = $( this ).serializeArray();
            // console.log(gameFormData);
            var gameIconName = $('#gameIcon').prop('files')[0]["name"];
            console.log(gameIconName);
            var gameTitle = gameFormData[0]['value'];
            var gameCode = gameFormData[1]['value'];
            var numberOfPlayers = gameFormData[2]['value'];
            console.log(gameTitle); 
            console.log(gameCode);
            console.log(numberOfPlayers);
            $.ajax({
                method: 'GET',
                url: 'create-game',
                data: {
                    'gameTitle': gameTitle,
                    'gameCode' : gameCode,
                    'numberOfPlayers' : numberOfPlayers,
                    'gameIcon' : gameIcon
                }
            }).done(function(response){
                console.log(response);
            })
            return false;
        })
    })
    
}

// $(document).ready(function(){
//     console.log($( "#createGameForm" ));
// })



function createGameBlock(gameName){
    console.log(gameName);
//     if (gameName == "29"){
//         console.log("came in create game block");
//             createGameBlock = getContainer() + getRowHeader() + getColumnHeader() + getPlayerNumber("first") + getDivEnding() + getColumnHeader() + getInputText("first") + getDivEnding()  + getDivEnding()
//                             + getRowHeader() + getColumnHeader() + getPlayerNumber("second") + getDivEnding() + getColumnHeader() + getInputText("second") + getDivEnding() + getDivEnding() 
//                             + getRowHeader() + getColumnHeader() + getPlayerNumber("third") + getDivEnding() + getColumnHeader() + getInputText("third") + getDivEnding() + getDivEnding() 
//                             + getRowHeader() + getColumnHeader() + getPlayerNumber("fourth") + getDivEnding() + getColumnHeader() + getInputText("fourth") + getDivEnding() + getDivEnding() 
//                             + getRowHeader() + getColumnHeader() + getButton() + getDivEnding() + getDivEnding();
//             $("#gameBlock").html(createGameBlock); 
//     }
//     else if(gameName == "ticTacToe"){
//             createGameBlock = getContainer() + getRowHeader() + getColumnHeader() + getPlayerNumber("first") + getDivEnding() + getColumnHeader() + getInputText("first") + getDivEnding()  + getDivEnding()
//                             + getRowHeader() + getColumnHeader() + getPlayerNumber("second") + getDivEnding() + getColumnHeader() + getInputText("second") + getDivEnding() + getDivEnding() 
//                             + getRowHeader() + getColumnHeader() + getButton() + getDivEnding() + getDivEnding();
// $("#gameBlock").html(createGameBlock); 
//     }
}

function getContainer(){
    return `
        <div class = "container">`;
}

function getRowHeader(){
    return `
        <div class = "row">`;
}

function getColumnHeader(){
    return `
        <div class = "col-sm-4">`;
}

function getInputText(id, placeHolder){
    return `
        <input type = "text" class = "form-control" id = "${id}" name = "${id}" placeholder = "${placeHolder}">`;
}

function getButton(){
    return `
        <button type = "submit" id = "submitButton" class = "w-70 btn btn-sm btn-primary">
            Create Game 
        </button>`;
}

function getDivEnding(){
    return `
        </div>`;
}