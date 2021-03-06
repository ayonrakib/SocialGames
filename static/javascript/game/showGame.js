// 1. document ready hoile:
//      1. 10 sec por por game data show korbo 
//      2. method: showGame
//      3. input: none
//      4. return: none
//      5. method:
//          1. ajax method e data POST korbo:
//              1. POST method
//              2. url: api/show-games
//              3. data empty dict
//              4. response paile:
//                  1. response show korbo
//                  2. response ke json object banabo
//                  3. jodi response['data'] false hoy:
//                      1. log korbo error ta
//                  4. noile:
//                      1. gameData variable banabo empty string
//                      2. response['data'] er sob index er jonno:
//                          1. game title e title, icon e pic, path e url, number of players e number of players boshabo
//                          2. notun row create korbo
//                  5. gameBlock e ei pura data gula html akare boshabo
//                  6. button e click korle:
//                      1. button er id read korbo
//                      2.  
$(document).ready(function(){
    // setInterval(showGame,10000);
    // function showGame(){
        $.ajax({
            method: 'POST',
            url: 'api/show-games',
            data: {}
        }).done(function(response){
            // console.log(response);
            response = JSON.parse(response);
            // console.log("image name is: ",response['data'][0]['gameIcon']);
            if (response['data'] == false){
                console.log(response['error']);
            }
            else{
                var gameData = "";
                for(var index = 0; index < response['data'].length; index++){
                    // console.log(key, response['data'][index][key]);
                    var imageHTML = `<img src="images/profilePicture/${response['data'][index]['gameIcon']}">`;
                    // console.log("image html is:",imageHTML);
                    gameData += getRowHeader() + getColumnHeader('gameTitleBlock') + response['data'][index]['gameTitle'] + getDivEnding()
                               +getColumnHeader('gameIconBlock') + `<img src="images/profilePicture/${response['data'][index]['gameIcon']}" height="50px" width="50px">`  + getDivEnding()
                               +getColumnHeader('gamePathBlock') + response['data'][index]['gamePath'] + getDivEnding()
                               +getColumnHeader('numberOfPlayersBlock') + response['data'][index]['numberOfPlayers'] + getDivEnding() +getColumnHeader() + getButton(response['data'][index]['id']) + getDivEnding();
                    // $(".gameIconBlock").html(`<img src="images/profilePicture/${response['data'][index]['gameIcon']}" height="50px" width="50px">`);
                }
                $(".gameBlock").html(gameData);
                // $(".imageBlock").html(`<img src="images/profilePicture/${response['data'][0]['gameIcon']}" height="50px" width="50px">`);
                $("button").on('click', function(){
                    var buttonId = $(this).attr('id');
                    console.log("The button id is: ",buttonId);
                    $.ajax({
                        method: 'POST',
                        url: 'api/get-game-url',
                        data:{
                            id: `${buttonId}`
                        }
                    }).done(function(response){
                        response = JSON.parse(response);
                        // console.log(response['data']);
                        window.location = `${response['data']}`;
                    })
                    
                })
            }
        });
        // 1. join button e click korle
        //      2. log hello world

})

function getContainer(){
    return `<div class = "container">`;
}

function getRowHeader(){
    return `<div class = "row">`;
}

function getColumnHeader(columnId){
    return `<div class = "col-sm-2 ${columnId}">`;
}

function getDivEnding(){
    return `</div>`;
}

function getButton(buttonId){
    return `<button class = "w-50 btn btn-sm btn-primary" id = ${buttonId}>Play</button>`
}