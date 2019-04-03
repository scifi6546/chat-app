var chat="<div class=\"wrapper\">\
<div class=\"subject\">subject: %subject%</div>\
<div class=\"message_cont\">message: %message%</div>\n \
</div>";

$(document).ready(function(){
	$.getJSON('get_messages',function(result){
		print_chat(result);
	});
});
function print_chat(messages){
	var text=""

	for(var i=0;i<messages.length;i++){
		var temp_text = chat;
		temp_text = temp_text.replace("%message%",messages[i]['messages']);
		temp_text=temp_text.replace("%subject%",messages[i]['subject']);
		text+=temp_text;
		
	}
	$(".chat").append(text);
	console.log(text)
}

