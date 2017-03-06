# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, Integer, Float, String, DateTime, text
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime
from config import SQLALCHEMY_DATABASE_URI
import sqlalchemy, sys

Base = declarative_base()

class Rank(Base):
    __tablename__ = "ranks"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    scores = Column(Integer)
    
    player = relationship("Player", backref = "rank")

    def __repr__(self):
        return "<Rank(id='%d', name='%s', scores='%d')>" % (self.id, self.name, self.scores)

class Player(Base):
    __tablename__ = "players"

    name = Column(String(255), primary_key=True)
    scores = Column(Float)
    rank_id = Column(Integer, sqlalchemy.ForeignKey('ranks.id'))
    match_id = Column(BigInteger)
    level = Column(Integer)
    experience = Column(BigInteger)
    kills = Column(Integer)
    dies = Column(Integer)
    kd = Column(Float)
    matches = Column(Integer)
    victories = Column(Integer)
    winrate = Column(Float)
    avg_stat = Column(Integer)
    last_update = Column(DateTime)

    def __repr__(self):
        return "<Player(name='%s', scores='%.2f', rank_id='%d', level='%d')>" % (self.name.encode('cp866', errors='replace').decode('cp866'), self.scores, self.rank_id, self.level)

if __name__ == "__main__":
    engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI)
    # Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    """session.add(Rank(id = 1, name = "Выживший", scores = 0))
    session.add(Rank(id = 2, name = "Адепт", scores = 200))
    session.add(Rank(id = 3, name = "Матерый", scores = 630))
    session.add(Rank(id = 4, name = "Ловчий", scores = 900))
    session.add(Rank(id = 5, name = "Рейтар", scores = 1800))
    session.add(Rank(id = 6, name = "Хорунжий ", scores = 3150))
    session.add(Rank(id = 7, name = "Ветеран", scores = 4500))
    session.add(Rank(id = 8, name = "Центурион", scores = 5850))
    session.add(Rank(id = 9, name = "Пилигрим", scores = 7200))
    session.add(Rank(id = 10, name = "Сталкер", scores = 8550))
    session.add(Rank(id = 11, name = "Волхв", scores = 9900))
    session.add(Rank(id = 12, name = "Хранитель", scores = 11000))
    session.add(Rank(id = 13, name = "Мастер", scores = 11000))
    session.commit()"""
    for rank in session.query(Rank).all():
        print(rank)
    session.close()