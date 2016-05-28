# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import FormRequest

class DoubanSpider(Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://www.douban.com/accounts/login?source=book']
    headers = {
                'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
                'Accept-Encoding':'gzip, deflate',
                'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'Connection':'keep-alive'
            }
    form_data = {'form_email': '15680738065', 'form_password': 'yu19951201'}

    def start_requests(self):
        return [FormRequest('https://www.douban.com/accounts/login',
                            formdata = self.form_data,
                            meta = {'cookiejar':1},
                            headers = self.headers,
                            callback = self.post_login
                          )]

    def post_login(self, response):
        print 'Preparing login'
        return [FormRequest.from_response(response,
                            meta = {'cookiejar':response.meta['cookiejar']},
                            headers = self.headers,
                            formdata = self.form_data,
                            callback = self.after_login,
                            dont_filter = True)]

    def after_login(self, response):
        print 'After login'
        print response.body
