from baseprovider import BaseProvider
from webscraping.newsscraper.article import Article


class RajanewsProvider(BaseProvider):
    def extract_article_date(self, link):
        html = self.fetch_page(link)
        soup = self.parse_page(html)
        datetime = soup.find("span", class_="date-display-single").text
        return datetime

    def extract_articles(self, soup):
        articles = []
        article_blocks = soup.find('div', class_='homepage')
        for article in article_blocks.find_all("div", class_="item"):
            link = self.url + article.find("a")["href"]
            title = article.find("div", class_="title").text
            image = article.find("img")["src"]
            summary = article.find("div", class_="lead").text
            date = self.extract_article_date(link)
            article_model = Article(image=image, title=title, date=date, link=link, summary=summary, provider=self.name)
            articles.append(article_model)
        return articles
