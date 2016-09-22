# -*- coding: utf-8 -*-
import scrapy
from buxuyao.items import BuxuyaoItem


class BuxuyaoSpider(scrapy.Spider):
    name = "buxuyao"
    allowed_domains = ["www.buxuyao.cn"]
    start_urls = [
        'http://www.buxuyao.cn/picture/list_2_1.html',
        'http://www.buxuyao.cn/picture/list_2_2.html',
        'http://www.buxuyao.cn/picture/list_2_3.html',
        'http://www.buxuyao.cn/picture/list_2_4.html',
        'http://www.buxuyao.cn/picture/list_2_5.html',
        'http://www.buxuyao.cn/picture/list_2_6.html',
        'http://www.buxuyao.cn/picture/list_2_7.html',
        'http://www.buxuyao.cn/picture/list_2_8.html',
        'http://www.buxuyao.cn/picture/list_2_9.html',
        'http://www.buxuyao.cn/picture/list_2_10.html',
        'http://www.buxuyao.cn/picture/list_2_11.html',
        'http://www.buxuyao.cn/picture/list_2_12.html',
        'http://www.buxuyao.cn/picture/list_2_13.html',
        'http://www.buxuyao.cn/picture/list_2_14.html',
        'http://www.buxuyao.cn/picture/list_2_15.html',
        'http://www.buxuyao.cn/picture/list_2_16.html',
        'http://www.buxuyao.cn/picture/list_2_17.html',
        'http://www.buxuyao.cn/picture/list_2_18.html',
        'http://www.buxuyao.cn/picture/list_2_19.html',
        'http://www.buxuyao.cn/picture/list_2_20.html',
        'http://www.buxuyao.cn/picture/list_2_21.html',
        'http://www.buxuyao.cn/picture/list_2_22.html',
        'http://www.buxuyao.cn/picture/list_2_23.html',
        'http://www.buxuyao.cn/picture/list_2_24.html',
        'http://www.buxuyao.cn/picture/list_2_25.html',
        'http://www.buxuyao.cn/picture/list_2_26.html',
        'http://www.buxuyao.cn/picture/list_2_27.html',
        'http://www.buxuyao.cn/picture/list_2_28.html',
        'http://www.buxuyao.cn/picture/list_2_29.html',
        'http://www.buxuyao.cn/picture/list_2_30.html',
        'http://www.buxuyao.cn/picture/list_2_31.html',
        'http://www.buxuyao.cn/picture/list_2_32.html',
        'http://www.buxuyao.cn/picture/list_2_33.html',
        'http://www.buxuyao.cn/picture/list_2_34.html',
        'http://www.buxuyao.cn/picture/list_2_35.html',
        'http://www.buxuyao.cn/picture/list_2_36.html',
        'http://www.buxuyao.cn/picture/list_2_37.html',
        'http://www.buxuyao.cn/picture/list_2_38.html',
        'http://www.buxuyao.cn/picture/list_2_39.html'
    ]
    items = []
    def parse(self, response):
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
            self.items.append(item)
        return self.items
