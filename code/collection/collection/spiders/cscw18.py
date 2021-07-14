import pdb

import scrapy
from scrapy.selector import Selector


class Spider_CSCW18(scrapy.Spider):
    name = "cscw18"
    start_urls = [
        'https://cscw.acm.org/2018/program/toc.html'
    ]

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath("(//a[contains(@class, 'DLtitleLink')])[position()>=2]/text()"):
            yield {
                'title': article.extract().strip(),
                'year': '2018',
                'conf': 'CSCW',
                'conf_long': 'The ACM Conference on Computer Supported Cooperative Work'
            }