from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class NewsBase(BaseModel):
    title: str
    content: str

class NewsCreate(NewsBase):
    pass

class NewsResponse(NewsBase):
    id: int
    summary: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
