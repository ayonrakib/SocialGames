$(document).ready(function(){
    var currentSession = document.cookie;
    console.log("The current session is: ",currentSession);
    var decodedCookie = decodeURIComponent(currentSession);
    var decodedCurrentSession = decodedCookie.split(";");
    console.log("The decodedCurrentSession string is: ", decodedCurrentSession[1]);
    var index = decodedCurrentSession[1].search("=");
    var currentSessionCookie = decodedCurrentSession[1].slice(index+2,-1);
    console.log("The cookie is: ", currentSessionCookie);
    $('#uploadPictureButton').on('click', function(event) {
        event.preventDefault();
        $('#file-input').trigger('click');
        $.ajax({
            method:'POST',
            url:'upload-picture',
            data:{}
        }).done(function(response){
            console.log(response);
        })
    });
    $.ajax({
        method:'GET',
        url:'get-email',
        data:{}
    }).done(function(email){
        $("#email").val(email);
    })
    $("#modifyDataButton").click(function(){
        console.log("modify data button was clicked");
        console.log("password value is:",$("#password").val());
        var firstName = $("#firstName").val();
        var lastName = $("#lastName").val();
        var password = $("#password").val();
        $.ajax({
            method: 'GET',
            url:'modify-profile',
            data:{
                'firstName':firstName,
                'lastName' : lastName,
                'password':password
            }
        }).done(function(response){
            console.log(response);
        })
    })
})
function uploadPicture(){
    console.log("Upload picture button was clicked");    
}