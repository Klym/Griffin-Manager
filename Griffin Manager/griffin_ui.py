# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'griffin.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main_Form(object):
    def setupUi(self, Main_Form):
        Main_Form.setObjectName("Main_Form")
        Main_Form.resize(637, 498)
        Main_Form.setMinimumSize(QtCore.QSize(637, 498))
        Main_Form.setMaximumSize(QtCore.QSize(637, 498))
        self.groupBox = QtWidgets.QGroupBox(Main_Form)
        self.groupBox.setGeometry(QtCore.QRect(240, 10, 391, 361))
        self.groupBox.setObjectName("groupBox")
        self.sostavList = QtWidgets.QTreeWidget(self.groupBox)
        self.sostavList.setGeometry(QtCore.QRect(0, 20, 391, 341))
        self.sostavList.setObjectName("sostavList")
        self.sostavList.headerItem().setText(0, "2")
        self.groupBox_2 = QtWidgets.QGroupBox(Main_Form)
        self.groupBox_2.setGeometry(QtCore.QRect(240, 380, 391, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.saveButton = QtWidgets.QPushButton(self.groupBox_2)
        self.saveButton.setGeometry(QtCore.QRect(20, 30, 91, 31))
        self.saveButton.setObjectName("saveButton")
        self.updateButton = QtWidgets.QPushButton(self.groupBox_2)
        self.updateButton.setGeometry(QtCore.QRect(150, 30, 91, 31))
        self.updateButton.setObjectName("updateButton")
        self.exitButton = QtWidgets.QPushButton(self.groupBox_2)
        self.exitButton.setGeometry(QtCore.QRect(280, 30, 91, 31))
        self.exitButton.setObjectName("exitButton")
        self.groupBox_3 = QtWidgets.QGroupBox(Main_Form)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 221, 361))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(10, 20, 51, 21))
        self.label.setObjectName("label")
        self.rank = QtWidgets.QComboBox(self.groupBox_3)
        self.rank.setGeometry(QtCore.QRect(60, 20, 151, 22))
        self.rank.setObjectName("rank")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 47, 21))
        self.label_2.setObjectName("label_2")
        self.scores = QtWidgets.QLineEdit(self.groupBox_3)
        self.scores.setGeometry(QtCore.QRect(60, 60, 81, 20))
        self.scores.setText("")
        self.scores.setObjectName("scores")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 47, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 190, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(10, 220, 47, 13))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 250, 71, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(10, 280, 71, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(10, 310, 71, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(10, 335, 51, 21))
        self.label_12.setObjectName("label_12")
        self.exp = QtWidgets.QLabel(self.groupBox_3)
        self.exp.setGeometry(QtCore.QRect(80, 100, 81, 16))
        self.exp.setObjectName("exp")
        self.kills = QtWidgets.QLabel(self.groupBox_3)
        self.kills.setGeometry(QtCore.QRect(80, 126, 81, 20))
        self.kills.setObjectName("kills")
        self.dies = QtWidgets.QLabel(self.groupBox_3)
        self.dies.setGeometry(QtCore.QRect(80, 156, 111, 20))
        self.dies.setObjectName("dies")
        self.kd = QtWidgets.QLabel(self.groupBox_3)
        self.kd.setGeometry(QtCore.QRect(80, 190, 47, 13))
        self.kd.setObjectName("kd")
        self.victories = QtWidgets.QLabel(self.groupBox_3)
        self.victories.setGeometry(QtCore.QRect(80, 216, 91, 20))
        self.victories.setObjectName("victories")
        self.fails = QtWidgets.QLabel(self.groupBox_3)
        self.fails.setGeometry(QtCore.QRect(80, 250, 71, 16))
        self.fails.setObjectName("fails")
        self.matches = QtWidgets.QLabel(self.groupBox_3)
        self.matches.setGeometry(QtCore.QRect(80, 280, 71, 16))
        self.matches.setObjectName("matches")
        self.winrate = QtWidgets.QLabel(self.groupBox_3)
        self.winrate.setGeometry(QtCore.QRect(80, 310, 71, 16))
        self.winrate.setObjectName("winrate")
        self.avgExp = QtWidgets.QLabel(self.groupBox_3)
        self.avgExp.setGeometry(QtCore.QRect(80, 335, 71, 21))
        self.avgExp.setObjectName("avgExp")
        self.groupBox_4 = QtWidgets.QGroupBox(Main_Form)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 380, 221, 80))
        self.groupBox_4.setObjectName("groupBox_4")
        self.scoresAdd = QtWidgets.QLineEdit(self.groupBox_4)
        self.scoresAdd.setGeometry(QtCore.QRect(10, 20, 111, 20))
        self.scoresAdd.setObjectName("scoresAdd")
        self.plusScoresButton = QtWidgets.QPushButton(self.groupBox_4)
        self.plusScoresButton.setGeometry(QtCore.QRect(10, 50, 51, 23))
        self.plusScoresButton.setObjectName("plusScoresButton")
        self.plusScoresButton_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.plusScoresButton_2.setGeometry(QtCore.QRect(70, 50, 51, 23))
        self.plusScoresButton_2.setObjectName("plusScoresButton_2")
        self.saveScoresButton = QtWidgets.QPushButton(self.groupBox_4)
        self.saveScoresButton.setGeometry(QtCore.QRect(130, 20, 81, 23))
        self.saveScoresButton.setObjectName("saveScoresButton")
        self.cancelScoresButton = QtWidgets.QPushButton(self.groupBox_4)
        self.cancelScoresButton.setGeometry(QtCore.QRect(130, 50, 81, 23))
        self.cancelScoresButton.setObjectName("cancelScoresButton")
        self.groupBox.raise_()
        self.groupBox_3.raise_()
        self.groupBox_4.raise_()
        self.groupBox_2.raise_()

        self.retranslateUi(Main_Form)
        self.exitButton.clicked.connect(Main_Form.close)
        # new slots
        self.sostavList.itemSelectionChanged.connect(self.update_info)
        self.rank.currentTextChanged.connect(self.change_rank)
        self.scores.textEdited.connect(self.change_score)
        self.saveScoresButton.clicked.connect(self.save)
        self.cancelScoresButton.clicked.connect(self.cancel)
        QtCore.QMetaObject.connectSlotsByName(Main_Form)

    def retranslateUi(self, Main_Form):
        _translate = QtCore.QCoreApplication.translate
        Main_Form.setWindowTitle(_translate("Main_Form", "Griffin Manager"))
        self.groupBox.setTitle(_translate("Main_Form", "Состав"))
        self.groupBox_2.setTitle(_translate("Main_Form", "Действия"))
        self.saveButton.setText(_translate("Main_Form", "Сохранить"))
        self.updateButton.setText(_translate("Main_Form", "Обновить"))
        self.exitButton.setText(_translate("Main_Form", "Выход"))
        self.groupBox_3.setTitle(_translate("Main_Form", "Информация"))
        self.label.setText(_translate("Main_Form", "Звание:"))
        self.label_2.setText(_translate("Main_Form", "Очки:"))
        self.label_4.setText(_translate("Main_Form", "Опыт:"))
        self.label_5.setText(_translate("Main_Form", "Убийств:"))
        self.label_6.setText(_translate("Main_Form", "Смертей:"))
        self.label_7.setText(_translate("Main_Form", "У/C:"))
        self.label_8.setText(_translate("Main_Form", "Побед:"))
        self.label_9.setText(_translate("Main_Form", "Поражений:"))
        self.label_10.setText(_translate("Main_Form", "Матчей:"))
        self.label_11.setText(_translate("Main_Form", "Винрейт:"))
        self.label_12.setText(_translate("Main_Form", "Ср. счет:"))
        self.exp.setText(_translate("Main_Form", "701419"))
        self.kills.setText(_translate("Main_Form", "23570"))
        self.dies.setText(_translate("Main_Form", "22827"))
        self.kd.setText(_translate("Main_Form", "1.03"))
        self.victories.setText(_translate("Main_Form", "984"))
        self.fails.setText(_translate("Main_Form", "1061"))
        self.matches.setText(_translate("Main_Form", "2045"))
        self.winrate.setText(_translate("Main_Form", "48.12%"))
        self.avgExp.setText(_translate("Main_Form", "20"))
        self.groupBox_4.setTitle(_translate("Main_Form", "Очки"))
        self.plusScoresButton.setText(_translate("Main_Form", "+"))
        self.plusScoresButton_2.setText(_translate("Main_Form", "-"))
        self.saveScoresButton.setText(_translate("Main_Form", "Ок"))
        self.cancelScoresButton.setText(_translate("Main_Form", "Отмена"))

