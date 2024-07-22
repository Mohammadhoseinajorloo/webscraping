from webscraping.newsscraper.database.models.article import Articles
from sqlalchemy.orm import Session


def add_articles(articles: list, db: Session):
    counter = 0
    for article in articles:
        article_model_db = Articles(
            image=article.image,
            title=article.title,
            date=article.date,
            link=article.link,
            author=article.author,
            summary=article.summary,

        )
        db.add(article_model_db)
        counter += 1

        if counter < 10:
            db.commit()
            db.refresh(article_model_db)
        continue
