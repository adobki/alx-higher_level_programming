// Uses jQuery to add an element to a list when user clicks a DIV

$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
