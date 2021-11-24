import pdb
from time import sleep

import scrapy
from scrapy.selector import Selector

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class Spider_ICLR19(scrapy.Spider):
    name = "iclr19"
    start_urls = [
        'https://openreview.net/group?id=ICLR.cc/2019/Conference#accepted-oral-papers',
        'https://openreview.net/group?id=ICLR.cc/2019/Conference#accepted-poster-papers'
    ]

    def __init__(self):
        self.driver = webdriver.Chrome('../../../chromedriver')

    def parse(self, response):
        self.driver.get(response.request.url)
        self.driver.refresh()
        # pdb.set_trace()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, str(self.choose_wait(response.request.url))))
        )
        selenium_response_text = self.driver.page_source
        hxs = Selector(text=selenium_response_text)

        articles = hxs.xpath("//li[contains(@class, 'note')]//h4/a/text()")
        for article in articles:
            if article.extract().strip() != '':
                yield {
                    'title': article.extract().strip(),
                    'year': '2019',
                    'conf': 'ICLR',
                    'conf_long': 'International Conference on Machine Learning'
                }


    def choose_wait(self, url):
        if url == 'https://openreview.net/group?id=ICLR.cc/2019/Conference#accepted-oral-papers':
            return "//a[contains(@href, '/forum?id=B1gabhRcYX')]"
        elif url == 'https://openreview.net/group?id=ICLR.cc/2019/Conference#accepted-poster-papers':
            return "//a[contains(@href, '/forum?id=B1G5ViAqFm')]"