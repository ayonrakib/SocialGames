$(document).ready(function(){
    $("#hostGameButton").on('click', function(){
        $("#hostGameButtonBlock").hide();
        $("#friendsContainer").show();
    })
    // 1. invite friends button e click korle:
    //      1. ajax method call korbo:
    //          1. post method
    //          2. url: api/get-friends
    //          3. data: friendName: friendName dict
    //      2. response ferot paile:
    //          1. response ke json object e convert korbo
    //          2. response['data'] er sob index ee jonno:
    //              1. row er 1st column hobe id, then naame and then invite button
    //          3. friendsBlock block e html akare boshabo uporer sob details
    $("#inviteFriendsButton").on('click', function(){
        var friendName = $("#friendName").val();
        if(friendName == ""){
            $("#modalBody").html("Please insert valid name");
            $("#errorModalButton").trigger("click");
        }
        // console.log(friendName);
        else{
            $.ajax({
                method: 'POST',
                url: 'api/get-friends',
                data:{
                    friendName: `${friendName}`
                }
            }).done(function(response){
                response = JSON.parse(response);
                var friends = "";
                // console.log(response['data'].length);
                if (response['data'].length == 0) {
                    $("#modalBody").html("No friends found, please try again.");
                    $("#errorModalButton").trigger("click");
                } else {
                    for(var index = 0; index < response['data'].length; index++){
                        friends += getRowHeader() + getColumnHeader() + response['data'][index]['id'] + getDivEnding() 
                                 + getColumnHeader() + response['data'][index]['name'] + getDivEnding() 
                                 + getColumnHeader() + getInviteFriendButton(response['data'][index]['id'])  + getDivEnding()+ getDivEnding();
                    }
                    $("#showFriendsBlock").html(friends);
                }
            })
        }

    })
})

function getRowHeader(){
    return `<div class = "row" >`;
}

function getColumnHeader(){
    return `<div class = "col-sm-4" id = "friendsBlock">`;
}

function getInviteFriendButton(buttonId){
    return `<button type = "button" id = ${buttonId} class = "w-50 btn btn-primary">Invite</button>`;
}

function getDivEnding(){
    return `</div>`;
}