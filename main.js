// console.log(2 + 3)		//gives output in console

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


// function handleClick()
// {
// 	//alert('Hello')
// 	var url = "/users"		//this is a relative url
// 	fetch(url).then(function(res)
// 	{
// 		res.json().then(function(data)
// 		{
// 			console.log(data)
// 		})
// 	})		//In python we did requests.get, here we use fetch
// // code which does not depend on fetch will start executing but the code which requires the fetch function will wait, so we use then function 
// } 