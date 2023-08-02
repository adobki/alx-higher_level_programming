// Displays the hello message gotten from an API in chosen language
// after user clicks translate button.

$(document).ready(function(){
	$('INPUT#btn_translate').click(function () {
	  const lang = $('input#language_code').val();
	  const url = 'https://fourtonfish.com/hellosalut/?lang=' + lang;
	  $.get(url, function (hello) {
		  $('DIV#hello').text(hello.hello);
		  console.log(hello.hello);
	  });
	});
});
