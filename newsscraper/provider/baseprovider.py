import requests
from bs4 import BeautifulSoup
from abc import ABCMeta, abstractmethod
import time

from newsscraper.logs.logs_conf import logger


class BaseProvider(metaclass=ABCMeta):
    def __init__(self, url):
        self.url = url
        self.name = self.__class__.__name__

    def fetch_page(self, url):
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    def parse_page(self, html):
        return BeautifulSoup(html, 'html.parser')

    @abstractmethod
    def extract_articles(self, html):
        pass

    def scrape(self):
        print(f"start scrape {self.url} ...")
        logger.info(f"start scrape {self.url} ...")
        html = self.fetch_page(url=self.url)
        if html:
            soup = self.parse_page(html)
            articles = self.extract_articles(soup)
            print(f"end scraping {self.url}.")
            logger.info(f"end scraping {self.url}.")
            return articles
        return []
