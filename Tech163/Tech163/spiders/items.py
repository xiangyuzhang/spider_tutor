# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class Tech163Item(scrapy.Item):
        # define the fields for your item here like:
        # name = scrapy.Field()
        news_thread=scrapy.Field()      # define news id
        news_title = scrapy.Field()     # define title
        news_url = scrapy.Field()       # define url
        news_time=scrapy.Field()        # define time
        news_from=scrapy.Field()        # define from
        from_url=scrapy.Field()         # define from_url
        news_body=scrapy.Field()        # define body