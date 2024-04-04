const element = document.querySelector('#red_header');
const header = document.querySelector('header');

$(document).ready(function () {
  $(element).click(function () {
    $(header).addClass('red');
  });
});
