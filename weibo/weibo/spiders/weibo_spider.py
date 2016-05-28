# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request
from weibo.items import WeiboItem

class WeiboSpider(Spider):
    name = 'weibo'
    allowed_domains = ["weibo.cn"]
    start_urls = ["http://weibo.cn/u/1663819761"]
    cookies = {
    "_T_WM": "10fcc47835e41a2f63a48e03dc3a7c31", \
    "gsid_CTandWM": "4u1n12451BViShpTXeUqagcS3fj",\
    "SUB": "_2A256Q4tsDeRxGeVG7VAW8inFzzWIHXVZzxUkrDV6PUJbstBeLUL4kW1LHesx8bY-qJWWcfVZepuhpO-sGvmUDQ..", \
    "SUBP": "0033WrSXqPxfM725Ws9jqgMF55529P9D9WhrrUVLwwMQXRv7_7WBhIHp5JpX5o2p5NHD95Q01hqES0zN1KB4Ws4Dqcjki--4iKLFi-zci--Xi-i2iK.4i--RiKn7iKnfeK.4SBtt", \
    "SUHB": "00xpepkBjjbYsy", "SSOLoginState": "1464335164"
            }
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, cookies=self.cookies, callback=self.parse_weibo)

    def parse_weibo(self, response):
        item = WeiboItem()
        print response.xpath('/html/head/title/text()').extract()[0]
        for p in response.xpath('//div[contains(@id,"M")]'):
            item['content'] =  p.xpath('./div/span/text()').extract()
            yield item
        yield Request("http://weibo.cn" + response.xpath('//*[@id="pagelist"]/form/div/a/@href').extract()[0], cookies=self.cookies, callback=self.parse_weibo)
