# -*- coding: utf-8 -*-

import reprlib
import struct

from griffin_db import Player

from datetime import datetime, timedelta
from collections import UserList

class PlayersList(UserList):
    """ Container for database objects of players """

    def __init__(self, players = None):
        return super().__init__(players)

    def __getitem__(self, i):
        if isinstance(i, str):
            player = list(filter(lambda x: x.name == i, self.data))
            if len(player) == 0:
                raise IndexError("Can not to find player in list with name '%s'." % i)
            else:
                return player[0]
        return super().__getitem__(i)

    def __contains__(self, item):
        if isinstance(item, dict):
            func = lambda x: x.name == item['nickname']
        elif isinstance(item, str):
            func = lambda x: x.name == item
        else:
            return super().__contains__(item)
        count = len(list(filter(func, self.data)))
        return not count == 0

    def __repr__(self):
        myRepr = reprlib.Repr()
        myRepr.maxother = 50
        myRepr.maxlist = 3
        return myRepr.repr_list(self.data, 1)

    def update_player(self, x):
        p = self.__getitem__(x['nickname'])
        p.level = x['progress']['level']
        p.experience = x['progress']['experience']
        p.kills=x['total']['kills']
        p.dies = x['total']['dies']
        p.kd = x['total']['kd']
        p.matches = x['total']['matches']
        p.victories = x['total']['victories']
        p.winrate = x['total']['winRate']
        p.avg_stat = x['total']['scoreAvg']
        p.last_update = PlayersList.parse_datetime(x['updatedAt'], 3)

    @classmethod
    def create_player(cls, rank, x):
        # create database object of player
        player = Player(name=x['nickname'],
                        scores = 0,
                        rank_id = 1,
                        match_id = 0,
                        level = x['progress']['level'],
                        experience= x['progress']['experience'],
                        kills = x['total']['kills'],
                        dies = x['total']['dies'],
                        kd = x['total']['kd'],
                        matches = x['total']['matches'],
                        victories = x['total']['victories'],
                        winrate = x['total']['winRate'],
                        avg_stat = x['total']['scoreAvg'])
        # set object of rank and parse last updated time
        player.rank = rank
        player.last_update = PlayersList.parse_datetime(x['updatedAt'], 3)
        return player

    @classmethod
    def parse_datetime(cls, strdatetime, hdelta):
        return datetime.strptime(strdatetime, "%Y-%m-%dT%H:%M:%S.%fZ") + timedelta(hours=hdelta)

    def save_dump(self):
        with open("players.dump", "wb") as file:
            for player in self.data:
                file.write(struct.pack("40sf", bytes(player.name.encode("utf-8")), player.scores))

    def read_dump(self):
        with open("players.dump", "rb") as file:
            while True:
                try:
                    dump = struct.unpack("40sf", file.read(44))
                    name = dump[0].rstrip(b'\0').decode('utf-8')
                    yield (name, dump[1])
                except:
                    break

    def count_diff(self):
        """
        Generate the dictionary 
        that contains scores difference 
        after connecting with database
        """
        diff = {}
        for name, scores in self.read_dump():
            try:
                diff_sc = self.__getitem__(name).scores - round(scores, 2)
            except IndexError:
                continue
            if diff_sc == 0:
                continue
            diff[name] = diff_sc
        return diff