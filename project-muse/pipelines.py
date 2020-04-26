# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import FilesPipeline
from scrapy import Request
import unicodedata
import os
import re
import logging


def validate(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|\s]"
    new_title = re.sub(rstr, "_", title)
    new_title = re.sub('[\r\n\t]', '', new_title)
    return new_title


class MingyanPipeline(FilesPipeline):

    def get_media_requests(self, item, info):
        logging.log(logging.INFO, "page{}".format(str(item.get('page'))))
        return [Request(x, meta={'filename': item.get('file_name'), 'path': item.get('file_p')}) for x in item.get(self.files_urls_field, [])]

    def file_path(self, request, response=None, info=None):
        path = validate(request.meta['path'])
        name = validate(request.meta['filename'])
        return 'pdf/%s/%s%s' % (path, name, ".pdf")

