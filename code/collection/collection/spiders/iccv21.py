import pdb

import scrapy
from scrapy.selector import Selector

import json


class Spider_ICCV19(scrapy.Spider):
    name = "iccv21"
    start_urls = ['https://openaccess.thecvf.com/ICCV2021?day=all']

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath("//*[contains(@class, 'ptitle')]/a/text()"):
            yield {
                'title': article.extract().strip(),
                'year': '2021',
                'conf': 'ICCV',
                'conf_long': 'International Conference on Computer Vision'
            }