import pdb

import scrapy
from scrapy.selector import Selector


class Spider_AAAI19(scrapy.Spider):
    name = "aaai19"
    start_urls = [
        'https://aaai.org/Library/AAAI/aaai19contents.php'
    ]

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath("//p[contains(@class, 'left')]/a[1]//text()"):
            yield {
                'title': article.extract().strip(),
                'year': '2019',
                'conf': 'AAAI',
                'conf_long': 'the Association for the Advancement of Artificial Intelligence'
            }