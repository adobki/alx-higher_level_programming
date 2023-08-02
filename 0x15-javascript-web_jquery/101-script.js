// Uses jQuery to add an element to a list when user clicks a DIV

// Adds an item to the list
$('DIV#add_item').click(function() {
    $('UL.my_list').append('<li>Item</li>');
});

// Removes last item from the list
$('DIV#remove_item').click(function() {
    $('UL.my_list li:last-child').remove();
});

// Clears/empties the list
$('DIV#clear_list').click(function() {
    $('UL.my_list').empty();
});
