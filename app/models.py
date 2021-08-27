from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, DateTime

from db import Base
"""
id
title
content
timestamp
updated
"""

class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=False)
    content = Column(String, index=False, nullable=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), onupdate=func.now())