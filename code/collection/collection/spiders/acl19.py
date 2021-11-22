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
        for i in range(4000):
            href = '/P19-{}/'.format(1000+i)
            try:
                article = hxs.xpath("//a[contains(@href, '{}')]//text()".format(href))[0].extract().strip()
                yield {
                    'title': article,
                    'year': '2019',
                    'conf': 'ACL',
                    'conf_long': 'the Association for Computational Linguistics'
                }
            except:
                pass

        for i in range(4000):
            href = '/W19-{}/'.format(3200+i)
            try:
                article = hxs.xpath("//a[contains(@href, '{}')]//text()".format(href))[0].extract().strip()
                yield {
                    'title': article,
                    'year': '2019',
                    'conf': 'ACL',
                    'conf_long': 'the Association for Computational Linguistics'
                }
            except:
                pass