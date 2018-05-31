$('#fib_form').submit(function () {
    console.log('Fibonacci');
    var number = $('#input_number').val();
    console.log(number)
    $.ajax ({
		url: 'getfibonacci',
        type: 'POST',
		data: {'data': number},
		success: [
		    function(response) {
			if (response.data) {
				console.log(response.data)
			} else {
				console.log(response.error);
			}
		}],
		error: [function(xhr, errormsg, err) {
			console.log('xhr status ' + xhr.responseText);
		}]
	});
});