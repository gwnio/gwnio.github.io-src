#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site information
AUTHOR = 'Rg'
SITENAME = '@gwnio'
SITEURL = 'http://localhost:8000'
SITEURL = ''
SITE_DESCRIPTION = 'Notes, learnings and other miscellaneous things'

PATH = 'content'
STATIC_PATHS = ['images', 'pdfs', 'extra']
EXTRA_PATH_METADATA = {'extra/robots.txt': {'path': 'robots.txt'}}

# Localization issues
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

DEFAULT_DATE_FORMAT = '%b %d, %Y'

# Theme
THEME = 'themes/w3css-blog'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

TWITTER_USERNAME = ''
GITHUD_ID = ''

# Social widget
# 'Twitter': 'https://twitter.com/' + TWITTER_USERNAME,
SOCIAL = {'Twitter': '',
          'Github':'https://github.com/' + GITHUD_ID,
          'LinkedIn':'',
          'Facebook':'',
          'Instagram':'',
          'Snapchat':'',
          'Pinterest':'',
          'Email': ''}

DEFAULT_PAGINATION = False

# Category Settings
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'blog'

# Output
OUTPUT_SOURCES = True
OUTPUT_SOURCES_EXTENSION = ".txt"

# URL configuration
ARTICLE_URL = '{date:%Y}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'
TAG_URL = '{slug}/'
TAG_SAVE_AS = '{slug}/index.html'
ARCHIVES_URL = 'archives/'
ARCHIVES_SAVE_AS = 'archives/index.html'

DISQUS_SITENAME = ''
GOOGLE_ANALYTICS = ''

PLUGIN_PATHS = ["plugins", "../../../../../tools/Python36/Lib/site-packages"]
PLUGINS = ["summary", "pelican_gist"]

OUTPUT_PATH = 'output/local'