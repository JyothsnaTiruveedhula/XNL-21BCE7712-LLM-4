$.ajax({
    url: '/chat',
    type: 'POST',
    contentType: 'application/json',
    data: JSON.stringify({ "query": userQuery }),
    success: function(response) {
        var botResponse = response.response;
        $('#chat-box').append('<div class="bot-msg"><strong>Bot:</strong> ' + botResponse + '</div>');
        $('#chat-box').scrollTop($('#chat-box')[0].scrollHeight); // Scroll to the bottom
        
        // Change background based on query
        if (userQuery.toLowerCase().includes('crypto')) {
            setBackgroundImage('crypto');
        } else if (userQuery.toLowerCase().includes('stock')) {
            setBackgroundImage('stock');
        }
    },
    error: function() {
        $('#chat-box').append('<div class="bot-msg"><strong>Bot:</strong> Something went wrong, please try again later.</div>');
    }
});
