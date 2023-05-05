// Uses jQuery/AJAX to display a character name gotten from an API

$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: function (character) {
      $('DIV#character').text(character.name);
    }
  });
});
