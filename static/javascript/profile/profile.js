$(document).ready(function(){
    $('#uploadPictureButton').on('click', function(event) {
        event.preventDefault();
        $('#file-input').trigger('click');

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