# -*- coding: utf-8 -*-

import sys
import asyncio
from quamash import QEventLoop
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QStatusBar

from griffinUI import Ui_Main_Form

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
        QTreeWidgetItem(self.sostavList, ["Лескон", "11000", "Мастер", "65"])
        QTreeWidgetItem(self.sostavList, ["Клым", "10235", "Хранитель", "78"])
        QTreeWidgetItem(self.sostavList, ["Солярис", "2125", "Матерый", "68"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    with QEventLoop(app) as loop:
        asyncio.set_event_loop(loop)
        window = QMainWindow()
        ui = MainForm(window)
        window.show()
        loop.run_forever()