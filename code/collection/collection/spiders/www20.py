import pdb

import scrapy
from scrapy.selector import Selector

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Spider_WWW20(scrapy.Spider):
    name = "www20"
    start_urls = [
        'https://dl.acm.org/doi/proceedings/10.1145/3366423'
    ]

    def __init__(self):
        # add chrome driver to win10 PATH
        self.driver = webdriver.Chrome()

    def parse(self, response):
        self.driver.get(response.url)
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//h5[contains(@class, 'issue-item__title')]"))
        )

        selenium_response_text = self.driver.page_source
        hxs = Selector(text=selenium_response_text)
        articles = hxs.xpath("//h5/a/text()")
        for article in articles:
            yield {
                'title': article.extract().strip(),
                'year': '2020',
                'conf': 'WWW',
                'conf_long': 'International World Wide Web Conference'
            }