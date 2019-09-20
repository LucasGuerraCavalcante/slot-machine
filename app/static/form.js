$(document).ready(function() {

	$('form').on('buttonDisplay', function(event) {

		$.ajax({
			data : {
                bet : $('#bet').val(),
                coins : $('#coins').val(),
                a : $('#a').val(),
                b : $('#b').val(),
                c : $('#c').val(),
                status : $('#status').val(),
                space : $('#space').val()
			},
			type : 'POST',
			url : '/bet'
		})
		.done(function(data) {

            // ajeitar no HTML ids cada um

			$('#successAlert').text(data.name).show();
            $('#errorAlert').text(data.name).show();
            $('#successAlert').text(data.name).show();
            $('#errorAlert').text(data.name).show();
            $('#successAlert').text(data.name).show();
            $('#errorAlert').text(data.name).show();
            $('#errorAlert').text(data.name).show();

		});

		event.preventDefault();

	});

});