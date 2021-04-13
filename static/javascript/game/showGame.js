$(document).ready(function(){
        $.ajax({
            method: 'POST',
            url: 'api/show-games',
            data: {}
        }).done(function(response){
            console.log(response);
            response = JSON.parse(response);
            console.log(response['error']);
        });
})

function getContainer(){
    return `<div class = "container">`;
}

function getRowHeader(){
    return `<div class = "row">`;
}

function getColumnHeader(){
    return `<div class = "col-lg">`;
}

function getDivEnding(){
    return `</div>`;
}