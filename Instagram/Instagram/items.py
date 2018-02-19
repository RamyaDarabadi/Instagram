# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


from scrapy.item import Item, Field

class InstagramItem(Item):
    fullname=Field()
    username=Field()
    title=Field()
    propicurl=Field()
    logging_page_id=Field()
    mutual_followers = Field()
    biography = Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
