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
    name = "iclr21"
    start_urls = [
        'https://openreview.net/group?id=ICLR.cc/2021/Conference#oral-presentations',
    ]

    global manual_urls
    manual_urls = [
        'https://openreview.net/group?id=ICLR.cc/2021/Conference#oral-presentations',
        'https://openreview.net/group?id=ICLR.cc/2021/Conference#spotlight-presentations',
        'https://openreview.net/group?id=ICLR.cc/2021/Conference#poster-presentations'
    ]

    def __init__(self):
        # add chrome driver to win10 PATH
        self.driver = webdriver.Chrome('../../../chromedriver')

    def parse(self, response):
        global manual_urls
        for url in manual_urls:
            try:
                self.driver.get(url)
                self.driver.refresh()

                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'submissions-list')]"))
                )
                selenium_response_text = self.driver.page_source
                hxs = Selector(text=selenium_response_text)

                articles = hxs.xpath("//h4/*[1]/text()")
                for article in articles:
                    if article.extract().strip() != '':
                        yield {
                            'title': article.extract().strip(),
                            'year': '2021',
                            'conf': 'ICLR',
                            'conf_long': 'International Conference on Machine Learning'
                        }
            except:
                pass