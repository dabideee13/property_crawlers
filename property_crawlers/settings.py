BOT_NAME = 'property_crawlers'

SPIDER_MODULES = ['property_crawlers.spiders']
NEWSPIDER_MODULE = 'property_crawlers.spiders'

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 32

DOWNLOAD_DELAY = 3
RANDOMIZE_DOWNLOAD_DELAY = True

COOKIES_ENABLED = False

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 3
AUTOTHROTTLE_MAX_DELAY = 60

HTTPCACHE_ENABLED = True

AUTOTHROTTLE_ENABLED = True

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}

DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter'
