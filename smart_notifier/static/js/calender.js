$(document).ready(function(){
	$('button').click(function(){
		var date = $(this).text()
		window.location.href = window.location.protocol + date.trim() + '/'
	})
})