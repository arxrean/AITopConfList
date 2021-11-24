import pdb

import scrapy
from scrapy.selector import Selector

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Spider_WWW20(scrapy.Spider):
    name = "www21"
    start_urls = [
        'https://www2021.thewebconf.org/program/papers/'
    ]

    def __init__(self):
        # add chrome driver to win10 PATH
        self.driver = webdriver.Chrome('../../../chromedriver')

    def parse(self, response):
        self.driver.get(response.url)
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//tr//strong"))
        )

        selenium_response_text = self.driver.page_source
        hxs = Selector(text=selenium_response_text)
        articles = hxs.xpath("//tr//strong/text()")
        for article in articles:
            if article.extract().strip() not in ['Title:', 'Authors:', '']:
                yield {
                    'title': article.extract().strip(),
                    'year': '2021',
                    'conf': 'WWW',
                    'conf_long': 'International World Wide Web Conference'
                }