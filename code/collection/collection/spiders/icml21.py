import pdb

import scrapy
from scrapy.selector import Selector


class Spider_ICML20(scrapy.Spider):
    name = "icml21"
    start_urls = [
        'https://icml.cc/Conferences/2021/Schedule?type=Poster'
    ]

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath('//div[contains(@class, "maincardBody")]/text()'):
            yield {
                'title': article.extract().strip(),
                'year': '2021',
                'conf': 'ICML',
                'conf_long': 'International Conference on Machine Learning'
            }