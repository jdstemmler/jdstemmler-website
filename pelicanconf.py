#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import datetime

AUTHOR = u'Jayson Stemmler'
SITENAME = u'Jayson Stemmler'
SITEURL = ''
SITENAME = "Jayson Stemmler's Blog"
SITETITLE = 'Jayson Stemmler'
SITESUBTITLE = 'Research / Data Scientist'
SITEDESCRIPTION = ''
# SITELOGO = SITEURL + '/images/profile.png'
# FAVICON = SITEURL + '/images/favicon.ico'

COPYRIGHT_NAME = "Jayson Stemmler"
COPYRIGHT_YEAR = datetime.datetime.today().strftime('%Y')

# THEME_DIR = os.path.join(os.getenv("HOME"), 'Documents/Blogging/pelican-themes')
# THEME = os.path.join(THEME_DIR, 'Flex')

THEME = 'themes/Flex'

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
SITELOGO = '/images/profile.png'

LINKS = (('Resume', 'https://represent.io/jdstemmler'),)

SOCIAL = (('linkedin', 'https://linkedin.com/in/jdstemmler/en'),
          ('github', 'https://github.com/jdstemmler'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

BROWSER_COLOR = '#333333'
ROBOTS = 'index, follow'
