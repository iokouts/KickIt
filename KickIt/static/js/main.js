var stickymenu;
var stickymenuoffset;
var scrolltimer;
var logo_image;

window.onload = function() {
    stickymenu = document.getElementById("sticky_menu");
    stickymenuoffset = stickymenu.offsetTop + 200;

    //logo_image = document.getElementById("logo_path");//.getElementsByTagName("path");
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
    x.style.background = '#fff';
}
