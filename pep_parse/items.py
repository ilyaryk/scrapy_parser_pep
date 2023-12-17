import scrapy
from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PepParseItem(scrapy.Item):
    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()


class PEP(Base):
    __tablename__ = 'pep'
    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    name = Column(Text)
    status = Column(Text)
