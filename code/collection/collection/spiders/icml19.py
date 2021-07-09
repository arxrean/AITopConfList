import pdb

import scrapy
from scrapy.selector import Selector


class Spider_ICML19(scrapy.Spider):
    name = "icml19"
    start_urls = [
        'https://icml.cc/Conferences/2019/Schedule?type=Poster'
    ]

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath("//div[contains(@class, 'maincardBody')]/text()"):
            yield {
                'title': article.extract().strip(),
                'year': '2019',
                'conf': 'ICML',
                'conf_long': 'International Conference on Machine Learning'
            }