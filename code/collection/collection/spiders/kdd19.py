import pdb

import scrapy
from scrapy.selector import Selector


class Spider_KDD19(scrapy.Spider):
    name = "kdd19"
    start_urls = [
        'https://dblp.org/db/conf/kdd/kdd2019.html'
    ]

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath("//ul[contains(@class, 'publ-list')][3 <= position()]//span[contains(@class, 'title')]/text()"):
            yield {
                'title': article.extract().strip(),
                'year': '2019',
                'conf': 'KDD',
                'conf_long': 'Special Interest Group on Knowledge Discovery and Data Mining'
            }