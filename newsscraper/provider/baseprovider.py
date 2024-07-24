import requests
from bs4 import BeautifulSoup
from abc import ABCMeta, abstractmethod

from webscraping.newsscraper.db.repository.articles import add_articles
from webscraping.newsscraper.db.repository.provider import get_provider, add_provider
from webscraping.newsscraper.db.models.engin import get_session
from webscraping.newsscraper.logs.logs_conf import logger


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

    def save_to_db(self, articles):
        session = get_session()
        logger.info("checking exist provider in db ...")
        provider = get_provider(self.name, session)
        if not provider:
            logger.info("not finde provider and creating new provider")
            add_provider(self.name, session)

        logger.info(f"provider {provider} exist in db.")
        add_articles(articles, session)
        session.close()

    def scrape(self):
        print(f"start scrape {self.url} ...")
        logger.info(f"start scrape {self.url} ...")
        html = self.fetch_page(url=self.url)
        if html:
            soup = self.parse_page(html)
            articles = self.extract_articles(soup)
            print(f"end scraping {self.url}.")
            logger.info(f"end scraping {self.url}.")
            logger.info("saving articles to db ...")
            self.save_to_db(articles)
            logger.info("seved all articles in db.")
            return articles
        return []
