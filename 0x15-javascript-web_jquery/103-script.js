// Displays the hello message gotten from an API in chosen language after
// user clicks translate button or presses Enter in the language textbox.

$(document).ready(function(){
	$.loadTranslation = function () {
	  const lang = $('input#language_code').val();
	  const url = 'https://fourtonfish.com/hellosalut/?lang=' + lang;
	  $.get(url, function (hello) {
		  $('DIV#hello').text(hello.hello);
		  console.log(hello.hello);
	  });
	};

	$('INPUT#btn_translate').click(function () {
		$.loadTranslation();
	});

	$('INPUT#language_code').keypress(function (key) {
		if (key.which == 13) {
			$.loadTranslation();
		}
	});
});
