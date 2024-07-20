from baseprovider import BaseProvider
from newsscraper.article import Article


class AsriranProvider(BaseProvider):
    def extract_article_date(self, link):
        html = self.fetch_page(link)
        soup = self.parse_page(html)
        datetime = "".join(soup.find("div", class_="news_nav news_pdate_c").text.split()[1:])
        return datetime

    def extract_articles(self, soup):
        articles = []
        article_blocks = soup.find_all('div', class_='box2-cover c-box-cover panel_kh row')[1]
        for article in article_blocks.find_all('article', class_='box box2')[3:]:
            link = self.url + article.find('a')['href']
            title = article.find('h2', class_='Htag').find('a')['title']
            image = article.find('img')["data-src"]
            summary = article.find("div", class_="lead1").text
            date = self.extract_article_date(link)
            article_model = Article(image=image, title=title, date=date, link=link, summary=summary)
            articles.append(article_model)
        return articles