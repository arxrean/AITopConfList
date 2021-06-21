import pdb

import scrapy
from scrapy.selector import Selector


class Spider_ECCV20(scrapy.Spider):
    name = "eccv20"
    start_urls = ['https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/{}_ECCV_2020_paper.php'.format(i) for i in range(20000)]

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath('//div[@id="papertitle"]/text()'):
            print(article.extract().strip())
            yield {
                'title': article.extract().strip(),
                'year': '2020',
                'conf': 'ECCV',
                'conf_long': 'European Conference on Computer Vision'
            }