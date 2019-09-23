$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
                coins : $('#coins').val(),
                a : $('#a').val(),
                b : $('#b').val(),
                c : $('#c').val(),
                status : $('#status').val(),
			},
			type : 'POST',
			url : '/bet'
		})

		event.preventDefault();

	});

});