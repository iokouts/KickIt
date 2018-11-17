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
* creates a SQLite database file in the project directory
```bash
$ python manage.py createsuperuser
$ python manage.py runserver
```

## Setup
* set site name in Wagtail Admin -> Settings -> Site
* add social media accounts: Settings -> SiteSettings
* set mailchimp newsletter Subscribe Form: KickIt/templates/includes/footer.html

## TODO
### Dev
- [ ] Change PostPage Image Gallery => Image
- [ ] HomePage(slider) vs base jQuery version
- [ ] Ηamburger Μenu
- [x] ~~Change categories functionality (remove snippet, move properties to BlogIndexPage)~~
- [x] ~~Post Slider (BlogPage: Promote - show in frontpage slider)~~
- [ ] Related Posts in PostPage: show the 3 posts with the biggest number of common tags
- [x] ~~Greek Dates~~
- [x] ~~Check posts_grid.html js~~
- [x] ~~Main menu~~
- [x] ~~Post Index Pagination~~
- [ ] SEO / Share Buttons
	* adjust ~~open-graph~~ / twitter tags
	* get FB App ID
	* get tumblr account
- [x] ~~Newsletter with MailChimp~~
- [x] ~~Add Video Embed App~~
- [ ] Manage Cookies [django-cookie-consent](https://django-cookie-consent.readthedocs.io/en/latest/index.html)
- [ ] Clean Repo README

### Server
- [x] ~~Domain Name~~
- [x] ~~Connect server with domain~~ (51.15.117.113)
- [ ] Setup with dokku
- [ ] HTTPS

### Design
- [x] ~~Post Page~~
- [x] ~~footer logo = font~~
- [x] ~~Hover animations in post grid~~
- [ ] Blog Page featured posts hover animations
- [ ] Author / Author Index Pages
- [ ] Tags Index Page
- [ ] Other Main Menu Pages
- [ ] 404 / 500 error pages
- [ ] favicon
- [ ] Responsive Design
    * small desktop / tablet
    * mobile
    
## Resources
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
