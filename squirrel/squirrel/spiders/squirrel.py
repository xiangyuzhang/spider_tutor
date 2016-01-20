__author__ = 'parallels'
__author__ = 'parallels'
import scrapy
from scrapy import Request
from bs4 import BeautifulSoup
from items import Item
from scrapy.selector import Selector
import re
class squirrel(scrapy.Spider):
    name = "squirrel"
#     start_urls = ["http://www.heibanke.com/lesson/crawler_ex01/"]


    def start_requests(self):
        return [Request("http://www.usquirrel.com", callback = self.post_research,dont_filter = True)]

    #FormRequeset
    def post_research(self, response):
        print "start research"

        return [scrapy.FormRequest.from_response(response,
                            formdata = {
                            'university': "University of Massachusetts Amherst",
                            'course': 'College Writing - ENGLWRIT 112'
                            },
                            callback = self.after_login
                            )]
    def after_login(self,response):
        print "after_login"
#        soup = BeautifulSoup(response.body, 'lxml')
#        print soup.find_all('p')
        item = Item()
        self.get_in_state(response,item)
        self.get_out_state(response,item)
        self.get_course_description(response,item)
        self.get_schedule_time(response,item)
        self.get_schedule_from(response,item)
        self.get_schedule_type(response,item)
        self.get_course_site(response,item)
        return item

    def get_course_site(self, response, item):
        site = response.xpath("//div/h5/span")[0].extract().replace("<span>","").replace("</span>","")
        item['course_site'] = site

    def get_in_state(self, response, item):
        in_state = response.xpath("//p")[0].re('[0-9]+')
        item['in_state_price'] = in_state

    def get_out_state(self, response, item):
        out_state = response.xpath("//p")[1].re('[0-9]+')
        item['out_state_price'] = out_state

    def get_course_description(self,response, item):
        decription = response.xpath("//div/p")[2].extract().replace("<p>","").replace("</p>","")
        item['Course_description'] = decription

    def get_schedule_time(self,response,item):
        time = response.xpath("//div/p")[3].extract().replace("<p>","").replace("</p>","")
        item['Course_schedule_time'] = time

    def get_schedule_from(self,response,item):
        fromm = response.xpath("//div/p")[4].extract().replace("<p>","").replace("</p>","")
        item['Course_schedule_from'] = fromm

    def get_schedule_type(self,response,item):
        type = response.xpath("//div/p")[5].extract().replace("<p>","").replace("</p>","").replace("Class Type:","")
        item['Course_schedule_type'] = type
