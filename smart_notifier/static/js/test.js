$(document).ready(function(){

	var date = document.getElementById("Date-fetch")
	var final_string = date.innerHTML;
	$('.schedule-button').click(function(){
		$('#myModal').modal('show')	
		time1 = $(this).data('slot-one')
		time2 = $(this).data('slot-two')
		$('.time-slot-one').text(time1)
		$('.time-slot-two').text(time2)
	});

	$('#nameOfEvent').change(function(){
		var x = document.getElementById('nameOfEvent');
		final_string = final_string+"," +x.value+",";
	});

	$('#time').change(function(){
		var x = document.getElementById('time');
		final_string = final_string +x.value+",";
	});

	$('#importance').change(function(){
		var x = document.getElementById('importance');
		final_string = final_string +x.value+",";

	});

	$('#submit_button').click(function(){
		// window.location.href = final_string.trim() + '/'
		// alert(final_string.trim());
		$.ajax({
			type: "POST",
			url: window.location.href,
			data: final_string,
			success: success,
			datatype: datatype
		})
	});

	function success(data)
	{
		alert(data);
	}
})