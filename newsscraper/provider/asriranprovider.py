from newsscraper.provider.baseprovider import BaseProvider
from newsscraper.article import Article


class AsriranProvider(BaseProvider):
    def extract_article_date(self, link):
        print(f"fetche paghe for scrape {link}")
        html = self.fetch_page(link)
        print(f"parse page for scrape {link}")
        soup = self.parse_page(html)
        datetime = "".join(soup.find("div", class_="news_nav news_pdate_c").text.split()[1:])
        print(f"finde date in {link}")
        return datetime

    def extract_articles(self, soup):
        article_number = 1
        articles = []
        article_blocks = soup.find_all('div', class_='box2-cover c-box-cover panel_kh row')[1]
        print(f"enter into home page {article_blocks}")
        for article in article_blocks.find_all('article', class_='box box2')[3:]:
            link = self.url + article.find('a')['href']
            title = article.find('h2', class_='Htag').find('a')['title']
            image = article.find('img')["data-src"]
            summary = article.find("div", class_="lead1").text
            date = self.extract_article_date(link)
            article_model = Article(image=image, title=title, date=date, link=link, summary=summary, provider=self.name)
            print(f"create {article_number} article from {self.url}")
            articles.append(article_model)
            print(f"add {article_number} in articles list")
            article_number += 1

        return articles
