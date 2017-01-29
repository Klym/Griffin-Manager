# -*- coding: utf-8 -*-

import sys
import asyncio
import sqlalchemy

from quamash import QEventLoop
from sqlalchemy.orm import sessionmaker
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QStatusBar

from griffin_ui import Ui_Main_Form
from griffin_db import Player, Rank

class MainForm(Ui_Main_Form):
    def __init__(self, form):
        self.setupUi(form)
        
        # set status bar
        self.statusBar = QStatusBar()
        self.statusBar.showMessage("Готово")
        form.setStatusBar(self.statusBar)

        # set header of list
        header = QTreeWidgetItem(["Позывной", "Очки", "Звание", "Уровень"])
        self.sostavList.setHeaderItem(header)
        self.sostavList.header().resizeSection(0, 120)
        self.sostavList.header().resizeSection(1, 70)
        self.sostavList.header().resizeSection(2, 120)
        self.sostavList.header().resizeSection(3, 40)

        self.select_data()
        
        # set first item selected
        self.sostavList.setCurrentItem(self.sostavList.topLevelItem(0))

    def select_data(self):
        # select and bind players
        self.players = []
        for player in session.query(Player).order_by(Player.scores.desc()).all():
            self.players.append(player)
            QTreeWidgetItem(self.sostavList, [player.name, '%.2f' % player.scores, player.rank.name, '%s' % player.level])

        # select and bind ranks
        self.ranks = []
        for rank in session.query(Rank).order_by(Rank.scores).all():
            self.ranks.append(rank)
            self.rank.addItem(rank.name)

    def update_info(self):
        # get selected player's object
        index = self.sostavList.currentIndex().row()
        p = self.players[index]

        # update group box, line edit and labels
        self.rank.setCurrentText(p.rank.name)
        self.scores.setText('%.2f' % p.scores)
        self.exp.setText('%d' % p.experience)
        self.kills.setText('%d' % p.kills)
        self.dies.setText('%d' % p.dies)
        self.kd.setText('%.2f' % p.kd)
        self.victories.setText('%d' % p.victories)
        self.fails.setText('%d' % (p.matches - p.victories))
        self.matches.setText('%d' % p.matches)
        self.winrate.setText(('%.1f' % p.winrate) + '%')
        self.avgExp.setText('%d' % p.avg_stat)

    def change_rank(self):
        p_index = self.sostavList.currentIndex().row()
        r_index = self.rank.currentIndex()
        p = self.players[p_index]
        r = self.ranks[r_index]

        if p.rank.name == r.name or p_index == -1:
            return
        print(True)
        p.rank = r
        p.scores = r.scores
        self.scores.setText('%.2f' % r.scores)

    def change_score(self):
        p_index = self.sostavList.currentIndex().row()
        p = self.players[p_index]
        scores = float(self.scores.text())
        p.scores = scores
        current_rank = None
        for rank in self.ranks:
            if scores >= rank.scores:
                current_rank = rank
            else:
                break
        p.rank = current_rank
        self.rank.setCurrentText(p.rank.name)

if __name__ == "__main__":
    engine = sqlalchemy.create_engine("sqlite:///griffin.db")
    Session = sessionmaker(bind=engine)
    session = Session()
    
    app = QApplication(sys.argv)
    with QEventLoop(app) as loop:
        asyncio.set_event_loop(loop)
        window = QMainWindow()
        ui = MainForm(window)
        window.show()
        loop.run_forever()
    session.close()