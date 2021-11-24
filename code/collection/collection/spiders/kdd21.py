import pdb

import scrapy
from scrapy.selector import Selector


class Spider_KDD20(scrapy.Spider):
    name = "kdd21"
    start_urls = [
        'https://kdd.org/kdd2021/accepted-papers/index'
    ]

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath('//div[contains(@class, "media-body")]//font/text()'):
            yield {
                'title': article.extract().strip(),
                'year': '2021',
                'conf': 'KDD',
                'conf_long': 'Special Interest Group on Knowledge Discovery and Data Mining'
            }