import pdb

import scrapy
from scrapy.selector import Selector


class Spider_CIKM20(scrapy.Spider):
    name = "cikm20"
    start_urls = [
        'https://www.cikm2020.org/accepted-papers/accepted-research-papers/',
    ]

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath('//table/tbody/tr[1]/following::tr/td[1]/text()'):
            yield {
                'title': article.extract().strip(),
                'year': '2020',
                'conf': 'CIKM',
                'conf_long': 'INTERNATIONAL CONFERENCE ON INFORMATION AND KNOWLEDGE MANAGEMENT'
            }