function selectGameBlock(){
    // console.log("creategame js is loaded");

    gameForm = getContainer() + "<form id = 'createGameForm'>" + getRowHeader() + getColumnHeader() + "Game Title: " + getDivEnding() + getColumnHeader() + getInputText("gameTitle","Game Title") + getDivEnding() + getDivEnding()
             + getRowHeader() + getColumnHeader() + "Game Code: " + getDivEnding() + getColumnHeader() + getInputText("gameCode","Game Code") + getDivEnding() + getDivEnding()
             + getRowHeader() + getColumnHeader() + "Number of Players: " + getDivEnding() + getColumnHeader() + getInputText("numberOfPlayers","Number of Players") + getDivEnding() + getDivEnding()
             + getRowHeader() + getColumnHeader() + "Game Icon: " + getDivEnding() + getColumnHeader() + `<input type="file" id="gameIcon">` + getDivEnding() + getDivEnding()
             + getRowHeader() + getColumnHeader() + getDivEnding() + getColumnHeader() + getButton() + getDivEnding() + "</form>"  + getDivEnding() + getDivEnding();
    $("#gameBlock").html(gameForm);
    

    // create game form
    // input: event
    // return: none
    // method:
    //      1. submit button e click korar por direct bondho korbo
    //      2. form data er sob value read korbo
    //      3. icon name read korbo form data theke
    //      4. title name read korbo form data theke
    //      5. code name read korbo form data theke
    //      6. player number read korbo form data theke
    //      7. sob gula print korbo
    //      8. jodi kono data undefined na hoy:
    //          1. ajax call korbo:
    //              1. method: POST
    //              2. url: api/create-game
    //              3. data:
    //                  1. title name
    //                  2. code name
    //                  3. player number
    //                  4. icon name
    //              4. response paile:
    //                  1. jodi response data true hoy:
    //                      1. log korbo rresponse
    $(document).ready(function(){
        $( "#createGameForm" ).submit(function( event ) {
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
            if((gameIconName != undefined) && (gameTitle != undefined) && (gameCode != undefined)&& (numberOfPlayers != undefined)){
                $.ajax({
                    method: 'POST',
                    url: 'api/create-game',
                    data: {
                        'gameTitle': gameTitle,
                        'gameCode' : gameCode,
                        'numberOfPlayers' : numberOfPlayers,
                        'gameIcon' : gameIcon
                    }
                }).done(function(response){
                    console.log(response);
                })
            }

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