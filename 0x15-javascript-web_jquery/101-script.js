$(document).ready(function () {
  $('#add_item').click(function () {
    const item = '<li>Item</li>';
    $('.my_list').append(item);
  });

  $('#remove_item').click(function () {
    $('.my_list li:last').remove();
  });

  $('#clear_list').click(function () {
    $('.my_list').empty();
  });
});
