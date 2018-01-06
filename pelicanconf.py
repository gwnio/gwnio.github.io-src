#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site information
AUTHOR = 'Rg'
SITENAME = '@gwnio'
DOMAIN = 'localhost:8000'
SITEURL = 'http://' + DOMAIN
SITE_DESCRIPTION = 'Just documenting some things as I encounter'

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

# Social
TWITTER_USERNAME = ''
GITHUD_ID = 'gwnio'

SOCIAL = {'Twitter': 'https://twitter.com/' + TWITTER_USERNAME,
          'Github': 'https://github.com/' + GITHUD_ID,
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
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'
ARTICLE_URL = 'blog/{date:%Y}/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{slug}.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
ARCHIVES_URL = 'archives/'
ARCHIVES_SAVE_AS = 'archives/index.html'

TAGS_TO_EXCLUDE = {'christian'}

DISQUS_SITENAME = ''
GOOGLE_ANALYTICS = ''

PLUGIN_PATHS = ["plugins", "../../../../../tools/Python36/Lib/site-packages"]
PLUGINS = ["summary", "pelican_gist"]

OUTPUT_PATH = 'output/local'