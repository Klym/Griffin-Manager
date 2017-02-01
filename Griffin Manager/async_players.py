# -*- coding: utf-8 -*-

import asyncio
import aiohttp

from PyQt5.QtWidgets import QMessageBox

async def get_players(wnd):
    # send two request to get two pages of players
    to_do = [get_page({'limit': 50, 'skip': 0}), get_page({'limit': 50, 'skip': 50})]
    futures = asyncio.as_completed(to_do)
    isExcept = False # if the exception was raisen show window once
    players = []
    
    # iter future objects and sum results to list
    for future in futures:
        try:
            response = await future
            players += response['data']
        except Exception as ex:
            if not isExcept:
                QMessageBox.about(wnd.form, "Ошибка соединения", ex.args[0])
                isExcept = True
    return players

async def get_page(params):
    async with aiohttp.ClientSession() as asession:
        try:
            async with asession.get("https://survarium.pro/api/v2/clans/Грифон/players/", params=params) as resp:
                result = await resp.json()
        except aiohttp.ClientOSError:
            raise Exception('Не удалось установить соединение с survarium.pro')
    return result