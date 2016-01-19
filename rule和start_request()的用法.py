class scrapy.spider.Rule(link_extractor, callback = None, cb_kwargs = None, follow = None, process_links = None, process_request = None)
	!!!是一个格式，不是一个function
	1， link_extractor: 是一个Link Extractor对象，定义如何从爬过的网页上面提取links
	2， callback：是一个callable function或者是一个 string（这个string是一个funciton的名称），这个function用于处理每一个由link_extractor提取到的link
		这个callback function的第一个输入必须是response，然后必须返回一个list，包含Item更或者Request对象
		注意：这个callback function必须不能被命名为parse，不然会重写
	3，	cb_kwargs：是一个dict，包含keyword argument用于传入callback function
	4，	follow：是一个布尔值。指定了这个rule从response里面取出来的连接是否需要继续跟进，如果callback function是none，那么默认为true，否则则默认为false
	5，	process_links: 是一个callable或者string（是一个函数的名字）。从link_extractor中获取的连接列表会经过这个方法被过滤
	6，	process_request: 是一个callable或者string（是一个函数的名字）。这个Rule提取到的每一个request都会用这个函数进行过滤 

start_requests()
该方法必须返回一个可迭代对象(iterable)。该对象包含了spider用于爬取的第一个Request。

当spider启动爬取并且未制定URL时，该方法被调用。 当指定了URL时，make_requests_from_url() 将被调用来创建Request对象。 该方法仅仅会被Scrapy调用一次，因此您可以将其实现为生成器。

该方法的默认实现是使用 start_urls 的url生成Request。

如果您想要修改最初爬取某个网站的Request对象，您可以重写(override)该方法。 例如，如果您需要在启动时以POST登录某个网站，你可以这么写:

def start_requests(self):
    return [scrapy.FormRequest("http://www.example.com/login",
                               formdata={'user': 'john', 'pass': 'secret'},
                               callback=self.logged_in)]

def logged_in(self, response):
    # here you would extract links to follow and return Requests for
    # each of them, with another callback
    pass