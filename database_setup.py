import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

# User Class
class User(Base):
    __tablename__ = 'user'
   
    userId = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    picture = Column(String(255))

# Sport Category Class
class SportCategory(Base):
    __tablename__ = 'sportCategory'
    
    id = Column(Integer, primary_key = True)
    name = Column(String(255), nullable = False)
    userId = Column(Integer,ForeignKey('user.userId'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
        }
    

# Sporting Item Class
class SportingItem(Base):
    __tablename__ = 'sportingItems'

    id = Column(Integer, primary_key = True, autoincrement=True)
    name = Column(String(255), nullable = False)
    sport_cat_id = Column(Integer,ForeignKey('sportCategory.id'))
    sport = relationship(SportCategory) 
    userId = Column(Integer,ForeignKey('user.userId'))
    user = relationship(User)
    description = Column(String(255))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }
    
engine = create_engine('sqlite:///sportcatalog.db')

Base.metadata.create_all(engine)