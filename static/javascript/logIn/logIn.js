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
    var currentSessionCookie = getCurrentSession();
    console.log("The current session cookie is: ", currentSessionCookie);
    authenticate(currentSessionCookie);
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
            // authenticate method after clicking apiLogin Sign in button
        // input: event
        // return: none
        // method:
        //      1. url e direct kora theke stop korbo prevent default diye
        //      2. inputEmail id er value nibo
        //      3. inputPassword id er value nibo
        //      4. ajax method
        //          1. method: POST
        //          2. url: api-authenticate
        //          3. data:
        //              1. email: email
        //              2. password: password
        //          4. return paile:
        //              1. method input: response
        //                  1. log korbo response
        $("#apiLoginSubmitButton").click(function(event){
            event.preventDefault();
            var email = $("#inputEmail").val();
            var password = $("#inputPassword").val();
            $.ajax({
                method: 'POST',
                url: 'api/authenticate',
                data:{
                    'email': email,
                    'password': password
                }
            }).done(function(response){
                console.log(response);
            })
        })
        // method: getCurrentSession
        // input: none
        // return: currentSession
        // method:
        //      1. document theke cookie read korbo
        //      2. jodi cookie empty string hoy:
        //          1. return empty string
        //      3. cookie ta decode korbo and variable e save korbo
        //      4. decodedCookie ta ; borabor split korbo
        //      5. splitted cookie er 1st element nibo
        //      6. 1st element er = er index ta khuje ber korbo
        //      7. 1st element er index+2 theke -1 porjonto kete nibo
        //      8. return korbo currentSession
        function getCurrentSession(){
            var cookie = document.cookie;
            if (cookie == ""){
                return "";
            }
            console.log("The cookie is: ",cookie);
            var decodedCookie = decodeURIComponent(cookie);
            var decodedCurrentSession = decodedCookie.split(";");
            console.log("The decodedCurrentSession string is: ", decodedCurrentSession[1]);
            var index = decodedCurrentSession[1].search("=");
            var currentSessionCookie = decodedCurrentSession[1].slice(index+2,-1);
            console.log("The current Session is: ", currentSessionCookie);
            return currentSessionCookie;
        }

        // authenticate
        // input: currentSession
        // return: true if authenticated, false if not
        // method:
        //      1. ajax call korbo:
        //          1. method: POST
        //          2. data: currentSession dict
        //          3. url: /api/authenticate
        //      2. return value response:
        //          1. response ke object e convert korbo
        //          2. jodi response object er data true hoy:
        //              1. return true
        //          3. return false
        function authenticate(currentSessionCookie){
            $.ajax({
                method: 'POST',
                url: '/api/authenticate',
                data:{
                    currentSession : currentSessionCookie
                }
            }).done(function(response){
                console.log(typeof response);
                var responseObject = JSON.parse(response);
                console.log(responseObject);
                console.log("The type of responseObject is: ", typeof responseObject);
                console.log("data is: ",responseObject["data"]);
            })
        }
})