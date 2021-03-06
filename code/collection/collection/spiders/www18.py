import pdb

import scrapy
from scrapy.selector import Selector


class Spider_WWW18(scrapy.Spider):
    name = "www18"
    start_urls = [
        'https://dblp.org/db/conf/cikm/cikm2018.html',
    ]

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath("//ul[contains(@class, 'publ-list')][2 <= position()]//span[contains(@class, 'title')]/text()"):
            yield {
                'title': article.extract().strip(),
                'year': '2018',
                'conf': 'WWW',
                'conf_long': 'International World Wide Web Conference'
            }