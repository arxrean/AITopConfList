import pdb

import scrapy
from scrapy.selector import Selector


class Spider_ECCV18(scrapy.Spider):
    name = "eccv18"
    start_urls = ['https://openaccess.thecvf.com/ECCV2018']

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath("//dt[contains(@class, 'ptitle')]//a/text()"):
            yield {
                'title': article.extract().strip(),
                'year': '2018',
                'conf': 'ECCV',
                'conf_long': 'European Conference on Computer Vision'
            }