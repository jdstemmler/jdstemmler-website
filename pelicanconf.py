#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Jayson Stemmler'
SITENAME = u'Jayson Stemmler'
SITEURL = '/'

THEME_DIR = os.path.join(os.getenv("HOME"), 'Documents/Blogging/pelican-themes')
THEME = os.path.join(THEME_DIR, 'Flex')

USE_FOLDER_AS_CATEGORY = True

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{slug}'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{slug}.html'

PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}.html'

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

## THEME OPTIONS

MAIN_MENU = True
SITELOGO = '/images/profile.jpg'

SOCIAL = (('linkedin', 'https://linkedin.com/in/jdstemmler/en'),
          ('github', 'https://github.com/jdstemmler'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'
