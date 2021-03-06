# KickIt!

music blog 

## Built With

* [Wagtail](https://wagtail.io) - the powerfull CMS for modern websites
	* [Wagtail Docs](http://docs.wagtail.io/en/latest/index.html)

## Installation
* pull
* use venv with python 3.6
```bash
$ pip install -r requirements.txt
$ python manage.py migrate
```
* creates a SQLite database file in the project directory (default)
```bash
$ python manage.py createsuperuser
$ python manage.py runserver
```

## Deploy with Docker
* add nginx/media.conf to /home/dokku/.volumes/{app name}/nginx.conf.d/

## Setup
* set site name in Wagtail Admin -> Settings -> Site
* add social media accounts: Settings -> SiteSettings
* ~~set mailchimp newsletter Subscribe Form: KickIt/templates/includes/footer.html~~
* create Collections for media and manage permissions of User Groups

## TODO
### Dev
- [ ] Add Podcasts Tags (same as post tags?)
- [ ] check browser/mobile compatibility
- [ ] SEO
- [ ] improve readability with HTML5 tags
- [ ] minify css [django asset-managers](https://djangopackages.org/grids/g/asset-managers/)
- [ ] add help text to model properties

### Design
- [ ] Author / Author Index Pages

    
## Resources
### General
* [Let's Encrypt SSL Certificate](https://letsencrypt.org/)
* [ngrok - tunnels to locahost. for test purposes](https://ngrok.com/)
* [you might not need jquery](http://youmightnotneedjquery.com/)
* Responsive Design
	* [by google](https://developers.google.com/web/fundamentals/design-and-ux/responsive/)
* Social Sharing
    * [twitter cards](https://developer.twitter.com/en/docs/tweets/optimize-with-cards/overview/abouts-cards) / [twitter button guides](https://developer.twitter.com/en/docs/twitter-for-websites/tweet-button/overview.html)
	* [Facebook Share Dialog](https://developers.facebook.com/docs/sharing/reference/share-dialog) / [~~facebook share button~~](https://developers.facebook.com/docs/plugins/share-button/#)
	* [Facebook Include JS SDK](https://developers.facebook.com/docs/javascript/quickstart)
    * [tumblr buttons](https://www.tumblr.com/buttons)

* [MailChimp API](https://developer.mailchimp.com/documentation/mailchimp/guides/get-started-with-mailchimp-api-3/#resources)
* [LightGallery Post Image Gallery](https://github.com/sachinchoolur/lightGallery) - [Codepen Demo](https://codepen.io/sachinchoolur/pen/QjLNMM)

### Django / Wagtail
* [wagtailmenus](https://github.com/rkhleics/wagtailmenus)
* [wagtail metadata](https://github.com/takeflight/wagtail-metadata)
* Pagination
	* [django-el-pagination](https://django-el-pagination.readthedocs.io/en/latest/)
	* [reddit help](https://www.reddit.com/r/django/comments/9p70uf/adding_load_more_functionality_to_wagtail_via/)
* [django-newsletter](https://github.com/dokterbob/django-newsletter)
* [wagtail site settings](https://vix.digital/insights/creating-using-custom-settings-in-your-wagtail-site/)
* [wagtail embed](http://docs.wagtail.io/en/v2.4/advanced_topics/embeds.html)
* Manage Cookies [django-cookie-consent](https://django-cookie-consent.readthedocs.io/en/latest/index.html)