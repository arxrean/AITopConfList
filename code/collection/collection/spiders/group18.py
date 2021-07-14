import pdb

import scrapy
from scrapy.selector import Selector


class Spider_GROUP18(scrapy.Spider):
    name = "group18"
    start_urls = [
        'https://dblp.org/db/conf/group/group2018.html',
    ]

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath("//ul[contains(@class, 'publ-list')][2 <= position()]//span[contains(@class, 'title')]/text()"):
            yield {
                'title': article.extract().strip(),
                'year': '2018',
                'conf': 'GROUP',
                'conf_long': 'The ACM International Conference on Supporting Group Work'
            }