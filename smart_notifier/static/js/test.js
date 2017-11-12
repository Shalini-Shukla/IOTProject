$(document).ready(function(){

	var date = document.getElementById("Date-fetch")
	
	$('.schedule-button').click(function(){
		$('#myModal').modal('show')	
		time1 = $(this).data('slot-one')
		time2 = $(this).data('slot-two')
		$('.time-slot-one').text(time1)
		$('.time-slot-two').text(time2)
	});

	$('#submit_button').click(function(){
		var final_string = date.innerHTML;
		final_string = final_string+"," +$('#nameOfEvent').val();
		final_string = final_string+"," +$('#time').val();
		final_string = final_string+"," +$('#importance').val();
		// var data = {'data':final_string}
		url = window.location.href + 'writedata'
		alert(final_string.trim());


		$.ajax({
			type: "GET",
			url: url,
			data: {'data':final_string},
			success: success
		})

	});

	function success(data)
	{
		 location.reload()
	}
})