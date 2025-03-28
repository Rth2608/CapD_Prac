from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app import crud, schemas, openai_utils, qdrant_utils

router = APIRouter()
prefix = "/news"
tags = ["News"]

@router.post("/")
def create_news(news: schemas.NewsCreate, db: Session = Depends(get_db)):
    db_news = crud.create_news(db, news)
    summary = openai_utils.summarize_text(news.content)
    updated = crud.update_news_summary(db, db_news.id, summary)
    qdrant_utils.add_news_to_qdrant(updated.id, summary)
    return updated

@router.get("/")
def get_news_list(db: Session = Depends(get_db)):
    return crud.get_all_news(db)
