//when loading more posts, change the background color
$('.load_more_posts').click(
    function () {
        $(this).css('color', '#ffffff');
        $('.podcasts_grid_container').css('background',
                'linear-gradient(180deg, #ffffff 830px, #e84070 0)');
});

//Bind events to parent element, using .on() , in order to target the elements
//that are loaded with endless paginate callback.

//on hover change the background color according to the index
//after the 8 first elements we change the color
$('.podcasts_grid').on('mouseenter', '.podcast_single', function (event) {
    var hoverColor = '#e84070';
    if($(this).index() > 7)
        hoverColor = '#ffffff';

    $(this).css('background-color', hoverColor);
});

$('.podcasts_grid').on('mouseleave','.podcast_single', function (event) {
    var originalColor = '#ffffff';
    if( $(this).index() > 7 )
        originalColor = '#e84070';

    $(this).css('background-color', originalColor);
});