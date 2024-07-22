from webscraping.newsscraper.database.models.article import Articles
from webscraping.newsscraper.article import Article
from sqlalchemy.orm import Session


def add_articles(article: Article, db: Session):
    article_model_db = Articles(
        image=article.image,
        title=article.title,
        date=article.date,
        link=article.link,
        author=article.author,
        summary=article.summary,
    )
    db.add(article_model_db)
    db.commit()
    db.refresh(article_model_db)
    return article
