import pdb

import scrapy
from scrapy.selector import Selector


class Spider_ACL20(scrapy.Spider):
    name = "acl21"
    start_urls = [
        'https://2021.aclweb.org/program/accept/'
    ]

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath('//p/strong/text()'):
            yield {
                'title': article.extract().strip(),
                'year': '2021',
                'conf': 'ACL',
                'conf_long': 'the Association for Computational Linguistics'
            }