import pdb

import scrapy
from scrapy.selector import Selector


class Spider_KDD18(scrapy.Spider):
    name = "kdd18"
    start_urls = [
        'https://www.kdd.org/kdd2018/accepted-papers'
    ]

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath("//div[contains(@class, 'media-body')]//a/text()"):
            yield {
                'title': article.extract().strip(),
                'year': '2018',
                'conf': 'KDD',
                'conf_long': 'Special Interest Group on Knowledge Discovery and Data Mining'
            }