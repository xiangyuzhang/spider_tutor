__author__ = 'parallels'
import scrapy
from scrapy import Request
from bs4 import BeautifulSoup

def start_requests(usrname, password):
    return Request(url="http://www.heibanke.com/lesson/crawler_ex01/",
                   cookies={'name':usrname, 'password':password},dont_filter = True)


class heibanke2(scrapy.Spider):
    name = "herbanke2"
#     start_urls = ["http://www.heibanke.com/lesson/crawler_ex01/"]
    password = 0

    def start_requests(self):
        return [Request("http://www.heibanke.com/lesson/crawler_ex01/", callback = self.post_login,dont_filter = True)]

    #FormRequeset
    def post_login(self, response):
        print 'Preparing login'

        return [scrapy.FormRequest.from_response(response,
                            formdata = {
                            'usrname': 'Joselyn',
                            'password': str(self.password)
                            },
                            callback = self.after_login
                            )]
    def after_login(self,response):
        print "after_login"
        self.start_requests()
#        soup = BeautifulSoup(response.body,"lxml")
#        with open("body","wb") as f:
#            f.write(response.body)
#        if "Joselyn" not in soup.h3.string:
#            self.password+=1
#            self.start_requests()

#        else:
#            print "Key is", str(self.password)
#            print "Succeed!!!"