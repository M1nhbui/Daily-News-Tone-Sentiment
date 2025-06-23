from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Text
import datetime

Base = declarative_base()

class NewsSentiment(Base):
    __tablename__ = 'news_sentiment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    source = Column(String(255))
    cleaned_text = Column(Text)
    tone = Column(String(50))
