# -*- coding: utf-8 -*-

import asyncio
import aiohttp
import requests
import time

from config import clan
from quamash import QEventLoop, QThreadExecutor
from PyQt5.QtWidgets import QMessageBox

async def commit(session, players):
    # async commit to database and file dump
    loop = asyncio.get_event_loop()
    with QThreadExecutor(1) as executor:
        #await loop.run_in_executor(executor, session.commit)
        #await loop.run_in_executor(executor, players.save_dump)
        await asyncio.sleep(1)

async def rollback(session, players):
    # async rollback and count score changes
    loop = asyncio.get_event_loop()
    with QThreadExecutor(1) as executor: 
        await loop.run_in_executor(executor, session.rollback)
        changes = await loop.run_in_executor(executor, players.count_diff)
        return changes

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
    to_do = []
    updates = {}
    # prepare future objects and associate it with players db objects
    for player in wnd.players:
        url = "https://survarium.pro/api/v2/players/%s/stats" % player.name
        params = {'limit': 50, 'skip': 0}
        to_do.append(get_player_stat(player, url, params, updates))
        to_do_iter = asyncio.as_completed(to_do)

    t0 = time.time()

    # iter by future objects and update gui
    for future in to_do_iter:
        player = await future

        if player.scores < 0:
            player.scores = 0
        if  player.scores > wnd.ranks[-1].scores:
            player.scores = wnd.ranks[-1].scores
        # find rank by scores
        player.rank = wnd.find_rank(player.scores)
        # update progress bar
        wnd.progressBar.setValue(wnd.progressBar.value() + (95 / len(to_do)))

    print("Elapsed: %.2f" % (time.time() - t0))

    wnd.progressBar.setValue(100)
    return updates

async def get_player_stat(player, url, params, updates):
    response = await asend_request(url, params)
    scores_to_add = 0

    # if the player is new set last match id
    if player.match_id == 0:
        player.match_id = response['data'][0]['match']['id']
    else:
        # remember last match id and go to add scores
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
                response = await asyncio.ensure_future(send_request(url, params))
        # set new scores and rank
        player.match_id = last_match_id
        player.scores += scores_to_add
        if scores_to_add != 0:                    
            updates[player.name] = scores_to_add
    return player

async def asend_request(url, params):
    response = await aiohttp.request("GET", url, params=params)
    json = await response.json()
    return json

def send_request(url, params):
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise requests.exceptions.HTTPError("Ошибка %d. Данные по запросу не получены" % response.status_code)
    return response.json()