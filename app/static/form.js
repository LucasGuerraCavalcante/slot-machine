$(document).ready(function() {

	$('form').on('buttonDisplay', function(event) {

		console.log("teste1");

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
		.done(function(data) {

            $('#coins').html(data.coins);
            $('#a').html(data.a);
            $('#b').html(data.b);
            $('#c').html(data.c);
			$('#status').html(data.status);

			console.log("teste2");
			
		});

		event.preventDefault();

	});

});