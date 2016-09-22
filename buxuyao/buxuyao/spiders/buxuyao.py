# -*- coding: utf-8 -*-
import scrapy
from buxuyao.items import BuxuyaoItem


class BuxuyaoSpider(scrapy.Spider):
    name = "buxuyao"
    allowed_domains = ["www.buxuyao.cn"]
    start_urls = ['http://www.buxuyao.cn/picture/list_2_1.html']

    startPage = 1

    def parse(self, response):
        items = []
        for sel in response.css('.e2 li'):
            item = BuxuyaoItem()
            item['image_urls'] = []
            try:
                item['title'] = sel.css('.title::text').extract()[0]
            except Exception as e:
                item['title'] = sel.css('.title b::text').extract()[0]
            cover = sel.css('.preview img::attr(src)').extract()[0]
            if (cover.find('http') > -1):
                item['cover'] = cover
            else:
                item['cover'] = 'http://www.buxuyao.cn' + cover
            item['intro'] = sel.css('p.intro::text').extract()[0]
            item['image_urls'].append(item['cover'])
            items.append(item)
        return items
