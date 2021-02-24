$(document).ready(function(){
    // searchFriend id te click er function
    // input: none
    // return: none, just replace with the found users
    // method:
    //  1. friendName input er val read korbo
    //  2. ajax method:
    //      1. input: method: get, url: getfriends, data:{name:friendName}
    //  3. ei method er return value er jonno done method call
    //  4. input: function definition with the response value from the server
    //      1. friendNumber = 1
    //      2. friendsBlock hobe row header, 1st column header, image and columnend
    //      3. friends empty string
    //      4. response object(eval(response)) er len porjonto iterate and friendNumber++:
    //          1. friends += friendsBlock + column shuru + response[index]['name'] + column shesh + column shuru + addfreind(response[index]['email']) + column shesh + column shuru + blockFriend + column shesh+ row shesh
    //      5. friends id te friends boshabo page reload chara
    $("#searchFriend").click(function(){
        var friendEmail = $('#friendName').val();
        $.ajax({
            method: 'GET',
            url: '/get-friends',
            data: {email: friendEmail}
        }).done(function(response){
            console.log(eval(response));
            var friendNumber = 1;
            var friendsBlock = rowBlockHeader(friendNumber) + columnHeader(3) + imageBlock() + columnFooter();
            var friends = "";
            if (eval(response).length >=1){
                for(var index = 1; index < eval(response).length; index++, friendNumber++){
                    console.log(eval(response)[index]["status"]);
                    if(eval(response)[index]["status"] == "requested"){
                        friends += friendsBlock + columnHeader(3) + eval(response)[index]["name"] + columnFooter() 
                                + columnHeader(3) + button(`${eval(response)[index]["id"]}`,"remove","Remove", `${eval(response)[index]["id"]}`) + columnFooter() + columnHeader(3) + button(`${eval(response)[index]["id"]}`,"block","Block", `${eval(response)[index]["id"]}`) + columnFooter() + rowBlockFooter();
                    }
                    else if(eval(response)[index]["status"] == "accepted"){
                        friends += friendsBlock + columnHeader(3) + eval(response)[index]["name"] + columnFooter() 
                                + columnHeader(3) + button(`${eval(response)[index]["id"]}`,"remove","Remove", `${eval(response)[index]["id"]}`) + columnFooter() + columnHeader(3) + button(`${eval(response)[index]["id"]}`,"block","Block", `${eval(response)[index]["id"]}`) + columnFooter() + rowBlockFooter();
                    }
                    else if(eval(response)[index]["status"] == "rejected" || eval(response)[index]["status"] == ""){
                        friends += friendsBlock + columnHeader(3) + eval(response)[index]["name"] + columnFooter() 
                                + columnHeader(3) + button(`${eval(response)[index]["id"]}`,"add","Add Friend", `${eval(response)[index]["id"]}`) + columnFooter() + columnHeader(3) + button(`${eval(response)[index]["id"]}`,"block","Block", `${eval(response)[index]["id"]}`) + columnFooter() + rowBlockFooter();
                    }
                    else if(eval(response)[index]["status"] == "blocked"){
                        friends += friendsBlock + columnHeader(5) + eval(response)[index]["name"] + columnFooter() 
                                +  columnHeader(3) + button(`${eval(response)[index]["id"]}`,"unblock","Unblock", `${eval(response)[index]["id"]}`) + columnFooter() + rowBlockFooter();
                    }
                }
            }
            $('#friends').html(friends);
        });
    });
    setInterval(function(){
        $.ajax({
            method: 'GET',
            url: 'get-my-friends',
            data: {}
        }).done(function(response){
            console.log(response);
            var friendNumber = 1;
            var friendsBlock = rowBlockHeader(friendNumber) + columnHeader(3) + imageBlock() + columnFooter();
            var friends = "";
            if (eval(response).length >=1){
                for(var index = 0; index < eval(response).length; index++, friendNumber++){
                        friends += friendsBlock   + columnHeader(3) + eval(response)[index]["name"] + columnFooter() 
                                + columnHeader(3) + button(`${eval(response)[index]["id"]}`,"remove","Remove", `${eval(response)[index]["id"]}`) 
                                +  columnFooter() + columnHeader(3) + button("blockFriend"+`${eval(response)[index]["id"]}`,"block","Block",`${eval(response)[index]["id"]}`) + columnFooter() + rowBlockFooter();                    
                }
            }
            $('#myFriends').html(friends);
        })
    },10000);
    setInterval(function(){
        $.ajax({
            method: 'GET',
            url: 'get-pending-requests',
            data: {}
        }).done(function(response){
            console.log("pending requests",response);
            var friendNumber = 1;
            var friendsBlock = rowBlockHeader(friendNumber) + columnHeader(2) + imageBlock() + columnFooter();
            var friends = "";
            if (eval(response).length >=1){
                
                for(var index = 0; index < eval(response).length; index++, friendNumber++){
                        // friends += friendsBlock   + columnHeader(2) + eval(response)[index]["name"] + columnFooter() 
                        //         +  columnHeader(3) + button(`${eval(response)[index]["id"]}`,"accept","Accept", `${eval(response)[index]["id"]}`,)
                        //         +  columnFooter() + columnHeader(3) + button(`${eval(response)[index]["id"]}`,"remove","Remove", `${eval(response)[index]["id"]}`) 
                        //         +  columnFooter() + columnHeader(2) + button(`${eval(response)[index]["id"]}`,"block","Block", `${eval(response)[index]["id"]}`) + columnFooter() + rowBlockFooter();                    
                        console.log(eval(response));
                        if(eval(response)[index]["status"] == "requested"){
                            // console.log("came in if");
                            friends += friendsBlock + columnHeader(2) + eval(response)[index]["name"] + columnFooter() 
                                    + columnHeader(2) + button(`${eval(response)[index]["id"]}`,"add","Add", `${eval(response)[index]["id"]}`) + columnFooter()
                                    + columnHeader(3) + button(`${eval(response)[index]["id"]}`,"remove","Remove", `${eval(response)[index]["id"]}`) + columnFooter() + columnHeader(3) + button(`${eval(response)[index]["id"]}`,"block","Block", `${eval(response)[index]["id"]}`) + columnFooter() + rowBlockFooter();
                        }
                        else if(eval(response)[index]["status"] == "accepted"){
                            // console.log("came in else if");
                            friends += friendsBlock + columnHeader(3) + eval(response)[index]["name"] + columnFooter() 
                                    + columnHeader(3) + button(`${eval(response)[index]["id"]}`,"remove","Remove", `${eval(response)[index]["id"]}`) + columnFooter() + columnHeader(3) + button(`${eval(response)[index]["id"]}`,"block","Block", `${eval(response)[index]["id"]}`) + columnFooter() + rowBlockFooter();
                        }
                        else if(eval(response)[index]["status"] == "rejected" || eval(response)[index]["status"] == ""){
                            // console.log("came in 2nd else if");
                            friends += friendsBlock + columnHeader(3) + eval(response)[index]["name"] + columnFooter() 
                                    + columnHeader(3) + button(`${eval(response)[index]["id"]}`,"add","Add Friend", `${eval(response)[index]["id"]}`) + columnFooter() + columnHeader(3) + button(`${eval(response)[index]["id"]}`,"block","Block", `${eval(response)[index]["id"]}`) + columnFooter() + rowBlockFooter();
                        }
                    }
            }
            $('#pendingRequests').html(friends);
        })
    },10000);
    // $(document).on('click', '#removeFriend', function(){
    //     $(this).parent().parent().hide();
    //     $.ajax({
    //         method: 'GET',
    //         url: '/remove',
    //         data:{
    //             'userWhoRemoved' : 'a',
    //             'userToBeRemoved': 'b'
    //         }
    //     }).done(function(response){
    //         console.log(response);
    //     })
    // })
    // function removeFriend
    // input: id of friend to remove
    // return: send data to server to remove friend
    // method:
    //      1. ajax er method: get
    //      2. ajax er url: remove-friend
    //      3. data: friend id
    //      4. done hoile:
    //          1. function(response)
    //          2. console e log korbo response



$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus');
    })
