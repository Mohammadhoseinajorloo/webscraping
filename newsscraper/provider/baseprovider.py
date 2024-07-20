import requests
from bs4 import BeautifulSoup
from abc import ABCMeta, abstractmethod


class BaseProvider(metaclass=ABCMeta):
    def __init__(self, url):
        self.url = url

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
        html = self.fetch_page(url=self.url)
        if html:
            soup = self.parse_page(html)
            return self.extract_articles(soup)
        return []
