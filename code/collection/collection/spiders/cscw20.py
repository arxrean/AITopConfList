import pdb

import scrapy
from scrapy.selector import Selector


class Spider_CSCW20(scrapy.Spider):
    name = "cscw20"
    start_urls = [
        'https://cscw.acm.org/2020/toc.html'
    ]

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath("//a[contains(@class, 'DLtitleLink')]/text()"):
            yield {
                'title': article.extract().strip(),
                'year': '2020',
                'conf': 'CSCW',
                'conf_long': 'The ACM Conference on Computer Supported Cooperative Work'
            }