import $ from 'jquery';

window.jQuery = window.$ = $;
require('flexslider'); // This uses the NPM-package

$(function(){
  $('.flexslider').flexslider({
    animation: "fade",
    slideshow: true,
    slideshowSpeed: 4000,
    controlNav: false,
    prevText: '<',
    nextText: '>'
  })
});
