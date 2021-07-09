import pdb

import scrapy
from scrapy.selector import Selector


class Spider_CVPR18(scrapy.Spider):
    name = "cvpr18"
    start_urls = [
        'https://openaccess.thecvf.com/CVPR2018.py?day=2018-06-19',
        'https://openaccess.thecvf.com/CVPR2018.py?day=2018-06-20',
        'https://openaccess.thecvf.com/CVPR2018.py?day=2018-06-21'
    ]

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath("//dt[contains(@class, 'ptitle')]//a/text()"):
            yield {
                'title': article.extract().strip(),
                'year': '2018',
                'conf': 'CVPR',
                'conf_long': 'The Conference on Computer Vision and Pattern Recognition'
            }