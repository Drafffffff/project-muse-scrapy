# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import os




class MingyanItem(scrapy.Item):
    # define the fields for your item here like:
    file_p = scrapy.Field()
    file_name = scrapy.Field()
    file_urls = scrapy.Field() 
    files = scrapy.Field()
    page = scrapy.Field()
    pass
