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
* set mailchimp newsletter Subscribe Form: KickIt/templates/includes/footer.html

## TODO
### Dev
- [ ] Change PostPage Image Gallery => Image
- [ ] Related Posts in PostPage: show the 3 posts with the biggest number of common tags
- [x] ~~Newsletter with MailChimp~~
- [ ] Manage Cookies [django-cookie-consent](https://django-cookie-consent.readthedocs.io/en/latest/index.html)
- [ ] minify css (?)
- [ ] SEO
- [ ] check browser/mobile compatibility
- [ ] consider removing wagtail-embedvideos and using default [wagtail embed](http://docs.wagtail.io/en/v2.4/advanced_topics/embeds.html) 

### Server
- [x] ~~Update~~

### Design
- [ ] Author / Author Index Pages
- [ ] Podcast Page
- [ ] 404 / 500 error pages
- [ ] favicon

    
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

### Django / Wagtail
* [wagtailmenus](https://github.com/rkhleics/wagtailmenus)
* [wagtail metadata](https://github.com/takeflight/wagtail-metadata)
* [wagtail embed videos](https://github.com/infoportugal/wagtail-embedvideos)
* Pagination
	* [django-el-pagination](https://django-el-pagination.readthedocs.io/en/latest/)
	* [reddit help](https://www.reddit.com/r/django/comments/9p70uf/adding_load_more_functionality_to_wagtail_via/)
* [django-newsletter](https://github.com/dokterbob/django-newsletter)
* [wagtail site settings](https://vix.digital/insights/creating-using-custom-settings-in-your-wagtail-site/)
