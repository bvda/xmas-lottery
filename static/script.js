$(document).ready(function(){
    $('#sendButton').click(function(){
        let inputText = $('#inputText').val();
        
        $.ajax({
            url: '/get_data',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ 'input': inputText }),
            success: function(response){
                $('#responseText').text(response.response);
            },
            error: function(){
                $('#responseText').text('An error occurred.');
            }
        });
    });
});
