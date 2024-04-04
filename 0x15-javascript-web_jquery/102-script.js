$('document').ready(function () {
  $('#btn_translate').click(function () {
    const value = $('#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/',
      { lang: value },
      function (data) {
        const decodedText = $('<div/>').html(data.hello).text();
        $('#hello').text(decodedText);
      });
  });
});
