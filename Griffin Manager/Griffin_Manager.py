# -*- coding: utf-8 -*-

import sys
import asyncio
import sqlalchemy

from quamash import QEventLoop
from sqlalchemy.orm import sessionmaker
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QStatusBar, QMessageBox, QFileDialog
from PyQt5.QtGui import QClipboard
from PyQt5.QtCore import QTimer

from griffin_ui import Ui_Main_Form
from griffin_db import Player, Rank

class MainForm(Ui_Main_Form):
    def __init__(self, form):
        self.form = form
        self.setupUi(form)
        
        # set status bar
        self.statusBar = QStatusBar()
        form.setStatusBar(self.statusBar)

        # set checked flags of export settings
        self.fileRadio.setChecked(True)
        self.scoresCheckBox.setChecked(True)
        self.rankCheckBox.setChecked(True)
        self.levelCheckBox.setChecked(True)

        # set header of list
        header = QTreeWidgetItem(["Позывной", "Очки", "Звание", "Уровень"])
        self.sostavList.setHeaderItem(header)
        self.sostavList.header().resizeSection(0, 120)
        self.sostavList.header().resizeSection(1, 70)
        self.sostavList.header().resizeSection(2, 120)
        self.sostavList.header().resizeSection(3, 40)

        # select and bind data
        self.select_data()
        self.ready()
        self.fill_data()

    def ready(self):
        self.statusBar.showMessage("Игроков: %d" % len(self.players))

    def select_data(self):
        # select players
        self.players = [p for p in session.query(Player).order_by(Player.scores.desc()).all()]
            
        # select and bind ranks
        self.ranks = []
        for rank in session.query(Rank).order_by(Rank.scores).all():
            self.ranks.append(rank)
            self.rank.addItem(rank.name)

    def fill_data(self):
        # clear list, sort players by scores and fill
        self.sostavList.clear()
        self.players.sort(key=lambda x: x.scores, reverse=True)
        for player in self.players:
            QTreeWidgetItem(self.sostavList, [player.name, '%.2f' % player.scores, player.rank.name, '%s' % player.level])

        # set first item selected
        self.sostavList.setCurrentItem(self.sostavList.topLevelItem(0))


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
        self.lastUpdate.setText(p.last_update.strftime("%d.%m.%Y %H:%M:%S"))

    def change_rank(self):
        # get selected player's and rank's objects
        p_index = self.sostavList.currentIndex().row()
        r_index = self.rank.currentIndex()
        p = self.players[p_index]
        r = self.ranks[r_index]

        # ignore on scores changed event and on first binding
        if p.rank.name == r.name or p_index == -1:
            return

        # update model and ui
        p.rank = r
        p.scores = r.scores
        self.scores.setText('%.2f' % r.scores)
        self.sostavList.currentItem().setText(1, '%.2f' % r.scores)
        self.sostavList.currentItem().setText(2, r.name)

    def change_score(self):
        # if scores is empty set zero
        scores = self.scores.text()
        if scores == "":
            scores = 0
            self.scores.setText("0.00")

        # raise exception if value is not float or gt max scores
        try:                
            scores = float(scores)
            max = self.ranks[-1].scores
            if scores > max:
                raise Exception("Значение очков не может превышать %d" % max)
            if scores < 0:
                raise Exception("Значение очков не может быть отрицательным")
        except ValueError:
            QMessageBox.about(self.form, "Ошибка ввода", "Значение очков должно быть числом")
            return
        except Exception as ex:
            QMessageBox.about(self.form, "Ошибка ввода", ex.args[0])
            return
        
        # get selected player's object and new scores
        p_index = self.sostavList.currentIndex().row()
        p = self.players[p_index]

        # update player's scores
        p.scores = scores
        self.sostavList.currentItem().setText(1, '%.2f' % scores)

        # detect new rank
        current_rank = None
        for rank in self.ranks:
            if scores >= rank.scores:
                current_rank = rank
            else:
                break

        # update player's rank
        p.rank = current_rank
        self.rank.setCurrentText(p.rank.name)
        self.sostavList.currentItem().setText(2, p.rank.name)    

    def change_add_score(self):
        # if scores is empty set zero
        scores = self.scoresAdd.text()
        if scores == "":
            scores = 0
            self.scoresAdd.setText("0")

    def plus_minus_scores(self, func):
        # raise exception if value is not float
        try:                
            scores = float(self.scoresAdd.text())
        except ValueError:
            QMessageBox.about(self.form, "Ошибка ввода", "Значение очков должно быть числом")
        else:
            # sum scores and emit text changed event
            newScores = func(float(self.scores.text()), scores)
            self.scores.setText('%.2f' % newScores)
            self.change_score()

    def add_scores(self):
        self.plus_minus_scores(lambda x, y: x + y)

    def sub_scores(self):
        self.plus_minus_scores(lambda x, y: x - y)

    def save(self):
        # save all changes and inform user about it
        session.commit()
        self.statusBar.showMessage("Изменения сохранены")
        QTimer.singleShot(3000, self.ready)

    def cancel(self):
        # cancel all changes
        session.rollback()
        self.fill_data()

    def export(self):
        # export data to file or clipboard
        if self.fileRadio.isChecked():
            self.export_to_file()
        else:
            self.export_to_clipboard()

    def generate_export_data(self):
        # generate export format
        fmt = '{num}. {name} -'
        if self.scoresCheckBox.isChecked():
            fmt += ' {scores:.2f}'
        if self.rankCheckBox.isChecked():
            fmt +=  ' {rank}.'
        if self.levelCheckBox.isChecked():
            fmt += ' ({level})'
        if fmt[-1] == '-':
            fmt = fmt[:-2]

        # yield formatted string
        for i, player in enumerate(self.players):
            yield fmt.format(num=(i+1), name=player.name, scores=player.scores, rank=player.rank.name, level=player.level)

    def export_to_clipboard(self):
        # generate formatted text and copy to clipboard
        text = '\n'.join(w_str for w_str in self.generate_export_data())
        QClipboard.setText(QApplication.clipboard(), text)

        # inform user in status bar
        self.statusBar.showMessage("Скопировано в буфер обмена.")
        QTimer.singleShot(4000, self.ready)

    def export_to_file(self):
        # select path to export
        path = QFileDialog.getSaveFileName(self.form, 'Выберите файл', '', 'Text File (*.txt)')
        if path[0] == '':
            return       
        # write data to selected file
        with open(path[0], 'w') as file:
            for w_str in self.generate_export_data():
                file.write(w_str + '\n')
        # inform user in status bar
        self.statusBar.showMessage("Сохранено: " + path[0])
        QTimer.singleShot(4000, self.ready)

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