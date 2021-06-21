import pdb

import scrapy
from scrapy.selector import Selector


class Spider_KDD20(scrapy.Spider):
    name = "kdd20"
    start_urls = [
        'https://www.kdd.org/kdd2020/accepted-papers'
    ]

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath('//h2[1]/following::div[1]//a/text()'):
            yield {
                'title': article.extract().strip(),
                'year': '2020',
                'conf': 'KDD',
                'conf_long': 'Special Interest Group on Knowledge Discovery and Data Mining'
            }