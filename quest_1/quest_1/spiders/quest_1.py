

__author__ = 'parallels'
import scrapy
import scrapy.log
from bs4 import BeautifulSoup
import scrapy.log
from items import Item
from scrapy.selector import Selector
import re

class heibanke1(scrapy.Spider):
    name = "heibanke1"
#   allowd_domains = ["http://www.heibanke.com"]
#    allowed_domains = ["dmoz.org"]
    start_urls = ["http://www.heibanke.com/lesson/crawler_ex00/"]
    scrapy.log.msg("here we enter the class")


    def parse(self, response):

        scrapy.log.msg("enter parse")

        key = response.xpath("//html/body/div/div/div/h3").re(r'([0-9]+)')[1]
#         print key

        with open("key","wb") as f:
            f.write(key)
        return {"key":key}
#        with open("body", 'wb') as f:
#            f.write(response.body)

