# -*- coding: utf-8 -*-
import scrapy
import re
from tutorial.items import DangdangItem

class DangDangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ["dangdang.com"]
    start_urls = ["http://bang.dangdang.com/books/newhotsales/01.05.00.00.00.00-recent7-0-0-1-1"]

    def parse(self, response):
        for href in response.xpath('//*[@class="bang_list clearfix bang_list_mode"]/li/div[@class="pic"]/a'):
            url = response.urljoin(href.xpath('@href').extract()[0])
            print url
            yield scrapy.Request(url, callback=self.parse_dangdang_new_top10)

    def parse_dangdang_new_top10(self, response):
        #item = DangdangItem()
        #item['name'] = response.xpath('//*[@id="main_bd"]/div[3]/div[2]/div/div[1]/div[1]/h1/@title').extract()[0]
        #item['ISBN'] = response.xpath('//*[@id="detail_describe"]/ul/li[10]/text()').extract()[0]
        #item['desc'] = response.xpath('//*[@id="content"]/div[2]/textarea/text()').extract()[0]
        name =  response.xpath('//*[@id="main_bd"]/div[3]/div[2]/div/div[1]/div[1]/h1/@title').extract()[0]
        isbn = response.xpath('//*[@id="detail_describe"]/ul/li[10]/text()').extract()[0]
        desc =  response.xpath('//*[@id="content"]/div[2]/textarea/text()').extract()[0]
        ISBN = re.findall(r'[0-9]{13}', isbn)[0]
        print name
        print ISBN
        print desc
        #yield item
