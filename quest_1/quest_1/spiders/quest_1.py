

__author__ = 'parallels'
import scrapy
import scrapy.log
from bs4 import BeautifulSoup
from scrapy.http import Request
from items import Item
from scrapy.selector import Selector
import re

class heibanke1(scrapy.Spider):
    name = "heibanke1"
#   allowd_domains = ["http://www.heibanke.com"]
#    allowed_domains = ["dmoz.org"]
    start_urls = ["http://www.heibanke.com/lesson/crawler_ex00/"]



    def parse(self, response):

        key = response.xpath("//html/body/div/div/div/h3").re(r'([0-9]+)')[1]
        if(len(key) >= 2):
            print "find new url, continuing..."
            new_url = "http://www.heibanke.com/lesson/crawler_ex00/" + key
            with open("key","a") as f:
                f.write(key)
            yield Request(url = new_url, callback=self.parse)
        else:
            print "new mission found!!!Good Job!!!\nNew Url has been save in 'New Mission'"
            new_mission = response.xpath("//div/a").re("\"/.*/\"")[-1]
            print new_mission
            with open("new Mission",'a') as f:
                f.write(new_mission)
#        with open("body", 'wb') as f:
#            f.write(response.body)

