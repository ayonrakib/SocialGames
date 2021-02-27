function selectGameBlock(){
    // console.log("creategame js is loaded");

    gameForm = getContainer() + "<form>" + getRowHeader() + getColumnHeader() + "Game Title: " + getDivEnding() + getColumnHeader() + getInputText("gameTitle","Game Title") + getDivEnding() + getDivEnding()
             + getRowHeader() + getColumnHeader() + "Game Code: " + getDivEnding() + getColumnHeader() + getInputText("gameCode","Game Code") + getDivEnding() + getDivEnding()
             + getRowHeader() + getColumnHeader() + "Number of Players: " + getDivEnding() + getColumnHeader() + getInputText("numberOfPlayers","Number of Players") + getDivEnding() + getDivEnding()
             + getRowHeader() + getColumnHeader() + "Game Icon: " + getDivEnding() + getColumnHeader() + `<input type="file" id="gameIcon">` + getDivEnding() + getDivEnding()
             + getRowHeader() + getColumnHeader() + getDivEnding() + getColumnHeader() + getButton() + getDivEnding() + "</form>"  + getDivEnding() + getDivEnding();
    $("#gameBlock").html(gameForm);
}

function createNewGame(){
    $( "form" ).submit(function( event ) {
        gameFormData = $( this ).serializeArray();
        // console.log(gameFormData);
        event.preventDefault();
        var gameIconName = $('#gameIcon').prop('files')[0]["name"];
        console.log(gameIconName);
        for(var index = 0; index < gameFormData.length; index++){
            console.log(gameFormData[index]);
        }
      });
    
}

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
        <button type = "submit" id = "submitButton" onclick = "createNewGame()" class = "w-70 btn btn-sm btn-primary">
            Create Game 
        </button>`;
}

function getDivEnding(){
    return `
        </div>`;
}