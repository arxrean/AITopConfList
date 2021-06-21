import pdb

import scrapy
from scrapy.selector import Selector


class Spider_ACL20(scrapy.Spider):
    name = "acl20"
    start_urls = [
        'https://acl2020.org/program/accepted/'
    ]

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath('//h2[1]/following::p[2<=position() and position()<=779]/b/text()'):
            yield {
                'title': article.extract().strip(),
                'year': '2020',
                'conf': 'ACL',
                'conf_long': 'the Association for Computational Linguistics'
            }