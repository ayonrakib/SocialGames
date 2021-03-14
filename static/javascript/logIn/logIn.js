$(document).ready(function(){
    // 1. loginSubmitButton button e click korle function
    // 2. input none
    // 3. return: none
    // method:
    //      1. ajax request korbo:
    //          1. url: 'get-request-header'
    //          2. headers: {"Authorization": "Basic abcd"}
    //      2. response paile:
    //          1. console e log korbo response
    $("#loginSubmitButton").click(function(){
        // console.log("Clicked on login button");
        $.ajax({
            method: 'GET',
            url: 'get-request-header',
            headers: {"Authorization": "Basic abcd"}
        }).done(function(response){
            console.log(response);
        })
    })
})