$(document).ready(function(){
	alert('sam')
	$('button').click(function(){
		var date = $(this).text()
		// alert(date)
		window.location.href = window.location.protocol + date.trim() + '/'
	})
})