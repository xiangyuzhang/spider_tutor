# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    in_state_price = scrapy.Field()
    out_state_price = scrapy.Field()
    course_name = scrapy.Field()
    course_site = scrapy.Field()
    Course_description = scrapy.Field()
    Course_schedule_time = scrapy.Field()
    Course_schedule_from = scrapy.Field()
    Course_schedule_type = scrapy.Field()

    pass
