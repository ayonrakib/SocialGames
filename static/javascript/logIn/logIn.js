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
        // authenticate method after clicking apiLogin Sign in button
        // input: none
        // return: none
        // method:
        //      1. inputEmail id er value nibo
        //      2. inputPassword id er value nibo
        //      3. ajax method
        //          1. method: POST
        //          2. url: api-authenticate
        //          3. data:
        //              1. email: email
        //              2. password: password
        //          4. return paile:
        //              1. method input: response
        //                  1. log korbo response
        $("#apiLoginSubmitButton").click(function(){
            var email = $("#inputEmail")
        })
    })
})