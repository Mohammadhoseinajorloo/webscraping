from webscraping.newsscraper.db.models.article import Article
from sqlalchemy.orm import Session


def add_articles(articles: list, session: Session):
    for article_data in articles:
        article = Article(
            link=article_data["link"],
            title=article_data["title"],
            summary=article_data["summary"],
            date=article_data["date"],
            author=article_data["author"],
            image=article_data["image"]
        )
        session.add(article)
    session.commit()