$(document).on('click', '#blockFriend', function(){
    $(this).parent().parent().hide();
});
});

function removeFriend(friend_id){
    $.ajax({
        method: "GET",
        url: "remove-friend",
        data: {'userToBeRemoved': friend_id}
    }).done(function(response){
        console.log(response);
    })
}

function rowBlockHeader(friendNumber){
    return `<div class = "row" id = friendNumber${friendNumber}>`;
}

function columnHeader(columnWidth){
    return `<div class = "col-sm-${columnWidth} col-lg-${columnWidth}" id = "">`;
}

function imageBlock(){
    return '<img src = "/images/tictactoe.png" height = "40px" width = "40px">';
}

function firstNameBlock(){
    return 'Rakib';
}

function lastNameBlock(){
    return 'Ayon';
}

function button(buttonId, action, buttonValue, userToBeAddedOrRemoved){
    return `<button type = "button" id = ${buttonId} onclick = "${action}Friend('${userToBeAddedOrRemoved}')" class = "w-70 btn btn-sm btn-primary">
            ${buttonValue} </button>`;
}

function columnFooter(){
    return '</div>';
}

function rowBlockFooter(){
    return '</div>';
}

function addFriend(friend_id){
    console.log(friend_id);
    $.ajax({
        method: 'GET',
        url: 'add-friend',
        data: {
            'friend_id' : friend_id
        }
    }).done(function(response){
        console.log("addfriend response:  ");
        console.log(response);
    })
}

function acceptFriend(friend_id){
    $.ajax({
        method: "GET",
        url: 'accept-friend',
        data:{
            'friend_id': friend_id
        }
    }).done(function(response){
        console.log("addfriend response:  ");
        console.log(response);
    });
}

function blockFriend(friend_id){
    $.ajax({
        method: 'GET',
        url: 'block-friend',
        data:{
            'friend_id': friend_id
        }
    }).done(function(response){
        console.log(response);
        
    })
}

function unblockFriend(friend_id){
    $.ajax({
        method: 'GET',
        url: 'unblock-friend',
        data:{
            'friend_id': friend_id
        }
    }).done(function(response){
        console.log(response);
        
    })
}

function friendRequestAlreadySent(){
    return `<!-- Button trigger modal -->
    <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal">
        Launch demo modal
      </button>
      
      <!-- Modal -->
      <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              Hello World
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
              <button type="button" class="btn btn-primary">Save changes</button>
            </div>
          </div>
        </div>
      </div>`
}