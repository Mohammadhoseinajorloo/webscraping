from webscraping.newsscraper.provider.baseprovider import BaseProvider
from webscraping.newsscraper.article import Article
from webscraping.newsscraper.logs.logs_conf import logger


class RajanewsProvider(BaseProvider):
    def extract_article_date(self, link):
        logger.info(f"fetche paghe for scrape {link}")
        html = self.fetch_page(link)
        logger.info(f"parse page for scrape {link}")
        soup = self.parse_page(html)
        datetime = soup.find("span", class_="date-display-single").text
        logger.info(f"finde date in {link}")
        return datetime

    def extract_articles(self, soup):
        article_number = 1
        articles = []
        article_blocks = soup.find('div', class_='homepage')
        logger.info(f"finde {len(article_blocks)} article for scraping from {self.url}")
        for article in article_blocks.find_all("div", class_="item"):
            link = self.url + article.find("a")["href"]
            title = article.find("div", class_="title").text
            image = article.find("img")["src"]
            summary = article.find("div", class_="lead").text
            date = self.extract_article_date(link)
            article_model = Article(image=image, title=title, date=date, link=link, summary=summary, provider=self.name)
            logger.info(f"create {article_number} article from {self.url}")
            articles.append(article_model)
            logger.info(f"add {article_number} in articles list")
            article_number += 1

        return articles
