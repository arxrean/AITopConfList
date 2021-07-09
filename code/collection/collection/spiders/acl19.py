import pdb

import scrapy
from scrapy.selector import Selector


class Spider_ACL19(scrapy.Spider):
    name = "acl19"
    start_urls = [
        'https://aclanthology.org/events/acl-2019/'
    ]

    def parse(self, response):
        hxs = Selector(response)
        for i in range(1, 661):
            href = '/P19-{}/'.format(1000+i)
            article = hxs.xpath("//a[contains(@href, '{}')]//text()".format(href))[0].extract().strip()
            yield {
                'title': article,
                'year': '2019',
                'conf': 'ACL',
                'conf_long': 'the Association for Computational Linguistics'
            }