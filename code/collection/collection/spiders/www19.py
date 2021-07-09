import pdb

import scrapy
from scrapy.selector import Selector

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Spider_WWW19(scrapy.Spider):
    name = "www19"
    start_urls = [
        'https://thewebconf.org/www2019/accepted-papers/'
    ]

    def __init__(self):
        # add chrome driver to win10 PATH
        self.driver = webdriver.Chrome()

    def parse(self, response):
        self.driver.get(response.url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li/p[contains(@class, 'name')]"))
        )

        selenium_response_text = self.driver.page_source
        hxs = Selector(text=selenium_response_text)
        articles = hxs.xpath("//li/p[contains(@class, 'name')]/text()")
        for article in articles:
            yield {
                'title': article.extract().strip(),
                'year': '2020',
                'conf': 'WWW',
                'conf_long': 'International World Wide Web Conference'
            }