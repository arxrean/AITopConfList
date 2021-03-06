import pdb

import scrapy
from scrapy.selector import Selector


class Spider_CIKM18(scrapy.Spider):
    name = "cikm18"
    start_urls = [
        'https://dblp.org/db/conf/cikm/cikm2018.html',
    ]

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath("//span[contains(@class, 'title')]/text()"):
            yield {
                'title': article.extract().strip(),
                'year': '2018',
                'conf': 'CIKM',
                'conf_long': 'INTERNATIONAL CONFERENCE ON INFORMATION AND KNOWLEDGE MANAGEMENT'
            }