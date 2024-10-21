#!/usr/bin/env python3
"""video model"""
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.base_model import BaseModel


class Video(BaseModel):
    __tablename__ = 'videos'
    comments = relationship('Comment', back_populates='video')
    title = Column(String(20), nullable=False)
    description = Column(String(60), nullable=False)
    video_url = Column(String(60), nullable=False)
    thumbnail_url = Column(String(60), nullable=False)