# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, Integer, Float, String
from sqlalchemy.orm import relationship, sessionmaker
import sqlalchemy

Base = declarative_base()

class Rank(Base):
    __tablename__ = "ranks"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    scores = Column(Integer)
    
    player = relationship("Player", backref = "rank")

    def __repr__(self):
        return "<Rank(id='%d', name='%s', scores='%d')>" % (self.id, self.name, self.scores)

class Player(Base):
    __tablename__ = "players"

    name = Column(String, primary_key=True)
    scores = Column(Float)
    rank_id = Column(Integer, sqlalchemy.ForeignKey('ranks.id'))
    level = Column(Integer)
    experience = Column(BigInteger)
    kills = Column(Integer)
    dies = Column(Integer)
    kd = Column(Float)
    matches = Column(Integer)
    victories = Column(Integer)
    winrate = Column(Float)
    avg_stat = Column(Integer)

    def __repr__(self):
        return "<Player(name='%s', scores='%d', rank_id='%d', level='%d')>" % (self.name, self.scores, self.rank_id, self.level)

if __name__ == "__main__":
    engine = sqlalchemy.create_engine("sqlite:///griffin.db", echo=False)
    #Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    """session.add(Player(name="Лескон", scores=1000, rank_id=4, level=67, experience=40365, kills=69023, dies=70123, kd=0.81, matches=32874, victories=14876, winrate=36.1, avg_stat=248))
    session.add(Player(name="Солярис", scores=700, rank_id=3, level=69, experience=56912, kills=80493, dies=70123, kd=1.17, matches=35014, victories=10832, winrate=40.7, avg_stat=267))
    session.commit()"""
    for player in session.query(Player).all():
        print(player, player.rank)
    session.close()