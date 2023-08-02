// Uses jQuery to add an element to a list when user clicks a DIV

let count = 0;

// Adds an item to the list
$('DIV#add_item').click(function() {
//    $('UL.my_list').append('<li>Item</li>');
    $('UL.my_list').append('<li>Item ' + ++count +' </li>');
});

// Removes last item from the list
$('DIV#remove_item').click(function() {
    if (count > 0) {
        count--;
    };
    let my_list = $('UL.my_list');
    my_list.removeChild(my_list.childNodes[count]);
});

// Clears/empties the list
$('DIV#clear_list').click(function() {
    count = 0;
    $('UL.my_list').empty();
});
