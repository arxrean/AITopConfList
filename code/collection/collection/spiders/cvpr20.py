import pdb

import scrapy
from scrapy.selector import Selector


class Spider_CVPR20(scrapy.Spider):
    name = "cvpr20"
    start_urls = [
        'https://openaccess.thecvf.com/CVPR2020?day=2020-06-16',
        'https://openaccess.thecvf.com/CVPR2020?day=2020-06-17',
        'https://openaccess.thecvf.com/CVPR2020?day=2020-06-18'
    ]

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath('//*[contains(@class, "ptitle")]/a/text()'):
            yield {
                'title': article.extract(),
                'year': '2020',
                'conf': 'CVPR',
                'conf_long': 'The Conference on Computer Vision and Pattern Recognition'
            }