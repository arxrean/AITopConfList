import pdb

import scrapy
from scrapy.selector import Selector


class Spider_CVPR19(scrapy.Spider):
    name = "cvpr19"
    start_urls = [
        'https://openaccess.thecvf.com/CVPR2019.py?day=2019-06-18',
        'https://openaccess.thecvf.com/CVPR2019.py?day=2019-06-19',
        'https://openaccess.thecvf.com/CVPR2019.py?day=2019-06-20'
    ]

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath("//dt[contains(@class, 'ptitle')]//a/text()"):
            yield {
                'title': article.extract().strip(),
                'year': '2019',
                'conf': 'CVPR',
                'conf_long': 'The Conference on Computer Vision and Pattern Recognition'
            }