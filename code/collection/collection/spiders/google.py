import pdb

import scrapy
from scrapy.selector import Selector

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def url_compose(key, source, pg):
		url = 'https://scholar.google.com/scholar?start={}&q={}+source:"{}"&hl=en&as_sdt=0,14'.format(pg*10, key, '+'.join(source.split()))
		return url


class Spider_Google(scrapy.Spider):
	name = "google"

	def start_requests(self):
		keywords = ['expert', 'crowd'] # keywords that you want to search in google scholar
		sources = ['The Web Conference', 'Human Factors in Computing Systems'] # conferences/journals that you want to include
		pages = 5 # pages you want to search (exclusive)

		start_urls = []
		for key in keywords:
			for sou in sources:
				for pg in range(pages):
					start_urls.append(url_compose(key, sou, pg))

		for url in start_urls:
			yield self.make_requests_from_url(url)


	def __init__(self):
		# add chrome driver to win10 PATH
		self.driver = webdriver.Chrome(executable_path='../../chromedriver')


	def parse(self, response):
		# with open('page.html', 'wb') as html_file:
		# 	html_file.write(response.body)
			
		self.driver.get(response.request.url)
		WebDriverWait(self.driver, 60).until(
			EC.presence_of_element_located((By.XPATH, "//h3/a"))
		)
		selenium_response_text = self.driver.page_source
		hxs = Selector(text=selenium_response_text)
		for article in hxs.xpath("//h3/a"):
			title = ' '.join(article.xpath('.//text()').extract()).strip()
			yield {
				'title': ' '.join([x for x in title.split() if x != ' ']),
				'url': response.request.url
			}