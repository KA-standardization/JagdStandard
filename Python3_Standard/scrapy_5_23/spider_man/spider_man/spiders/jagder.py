import scrapy

"""
    name: 是 Scrapy 定位（和实例化）蜘蛛的方式
    allowed_domains: OffsiteMiddleware如果启用，则不会遵循对不属于此列表中指定的域名（或其子域）的 URL 的请求
                     scrapy.spidermiddlewares.offsite.OffsiteMiddleware
    start_urls: 
    

"""

"""
# CrawlSpider
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('item\.php', )), callback='parse_item'),
    )

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = scrapy.Item()
        item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        item['name'] = response.xpath('//td[@id="item_name"]/text()').get()
        item['description'] = response.xpath('//td[@id="item_description"]/text()').get()
        item['link_text'] = response.meta['link_text']
        url = response.xpath('//td[@id="additional_data"]/@href').get()
        return response.follow(url, self.parse_additional_page, cb_kwargs=dict(item=item))

    def parse_additional_page(self, response, item):
        item['additional_data'] = response.xpath('//p[@id="additional_data"]/text()').get()
        return item
"""

"""
# 允许自定义 cookie 的domain和path 属性。这仅在保存 cookie 以供以后请求时才有用
request_with_cookies = Request(url="http://www.example.com",
                               cookies=[{'name': 'currency',
                                        'value': 'USD',
                                        'domain': 'example.com',
                                        'path': '/currency'}])
                                        
# 当某些站点返回 cookie（在响应中）时，这些 cookie 将存储在该域的 cookie 中，并将在以后的请求中再次发送。这是任何常规网络浏览器的典型行为。
# 要创建一个不发送存储的 cookie 并且不存储接收到的 cookie 的请求，请将dont_merge_cookies密钥设置为True in request.meta。
# 发送手动定义的 cookie 并忽略 cookie 存储的请求示例：
Request(
    url="http://www.example.com",
    cookies={'currency': 'USD', 'country': 'UY'},
    meta={'dont_merge_cookies': True},
)                                                                             
"""

"""
import scrapy

from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

class ErrbackSpider(scrapy.Spider):
    name = "errback_example"
    start_urls = [
        "http://www.httpbin.org/",              # HTTP 200 expected
        "http://www.httpbin.org/status/404",    # Not found error
        "http://www.httpbin.org/status/500",    # server issue
        "http://www.httpbin.org:12345/",        # non-responding host, timeout expected
        "https://example.invalid/",             # DNS error expected
    ]

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u, callback=self.parse_httpbin,
                                    errback=self.errback_httpbin,
                                    dont_filter=True)

    def parse_httpbin(self, response):
        self.logger.info('Got successful response from {}'.format(response.url))
        # do something useful here...

    def errback_httpbin(self, failure):
        # log all failures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)
"""


class JagdSpider(scrapy.Spider):
    name = "jagd"

    #  必须返回一个可迭代的 Requests（你可以返回一个请求列表或编写一个生成器函数），Spider 将从中开始爬取。后续请求将从这些初始请求中依次生成
    """
        # start_requests 方法的快捷方式
        # 只需定义一个start_urls带有 URL 列表的类属性。然后，默认实现将使用此列表start_requests()为您的蜘蛛创建初始请求
        start_urls = [
            "https://www.baidu.com/s?wd=%E6%9F%AF%E8%BE%BE%E4%BC%8A",
            "https://www.baidu.com/s?wd=%E5%A5%A5%E8%8A%AC%E5%B7%B4%E8%B5%AB"
    ]
    """

    def start_requests(self):
        urls = [
            "https://www.baidu.com/s?wd=%E6%9F%AF%E8%BE%BE%E4%BC%8A",
            "https://www.baidu.com/s?wd=%E5%A5%A5%E8%8A%AC%E5%B7%B4%E8%B5%AB"
        ]
        for u in urls:
            """
                # DUPEFILTER_CLASS: dont_filter=False
                    默认 ( RFPDupeFilter) 基于使用该scrapy.utils.request.request_fingerprint函数的请求指纹进行过滤。为了更改检查重复项的方式，
                    您可以子类化RFPDupeFilter并覆盖其request_fingerprint方法。此方法应接受 scrapyRequest对象并返回其指纹（字符串）。
            """
            yield scrapy.Request(url=u, method='GET', callback=self.parse, dont_filter=False)

    # 将被调用以处理为每个请求下载的响应的方法。response 参数是一个实例
    def parse(self, response, **kwargs):
        for item in response.css('title::text').getall():
            yield {
                'title': item
            }

        png_url = response.css('noscript a::attr(href)').get()
        if png_url is not None:
            # scrapy.Request 不同，response.follow直接支持相对 URL - 无需调用 urljoin。注意response.follow只返回一个 Request 实例；您仍然必须提交此请求
            yield response.follow(png_url, callback=self.parse)
            """
            # 您还可以将选择器传递给response.follow而不是字符串；这个选择器应该提取必要的属性
            for href in response.css('ul.pager a::attr(href)'):
                yield response.follow(href, callback=self.parse)
            """

            """
            # 要从一个可迭代对象创建多个请求，您可以 response.follow_all改用
            css_ = response.css('noscript a')
            yield from response.follow_all(css_, callback=self.parse)
            # 进一步缩短
            yield from response.follow_all(css='noscript a', callback=self.parse)
            """

            """
            def parse(self, response):
                request = scrapy.Request('http://www.example.com/index.html',
                                         callback=self.parse_page2,
                                         cb_kwargs=dict(main_url=response.url))
                request.cb_kwargs['foo'] = 'bar'  # add more arguments for the callback
                yield request

            def parse_page2(self, response, main_url, foo):
                yield dict(
                    main_url=main_url,
                    other_url=response.url,
                    foo=foo,
                )
            """
