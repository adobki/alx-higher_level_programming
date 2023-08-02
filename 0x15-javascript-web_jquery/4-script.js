// Uses jQuery to toggle header color between red/green when user clicks a DIV

$('DIV#toggle_header').click(function () {
  const header = $('header');

  if (header.attr('class') === undefined) {
    header.addClass('red');
  } else {
    header.toggleClass('red');
    header.toggleClass('green');
  }
});
