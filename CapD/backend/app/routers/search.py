from fastapi import APIRouter, Query
from app.qdrant_utils import search_similar_news

router = APIRouter()
prefix = "/search"
tags = ["Search"]

@router.get("/")
def search_news(q: str = Query(..., description="검색할 뉴스 키워드")):
    return search_similar_news(q)
