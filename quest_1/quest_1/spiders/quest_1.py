__author__ = 'parallels'
import scrapy
import scrapy.log


class heibanke1(scrapy.Spider):
    name = "heibanke1"
#   allowd_domains = ["http://www.heibanke.com"]
#    allowed_domains = ["dmoz.org"]
    start_urls = ["http://www.heibanke.com/lesson/crawler_ex00/"]
    scrapy.log.msg("here we enter the class")

    def parse(self, response):

        with open("body", 'wb') as f:
            f.write(response.body)
