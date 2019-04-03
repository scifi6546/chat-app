var chat="<div class=\"wrapper\">\
<div class=\"subject\">subject: %subject%</div>\
<div class=\"username\">usename: %username%</div>\
<div class=\"message_cont\">message: %message%</div>\n \
</div>";

$(document).ready(function(){
	setInterval(get_chat(),300);
});
function get_chat(){
	$.getJSON('get_messages',function(result){
		print_chat(result);
	});
}
function send_message(input){
	console.log(input);
	console.log(input[0].value);
	console.log(input[1].value);
	message={"subject":input[0].value,"username":input[1].value,
	"messages":input[2].value};
	console.log(message);
	$.ajax({url:"post_message",
		type:"POST",
		data:JSON.stringify(message),
		contentType: 'application/json; charset=utf-8',
		dataType: 'json',
		async: false
		});
	get_chat();
}
function print_chat(messages){
	var text=""

	for(var i=0;i<messages.length;i++){
		var temp_text = chat;
		temp_text = temp_text.replace("%message%",messages[i]['messages']);
		temp_text=temp_text.replace("%subject%",messages[i]['subject']);
		temp_text=temp_text.replace("%username%",messages[i]['username']);
		text+=temp_text;
		
	}
	$(".chat").html(text);
	console.log(text)
}

