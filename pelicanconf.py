#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'abodewithin'
SITENAME = 'abodewithin.com'
SITEURL = 'http://abodewithin.com'
SITETITLE = 'abodewithin'
SITELOGO = 'tales-logo.png'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'English'
THEME = './themes/tales'
PATH = 'content'
STATIC_PATHS = ['images',  'pages', 'extra/robots.txt', 'extra/favicon.ico',]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

MAIN_STYLESHEET = 'styles-bluegreen.css'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 4
SIDEBARMAIN = "sidebar_main.html"
SIDEBAR_ARTICLE = "sidebar_article.html"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
LOAD_CONTENT_CACHE = False
DISPLAY_PAGES_ON_MENU = False

# plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['autostatic', 'advthumbnailer',]

# image
# IMG_EXT = ('jpg','png','gif','tiff')
