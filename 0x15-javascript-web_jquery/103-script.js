$('document').ready(function () {
  $('#btn_translate').click(button);
  $('#language_code').focus(function () {
    $(this).keydown(function (event) {
      if (event.which === 13) {
        button();
      }
    });
  });
});

function button () {
  const value = $('#language_code').val();
  $.get('https://hellosalut.stefanbohacek.dev/',
    { lang: value },
    function (data) {
      const decodedText = $('<div/>').html(data.hello).text();
      $('#hello').text(decodedText);
    });
}
