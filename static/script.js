$(document).ready(function() {
    $('#sendButton').click(function() {
        let inputText = $('#inputText').val();

        $.ajax({
            url: '/get_data',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ 'input': inputText }),
            success: function(response){
                console.log(response)
                for(var n of response.response) {
                    $('#numbers').append('<div class="round ' + n.color + '">' + n.number + '</div>')
                    console.log(n)
                }
            },
            error: function(){
                $('#responseText').text('An error occurred.');
            }
        });
    });
});
