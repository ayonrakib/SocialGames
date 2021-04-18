
$(document).ready(function(){
    $("#inviteFriendsButton").on('click', function(){
        var friendName = $("#friendName").val();
        // console.log(friendName);
        $.ajax({
            method: 'POST',
            url: 'api/get-friends',
            data:{
                friendName: `${friendName}`
            }
        }).done(function(response){
            response = JSON.parse(response);
            console.log(response);
            function printValues(response) {
                for(var k in response) {
                    if(response[k] instanceof Object) {
                        printValues(response[k]);
                    } else {
                        console.log(response[k]);
                    };
                }
            };
            
            // Printing all the values from the resulting object
            printValues(response);
            
        })
    })
})