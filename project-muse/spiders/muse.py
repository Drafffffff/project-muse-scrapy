# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request
from mingyan.items import MingyanItem
import re


class MuseSpider(scrapy.Spider):
    name = 'muse'
    max_page = 622
    page = 0
    allowed_domains = ['muse.jhu.edu']
    start_urls = [
        "https://muse.jhu.edu/search?action=browse&limit=subscription:y&limit=discipline_id:18,25&min=1&max=30"]

    def parse_content(self, response):
        item = MingyanItem()
        name = response.meta['name']
        for each in response.xpath("//*[@class='card row small-30 no_image']"):
            pdf_name = each.xpath("div/ol/li/span/a/text()").extract()[0]
            pdf_link = response.urljoin(each.xpath(
                "div/ol/li/span/div/ul/li/a/@href").extract()[0])
            item['file_p'] = name
            item['file_name'] = pdf_name
            item['file_urls'] = [pdf_link]
            item['page'] = response.meta['page']
            yield item

    def parse(self, response):
        self.page += 30
        for each in response.xpath("//*[@id='search_results']/li/div/div[2]/ul/li[1]/span/a"):
            item = MingyanItem()
            name = each.xpath("text()").extract()[0]
            url = response.urljoin(each.xpath("@href").extract()[0])
            yield Request(url=url, callback=self.parse_content, meta={'name': name,'page':self.page})
        if(self.page < self.max_page):
            next_page = "https://muse.jhu.edu/search?action=browse&limit=subscription:y&limit=discipline_id:18,25&min={}&max={}".format(
                str(self.page+1), str(self.page+30))
            yield Request(url=next_page, callback=self.parse)
