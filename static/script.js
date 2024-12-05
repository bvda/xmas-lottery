let ticker;
let count = 0

function pull() {
    $.ajax({
        url: '/get_draw',
        type: 'GET',
        contentType: 'application/json',
        success: (resp) => {
            $('#current').empty()
            let current = resp.response[1].at(-1)
            console.log(current)
            $('#current').append('<div class="roboto-mono-medium round ' + current.color + '">' + 
                '<p>Litra ' + current.litra +  '</p>' +
                '<p> NR.' +  String(current.number).padStart(3, '0') + '</p></div>')
            $('#numbers').empty()
            for(var n of resp.response[1].slice(0, -1)) {
                $('#numbers').append('<div class="roboto-mono-medium round ' + n.color + '">' + n.number + '</div>')
                console.log(n)
            }
            console.log(resp)
            count++
            if(count >= 5  ) {
                clearInterval(ticker)
                count = 0
            }
        }
    })
}

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
        $('#clear').click(() => {
            $.ajax({
                url:'/clear',
                type: 'POST',
            
        success: (resp) => {
            $('#current').empty()
            $('#numbers').empty()
            console.log(resp)
        
        }})
    })
    $('#sendButton').click(function() {
        pull()
        ticker = setInterval(pull, 1000)
    });

});
