# KickIt!

music blog 

## Built With

* [Wagtail](https://wagtail.io) - the powerfull CMS for modern websites
	* [Wagtail Docs](http://docs.wagtail.io/en/latest/index.html)

## Installation (probably)
* pull
* use venv with python 3.6
```bash
$ pip install -r requirements.txt
$ python manage.py migrate
```
* if that fails, try:
```bash
$ pip install -r pip-freeze-requirements.txt
$ python manage.py migrate
```


* creates a SQLite database file in the project directory
```bash
$ python manage.py createsuperuser
$ python manage.py runserver
```

## TODO
### Dev
- [ ] Change PostPage Image Gallery => Image
- [ ] Post Slider (BlogPage: Promote - show in frontpage slider)
- [ ] Related Posts in PostPage

- [ ] Main menu [wagtailmenus](https://github.com/rkhleics/wagtailmenus)
- [ ] Post Index Pagination [demo](https://simpleisbetterthancomplex.com/tutorial/2017/03/13/how-to-create-infinite-scroll-with-django.html)
- [ ] SEO / Share Buttons (BlogPage)
	* [~~wagtail-metadata~~](https://github.com/takeflight/wagtail-metadata) (done!)
	* adjust open-graph / twitter tags
	* [twitter cards](https://developer.twitter.com/en/docs/tweets/optimize-with-cards/overview/abouts-cards) / [twitter button guides](https://developer.twitter.com/en/docs/twitter-for-websites/tweet-button/overview.html)
	* [Facebook Share Dialog](https://developers.facebook.com/docs/sharing/reference/share-dialog) / [~~facebook share button~~](https://developers.facebook.com/docs/plugins/share-button/#)
	* [tumblr buttons](https://www.tumblr.com/buttons)
- [ ] Newsletter 
	* [django-newsletter](https://github.com/dokterbob/django-newsletter)
- [x] ~~Add Video Embed App~~ [wagtail-embedvideos](https://github.com/infoportugal/wagtail-embedvideos)
- [ ] Manage Cookies [django-cookie-consent](https://django-cookie-consent.readthedocs.io/en/latest/index.html)

### Server
- [ ] Domain Name
- [ ] Setup with dokku
- [ ] HTTPS

### Design
- [x] ~~Post Page~~
- [ ] Author / Author Index Pages
- [ ] Hover animations in post grid
- [ ] Tags Index Page
- [ ] Other Main Menu Pages
- [ ] 404 / 500 error pages
