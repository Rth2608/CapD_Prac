from sqlalchemy.orm import Session
from app import models, schemas

def create_news(db: Session, news: schemas.NewsCreate):
    db_news = models.News(**news.dict())
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news

def update_news_summary(db: Session, news_id: int, summary: str):
    news = db.query(models.News).filter(models.News.id == news_id).first()
    if news:
        news.summary = summary
        db.commit()
        db.refresh(news)
    return news

def get_all_news(db: Session):
    return db.query(models.News).all()
