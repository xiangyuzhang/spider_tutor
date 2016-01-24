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
    school = []
    info = {}
    def start_requests(self):       # step 1, start_url
        print "enter start_requests"
        return [Request("http://www.usquirrel.com", callback = self.find_school, dont_filter = True)]

    def find_school(self,response):         # step 2, find all the candidate school and start find the following course
        print "enter find_school"
        for school_item in response.xpath("//select/option").re("\".*\""):
            self.school.append(school_item)
            school_item = str(school_item)
            print school_item
            request = scrapy.Request(("http://www.usquirrel.com/autocomplete/course?school=" + ("+").join(school_item.split(" "))).replace("\"",""), callback = self.find_course, dont_filter = True)
            request.meta["school"] = school_item
            yield request
#        print self.school
#        request = scrapy.Request(("http://www.usquirrel.com/autocomplete/course?school=" + ("+").join(self.school[1].split(" "))).replace("\"",""), callback = self.find_course, dont_filter = True)
#        request.meta["school"] = self.school[1]

#        return [request]

    def find_course(self,response): # step 3, find all the given school's courses, and start over to send request
        print "enter find_course"
        courses = []
        school = response.meta["school"]
        courses = response.body.replace("[","").replace("]","").split(",")
        print courses
#        for course_item in courses:
#            request = scrapy.Request("http://www.usquirrel.com", callback = self.post_research, dont_filter = True)
#            request.meta["course"] = course_item
#            request.meta["school"] = school
#            yield request
        request = scrapy.Request("http://www.usquirrel.com", callback = self.post_research, dont_filter = True)
        request.meta["course"] = courses[0]
        request.meta["school"] = school
        return [request]
    #FormRequeset
    def post_research(self, response): # step 4, based on the request, open course info
        print "post_research"

        school = response.meta["school"].replace("\"","")
        course = response.meta["course"].replace("\"","")
        print "This is school:", school
        print "this is course:", course
        yield scrapy.FormRequest.from_response(response,
                            formdata = {
                            'university': school,
                            'course': course
                            },
                            callback = self.after_login
                            )
    def after_login(self,response): # final step, start to derive course info
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
        self.get_course_name(response,item)
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

    def get_course_name(self,response,item):
        name = str((". ").join(response.xpath("//h3/span").re(">.*<"))).replace("<","").replace(">","")
        item["course_name"] = name
#        print " this is the course name", name


