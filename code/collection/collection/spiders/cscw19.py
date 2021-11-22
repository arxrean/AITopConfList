import pdb

import scrapy
from scrapy.selector import Selector


class Spider_CSCW19(scrapy.Spider):
    name = "cscw19"
    start_urls = [
        'https://cscw.acm.org/2019/toc.html'
    ]

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath("//a[contains(@class, 'DLtitleLink')]/text()"):
            yield {
                'title': article.extract().strip(),
                'year': '2019',
                'conf': 'CSCW',
                'conf_long': 'The ACM Conference on Computer Supported Cooperative Work'
            }