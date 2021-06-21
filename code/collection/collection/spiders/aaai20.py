import pdb

import scrapy
from scrapy.selector import Selector


class Spider_AAAI20(scrapy.Spider):
    name = "aaai20"
    start_urls = [
        'https://aaai.org/Library/AAAI/aaai20contents-issue01.php',
        'https://aaai.org/Library/AAAI/aaai20contents-issue02.php',
        'https://aaai.org/Library/AAAI/aaai20contents-issue03.php',
        'https://aaai.org/Library/AAAI/aaai20contents-issue04.php',
        'https://aaai.org/Library/AAAI/aaai20contents-issue05.php',
        'https://aaai.org/Library/AAAI/aaai20contents-issue06.php',
        'https://aaai.org/Library/AAAI/aaai20contents-issue07.php',
    ]

    def parse(self, response):
        hxs = Selector(response)
        for article in hxs.xpath('//*[contains(@class, "left")]/a[1]/text()'):
            yield {
                'title': article.extract().strip(),
                'year': '2020',
                'conf': 'AAAI',
                'conf_long': 'the Association for the Advancement of Artificial Intelligence'
            }