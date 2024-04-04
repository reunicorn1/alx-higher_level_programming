$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json',
    function (data, status) {
      if (status === 'success') {
        let value;
        for (const movie of data.results) {
          value = $('<li></li>').text(movie.title);
          $('#list_movies').append(value);
        }
      }
    });
});
