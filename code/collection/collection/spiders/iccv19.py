import pdb

import scrapy
from scrapy.selector import Selector

import json


class Spider_ICCV19(scrapy.Spider):
    name = "iccv19"
    start_urls = [
        'https://openaccess.thecvf.com/ICCV2019.py?day=2019-10-29',
        'https://openaccess.thecvf.com/ICCV2019.py?day=2019-10-30',
        'https://openaccess.thecvf.com/ICCV2019.py?day=2019-10-31',
        'https://openaccess.thecvf.com/ICCV2019.py?day=2019-11-01'
    ]

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath("//dt[contains(@class, 'ptitle')]//a/text()"):
            yield {
                'title': article.extract().strip(),
                'year': '2019',
                'conf': 'ICCV',
                'conf_long': 'International Conference on Computer Vision'
            }