import pdb

import scrapy
from scrapy.selector import Selector


class Spider_ACL18(scrapy.Spider):
    name = "acl18"
    start_urls = [
        'https://acl2018.org/programme/papers/'
    ]

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath("//span[contains(@class, 'paper-title')]/a/text()"):
            yield {
                'title': article.extract().strip(),
                'year': '2018',
                'conf': 'ACL',
                'conf_long': 'the Association for Computational Linguistics'
            }