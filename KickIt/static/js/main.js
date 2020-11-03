$(function(){
    var stickymenu = $('#sticky_menu');
    var stickymenuoffset = stickymenu.offset().top + 200;
    var logo_image = $('#logo_path');

    var pathname = window.location.pathname; // Returns path only

    $(window).scroll(function () {
        if($(window).scrollTop() > stickymenuoffset) {
            stickymenu.addClass('sticky');
                logo_image.css("fill", "#fff");
        } else {
            stickymenu.removeClass('sticky');
            if(pathname === '/' && screen.width > 725) {
                logo_image.css("fill", "#000");
            }
        }
    });
});

function changeBackground(x, color){
    x.style.background = color;
}

function resetBackground(x){
    var color;
    (screen.width <= 500) ? color = '#f7f6f6' : color='#fff';
    x.style.background = color;
}

function hamburgerButtonClick(){
    var hamburger = $('.hamburger');
    var menu = $('.menu');

    var is_active = 'is-active';
    var mobile_menu = 'mobile_menu';

    if(!hamburger.hasClass(is_active)) {
        hamburger.addClass(is_active);
        menu.addClass(mobile_menu);
    }
    else {
        hamburger.removeClass(is_active);
        hamburger.removeClass(mobile_menu);
        menu.removeClass(mobile_menu);
    }
}
