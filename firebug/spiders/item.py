__author__ = 'parallels'
import scrapy


class item(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()

    # here, the field is kind like a object's various properties. Its format is exactly same with the DICT api.
    # So here, we declare the property name, url, description respectively
    # if we want to translate the code above into existing python code, it will be like:
class item:
    def __init__(self,name,url,description):
        self.name = name
        self.url = url
        self.description = description
# the following is the way to declare a new object
object = item(name = "descktop", url = "1000",)
# the following is the way to visit its property
item["name"] # equal to item.name
item.get('name') # equal to item.name

