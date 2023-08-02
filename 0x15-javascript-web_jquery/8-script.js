// Uses jQuery/AJAX to display a list of movies gotten from an API

$(function () {
  const moviesList = $('#list_movies');

  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (movies) {
      $.each(movies.results, function (i, movie) {
        moviesList.append('<li> ' + movie.title + ' </li>');
      });
    }
  });
});
