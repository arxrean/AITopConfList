import pdb

import scrapy
from scrapy.selector import Selector


class Spider_CIKM19(scrapy.Spider):
    name = "cikm19"
    start_urls = [
        'https://dblp.org/db/conf/cikm/cikm2019.html',
    ]

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath("//ul[contains(@class, 'publ-list')][3 <= position() and position() < 62]//span[contains(@class, 'title')]/text()"):
            yield {
                'title': article.extract().strip(),
                'year': '2019',
                'conf': 'CIKM',
                'conf_long': 'INTERNATIONAL CONFERENCE ON INFORMATION AND KNOWLEDGE MANAGEMENT'
            }