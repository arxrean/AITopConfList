import pdb
from time import sleep

import scrapy
from scrapy.selector import Selector

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class Spider_ICLR18(scrapy.Spider):
    name = "iclr18"
    start_urls = [
        'https://openreview.net/group?id=ICLR.cc/2018/Conference#accepted-oral-papers'
    ]

    def __init__(self):
        # add chrome driver to win10 PATH
        self.driver = webdriver.Chrome('../../../chromedriver')

    def parse(self, response):
        self.driver.get(response.request.url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@id, 'accepted-oral-papers')]//h4"))
        )
        selenium_response_text = self.driver.page_source
        hxs = Selector(text=selenium_response_text)

        articles = hxs.xpath("//div[contains(@id, 'accepted-oral-papers')]//h4/a[1]/text()") + hxs.xpath("//div[contains(@id, 'accepted-poster-papers')]//h4/a[1]/text()")
        for article in articles:
            if article.extract().strip() != '':
                yield {
                    'title': article.extract().strip(),
                    'year': '2018',
                    'conf': 'ICLR',
                    'conf_long': 'International Conference on Machine Learning'
                }