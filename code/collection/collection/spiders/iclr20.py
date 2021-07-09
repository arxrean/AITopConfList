import pdb

import scrapy
from scrapy.selector import Selector

import json


class Spider_ICLR20(scrapy.Spider):
    name = "iclr20"
    start_urls = [
        'https://iclr.cc/virtual_2020/papers.json'
    ]

    def parse(self, response):
        # pdb.set_trace()
        data = json.loads(response.text)
        for article in data:
            yield {
                'title': article['content']['title'].strip(),
                'year': '2020',
                'conf': 'ICML',
                'conf_long': 'International Conference on Machine Learning'
            }