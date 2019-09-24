
// One day I'll aply ajax in my project

function sequences() {
	document.getElementById("sequences").innerHTML = 
	'<table>' +
		'<tr>' +
			'<th>[7 7 7]</th>' +
			'<th>Bet x 200</th>' +
			'<th>  </th>' +
	'<p></p>' +
	'<p></p>' +
	'<p></p>' +
	'<p></p>' +
	'<p></p>' +
	'<p></p>' 
}

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