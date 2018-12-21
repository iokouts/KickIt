var window = document.window;

window.fbAsyncInit = function() {
    FB.init({
      appId            : 'your-app-id',
      autoLogAppEvents : true,
      xfbml            : true,
      version          : 'v3.1'
    });
};

(function(d, s, id){
    var js, fjs = d.getElementsByTagName(s)[0];

    if (d.getElementById(id)) {return;}

    js = d.createElement(s); js.id = id;
    js.src = "https://connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

document.getElementById('fb_shareBtn').onclick = function() {
    FB.ui({
    method: 'share',
    display: 'popup',
    href: '{{ request.build_absolute_uri }}'
    }, function(response){});
};

document.getElementById('tumblr_shareBtn').onclick = function() {
    window.open('https://www.tumblr.com/widgets/share/tool?canonicalUrl={{ request.build_absolute_uri }}','ShareTumblr','width=540,height=600');
};

document.getElementById('twitter_shareBtn').onclick = function() {
    window.open('https://twitter.com/intent/tweet','ShareTwitter','width=540,height=600');
};