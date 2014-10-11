$('.js-captcha-refresh').click(function() {
	/* Act on the event */
	$form = $(this).parents('form');
	$.getJSON(($(this),{}, function(json) {
			/*optional stuff to do after success */
	});
	return false
});