from pydantic import BaseModel
from sqlalchemy import Integer, String, Column, Text, DateTime
from typing import Optional
from datetime import datetime


from backend.app.db.base_class import Base


class Note(Base):
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    text = Column(Text, nullable=False)
    title = Column(String, nullable=False)
    create = Column(DateTime, default=datetime.utcnow(), nullable=False)


class CreateNote(BaseModel):
    title: str
    text: str


class NoteUpdate(BaseModel):
    title: Optional[str] = None
    text: Optional[str] = None
