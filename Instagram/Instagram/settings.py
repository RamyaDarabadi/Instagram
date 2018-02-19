# -*- coding: utf-8 -*-

# Scrapy settings for Instagram project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'Instagram'

SPIDER_MODULES = ['Instagram.spiders']
NEWSPIDER_MODULE = 'Instagram.spiders'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
DOWNLOAD_DELAY = 1
ITEM_PIPELINES = {
        'Instagram.pipelines.InstagramPipeline': 300,
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Instagram (+http://www.yourdomain.com)'
