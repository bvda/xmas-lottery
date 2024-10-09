$(document).ready(function() {       
     $.ajax({
            url: '/get_data',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ 'input': inputText }),
            success: function(response){
                console.log(response)
            },
            error: function(){
                $('#responseText').text('An error occurred.');
            }
        });
    $('#sendButton').click(function() {
        $.ajax({
            url: '/get_draw',
            type: 'GET',
            contentType: 'application/json',
            success: (resp) => {
                $('#numbers').empty()
                for(var n of resp.response[1]) {
                    $('#numbers').append('<div class="round ' + n.color + '">' + n.number + '</div>')
                    console.log(n)
                }
                console.log(resp)
            }
        })
    });

});
