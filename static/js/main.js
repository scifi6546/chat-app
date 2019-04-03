$(document).ready(function(){
	$.getJSON('get_messages',function(result){
		print_chat(result);
	});
});
function print_chat(messages){
	var text=""

	for(var i=0;i<messages.length;i++){
		text+=messages[i]['messages'];
		text+='\n';
	}
	$(".chat").text(text);
	console.log(text)
}

