// Uses jQuery/AJAX to display the hello message gotten from an API

$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    headers: { 'Access-Control-Allow-Origin': '*' },
    success: function (hello) {
      $('DIV#hello').text(hello.hello);
      console.log(hello);
    }
  });
});
