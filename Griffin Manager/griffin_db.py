# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, Integer, Float, String, DateTime
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime
import sqlalchemy, sys

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
    last_update = Column(DateTime)

    def __repr__(self):
        return "<Player(name='%s', scores='%d', rank_id='%d', level='%d')>" % (self.name.encode('cp866', errors='replace').decode('cp866'), self.scores, self.rank_id, self.level)

if __name__ == "__main__":
    engine = sqlalchemy.create_engine("sqlite:///griffin.db", echo=False)
    #Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    """session.add(Player(name="Клым", scores=0, rank_id=1, level=78, experience=100654, kills=120934, dies=60234, kd=1.58, matches=80346, victories=40324, winrate=49.8, avg_stat=321, last_update=datetime(2017, 1, 30, 5, 10, 12)))
    session.add(Player(name="Лескон", scores=1000, rank_id=4, level=67, experience=40365, kills=69023, dies=70123, kd=0.81, matches=32874, victories=14876, winrate=36.1, avg_stat=248, last_update=datetime(2017, 1, 30, 2, 23, 45)))
    session.add(Player(name="Солярис", scores=700, rank_id=3, level=69, experience=56912, kills=80493, dies=70123, kd=1.17, matches=35014, victories=10832, winrate=40.7, avg_stat=267, last_update=datetime(2017, 1, 29, 18, 16, 23)))
    session.commit()
    session.add(Player(name="Для удаления игрок", scores=700, rank_id=3, level=69, experience=56912, kills=80493, dies=70123, kd=1.17, matches=35014, victories=10832, winrate=40.7, avg_stat=267, last_update=datetime(2017, 1, 29, 18, 16, 23)))
    session.commit()"""
    for player in session.query(Player).all():
        print(player, player.rank)
    session.close()