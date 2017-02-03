# -*- coding: utf-8 -*-

import asyncio
import requests
import time

from quamash import QEventLoop, QThreadExecutor
from PyQt5.QtWidgets import QMessageBox

async def get_players(wnd):
    # send two request to get two pages of players
    loop = asyncio.get_event_loop()
    url = "https://survarium.pro/api/v2/clans/Грифон/players/"
    to_do = [(url, {'limit': 50, 'skip': 0}), (url, {'limit': 50, 'skip': 50})]
    players = []
    futures = []
    # coroutine runned in QThreadExecutor doesn't block event loop
    with QThreadExecutor(2) as executor:
        for params in to_do:
            future = loop.run_in_executor(executor, send_request, *params)
            futures.append(future)
        for future in futures:
            try:
                response = await future
                players += response['data']
            except requests.exceptions.ConnectionError:
                QMessageBox.about(wnd.form, "Ошибка соединения", "Не удалось установить соединение с survarium.pro")
                break
    return players

async def get_stats(wnd):
    loop = asyncio.get_event_loop()
    futures = {}
    t0 = time.time()
    with QThreadExecutor(35) as executor:
        # prepare future objects and associate it with players db objects
        for player in wnd.players:
            url = "https://survarium.pro/api/v2/players/%s/stats" % player.name
            params = {'limit': 50, 'skip': 0}
            future = loop.run_in_executor(executor, send_request, url, params)
            futures[future] = player
        # iter by future objects and read responses
        for future in futures.keys():
            player = futures[future]
            try:
                response = await future
                print(player, response["total"])
            except requests.exceptions.ConnectionError:
                QMessageBox.about(wnd.form, "Ошибка соединения", "Не удалось установить соединение с survarium.pro")
                break
    elapsed = time.time() - t0
    print("Elapses: %.3f" % elapsed)

def send_request(url, params):
    response = requests.get(url, params=params)
    return response.json()