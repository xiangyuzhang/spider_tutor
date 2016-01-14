__author__ = 'parallels'


from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from item import item
class GoogleDirectorySpider(CrawlSpider):
    name = 'directory.google.com'
    allowed_domains = ['directory.google.com']
    start_urls = ['http://directory.google.com/']

    rules = (
        Rule(LinkExtractor(allow='directory\.google\.com/[A-Z][a-zA-Z_/]+$'),
            'parse_category', follow=True,
        ),
    )

    
    def parse_category(self, response):

        # The path to website links in directory page
        links = response.xpath('//td[descendant::a[contains(@href, "#pagerank")]]/following-sibling::td/font')

        for link in links:
            item = item()
            item['name'] = link.xpath('a/text()').extract()
            item['url'] = link.xpath('a/@href').extract()
            item['description'] = link.xpath('font[2]/text()').extract()
            yield item