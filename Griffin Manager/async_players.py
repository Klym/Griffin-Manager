# -*- coding: utf-8 -*-

import asyncio
import requests

from quamash import QEventLoop, QThreadExecutor
from PyQt5.QtWidgets import QMessageBox

async def get_players(wnd):
    # send two request to get two pages of players
    loop = asyncio.get_event_loop()
    url = "https://survarium.pro/api/v2/clans/Грифон/players/"
    to_do = [(url, {'limit': 50, 'skip': 0}), (url, {'limit': 50, 'skip': 50})]
    players = []
    with QThreadExecutor(2) as executor:        
        for params in to_do:
            future = loop.run_in_executor(executor, send_request, *params)
            try:
                response = await future
                players += response['data']
            except requests.exceptions.ConnectionError:
                QMessageBox.about(wnd.form, "Ошибка соединения", "Не удалось установить соединение с survarium.pro")
                break
    return players

def send_request(url, params):
    response = requests.get(url, params=params)
    return response.json()