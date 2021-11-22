import pdb

import scrapy
from scrapy.selector import Selector


class Spider_CIKM20(scrapy.Spider):
    name = "cikm21"
    start_urls = [
        'https://www.cikm2021.org/accepted-papers',
    ]

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath('//li/b/text()'):
            yield {
                'title': article.extract().strip(),
                'year': '2021',
                'conf': 'CIKM',
                'conf_long': 'INTERNATIONAL CONFERENCE ON INFORMATION AND KNOWLEDGE MANAGEMENT'
            }