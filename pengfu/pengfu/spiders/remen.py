# -*- coding: utf-8 -*-
import scrapy
from pengfu.items import PengfuItem

class RemenSpider(scrapy.Spider):
    name = 'remen'
    # allowed_domains = ['']
    start_urls = ['https://www.pengfu.com/zuijurenqi_1_1.html']

    def parse(self, response):
        list_items = response.css('.list-item')
        for item in list_items:
            penfuItem = PengfuItem()
            penfuItem['name'] = item.css('.user_name_list a::text').extract()[0]
            penfuItem['title'] = item.css('.dp-b a::text').extract()[0]
            content_img = item.css('.content-img img::attr(src)')
            penfuItem['img'] = ''
            if len(content_img) > 0:
                penfuItem['img'] = content_img.extract()[0]
            penfuItem['content'] = item.css('.content-img::text').extract()[0].strip()
            yield penfuItem
        # isNext = response.css('.page a.on::text').extract()[-1:][0].strip()
        # if isNext == '下一页':
        #     nextUrl = response.css('.page a.on::attr(href)').extract()[-1:][0]
        #     print(nextUrl)
        #     yield scrapy.Request(nextUrl,callback=self.parse)