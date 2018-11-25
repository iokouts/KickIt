var stickymenu;
var stickymenuoffset;
var logo_image;

window.onload = function() {
    stickymenu = document.getElementById("sticky_menu");
    stickymenuoffset = stickymenu.offsetTop + 200;

    logo_image = $("#logo_path");
};

window.addEventListener("scroll", function(e){
    requestAnimationFrame(function(){
        if (window.pageYOffset > stickymenuoffset){
            stickymenu.classList.add('sticky');
            logo_image.css("fill","#fff");
        }
        else{
            stickymenu.classList.remove('sticky');
            logo_image.css("fill","#000");
        }
    })
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
    var hamburger = $('.hamburger--spin');
    var menu = $('.menu');

    var is_active = 'is-active';
    var mobile_menu = 'mobile_menu';

    if(!hamburger.hasClass(is_active)) {
        hamburger.addClass(is_active);
        menu.addClass(mobile_menu);
    }
    else {
        hamburger.removeClass([is_active, mobile_menu]);
        menu.removeClass(mobile_menu);
    }
}
