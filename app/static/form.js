
clicks = 0

function sequences() {
	clicks = clicks + 1
    if (clicks == 1) {
		document.getElementById("sequences").innerHTML = 
		'<table class="greenText">' +
			'<tr>' +
				'<th>[7 7 7]</th>' +
				'<th>Bet x 200</th>' +
				'<th> 0.009% </th>' +
			'</tr>' +
			'<tr>' +
				'<th>[A A A]</th>' +
				'<th>Bet x 100</th>' +
				'<th> 0.057% </th>' +
			'</tr>' +
			'<tr>' +
				'<th>[♠ ♠ ♠]</th>' +
				'<th>Bet x 100</th>' +
				'<th> 0.076% </th>' +
			'</tr>' +
			'<tr>' +
				'<th>[♠ ♠ A]</th>' +
				'<th>Bet x 100</th>' +
				'<th> 0.038% </th>' +
			'</tr>' +
			'<tr>' +
				'<th>[♣ ♣ ♣]</th>' +
				'<th>Bet x 18</th>' +
				'<th> 0.378% </th>' +
			'</tr>' +
			'<tr>' +
				'<th>[♣ ♣ A]</th>' +
				'<th>Bet x 18</th>' +
				'<th> 0.047% </th>' +
			'</tr>' +
			'<tr>' +
				'<th>[♥ ♥ ♥]</th>' +
				'<th>Bet x 14</th>' +
				'<th> 0.595% </th>' +
			'</tr>' +
			'<tr>' +
				'<th>[♥ ♥ A]</th>' +
				'<th>Bet x 14</th>' +
				'<th> 0.009% </th>' +
			'</tr>' +
			'<tr>' +
				'<th>[♦ ♦ ♦]</th>' +
				'<th>Bet x 10</th>' +
				'<th> 0.945% </th>' +
			'</tr>' +
			'<tr>' +
				'<th>[♦ ♦ A]</th>' +
				'<th>Bet x 10</th>' +
				'<th> 0.236%   </th>' +
			'</tr>' +
			'<tr>' +
				'<th>[☺ ☺ ANY]</th>' +
				'<th>Bet x 2</th>' +
				'<th> 2.484% </th>' +
			'</tr>' +
			'<tr>' +
				'<th>[☺ ANY ANY]</th>' +
				'<th>Bet x 2</th>' +
				'<th> 9.524% </th>' +
			'</tr>' +
		'</table>'

	} else if (clicks > 1) {
        document.getElementById("sequences").innerHTML = "";
        clicks = 0
    }

}

// One day I'll aply ajax in my project

$(function(){
	$('buttonDisplay').click(function(){
		var bet = $('#buttonDisplay').val();
		// var pass = $('#inputPassword').val();
		$.ajax({
			url: '/bet',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});