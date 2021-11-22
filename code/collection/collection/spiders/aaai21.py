import pdb

import scrapy
from scrapy.selector import Selector


class Spider_AAAI20(scrapy.Spider):
    name = "aaai21"
    start_urls = ['https://www.aaai.org/Library/AAAI/aaai21-issue{:02d}.php'.format(i) for i in range(1, 19)]

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath("//*[contains(@class, 'left')]/a[1]/text()"):
            yield {
                'title': article.extract().strip(),
                'year': '2021',
                'conf': 'AAAI',
                'conf_long': 'the Association for the Advancement of Artificial Intelligence'
            }