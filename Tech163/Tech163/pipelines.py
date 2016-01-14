# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html



from store.py import 


class Tech163Pipeline(object):
    def process_item(self, item, spider):
        if spider.name != "news":  return item
        if item.get("news_thread", None) is None: return item

        spec = { "news_thread": item["news_thread"] }
        .news.update(spec, {'$set': dict(item)}, upsert=True)
        return None