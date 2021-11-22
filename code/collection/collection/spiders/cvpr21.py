import pdb

import scrapy
from scrapy.selector import Selector


class Spider_CVPR20(scrapy.Spider):
    name = "cvpr21"
    start_urls = ['https://openaccess.thecvf.com/CVPR2021?day=all']

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath('//*[contains(@class, "ptitle")]/a/text()'):
            yield {
                'title': article.extract(),
                'year': '2021',
                'conf': 'CVPR',
                'conf_long': 'The Conference on Computer Vision and Pattern Recognition'
            }