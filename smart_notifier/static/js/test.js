$(document).ready(function(){
	$('.schedule-button').click(function(){
		$('#myModal').modal('show')	
		time1 = $(this).data('slot-one')
		time2 = $(this).data('slot-two')
		// console.log(time1)
		// console.log(time2)
		$('.time-slot-one').text(time1)
		$('.time-slot-two').text(time2)
	})
})