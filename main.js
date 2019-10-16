var socket = io();
    socket.on('connect', function() 
    {
    	console.log('Connection Established')
        // socket.emit('my event', {data: 'I\'m connected!'});
    });

function handleClick()
{
	var inputBox = document.getElementById('inputBox')
	socket.emit('msg', inputBox.value)
	inputBox.value = ''
}

socket.on('push', function(data)
{
	var chatBox = document.getElementById('chatBox')
	chatBox.innerHTML += data + "<br/>"
})
