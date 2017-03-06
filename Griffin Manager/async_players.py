# -*- coding: utf-8 -*-

import asyncio
import requests
import time

from config import clan
from quamash import QEventLoop, QThreadExecutor
from PyQt5.QtWidgets import QMessageBox

async def get_players(wnd):
    # send two request to get two pages of players
    loop = asyncio.get_event_loop()
    url = "https://survarium.pro/api/v2/clans/%s/players/" % clan
    to_do = [(url, {'limit': 50, 'skip': 0}), (url, {'limit': 50, 'skip': 50})]
    players = []
    futures = []
    # coroutine runned in QThreadExecutor doesn't block event loop
    with QThreadExecutor(2) as executor:
        for params in to_do:
            future = loop.run_in_executor(executor, send_request, *params)
            futures.append(future)
        for future in futures:
            response = await future
            players += response['data']
            wnd.progressBar.setValue(wnd.progressBar.value() + 2.5)
    return players

async def get_stats(wnd):
    loop = asyncio.get_event_loop()
    futures = {}
    updates = {}
    with QThreadExecutor(35) as executor:
        # prepare future objects and associate it with players db objects
        for player in wnd.players:
            url = "https://survarium.pro/api/v2/players/%s/stats" % player.name
            params = {'limit': 50, 'skip': 0}
            future = loop.run_in_executor(executor, send_request, url, params)
            futures[future] = (player, url, params)

        # iter by future objects and read responses
        for future in futures.keys():
            # unpack tupe associated with current future
            player, url, params = futures[future]
            scores_to_add = 0
            response = await future
            # if the player is new set last match id
            if player.match_id == 0:
                player.match_id = response['data'][0]['match']['id']
            else:
                # remember las match id and go to add scores
                last_match_id = response['data'][0]['match']['id']
                is_next = True
                while is_next:
                    for match in response['data']:
                        if player.match_id == match['match']['id']:
                            # if we found last match on this page break from loops
                            is_next = False
                            break
                        scores_to_add += match['score'] * 0.01
                    else:
                        # if last match doesn't on this page, get the next one
                        params['skip'] += 50
                        response = await loop.run_in_executor(executor, send_request, url, params)
                # set new scores and rank
                player.match_id = last_match_id
                player.scores += scores_to_add
                if scores_to_add != 0:                    
                    updates[player.name] = scores_to_add
                if player.scores < 0:
                    player.scores = 0
                if  player.scores > wnd.ranks[-1].scores:
                    player.scores = wnd.ranks[-1].scores
                # find rank by scores
                player.rank = wnd.find_rank(player.scores)
                # update progress bar
                wnd.progressBar.setValue(wnd.progressBar.value() + (95 / len(futures)))
    wnd.progressBar.setValue(100)
    return updates

def send_request(url, params):
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise requests.exceptions.HTTPError("Ошибка %d. Данные по запросу не получены" % response.status_code)
    return response.json()