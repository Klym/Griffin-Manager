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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("griffin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main_Form.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(Main_Form)
        self.groupBox.setGeometry(QtCore.QRect(240, 10, 391, 361))
        self.groupBox.setObjectName("groupBox")
        self.sostavList = QtWidgets.QTreeWidget(self.groupBox)
        self.sostavList.setGeometry(QtCore.QRect(0, 20, 391, 341))
        self.sostavList.setObjectName("sostavList")
        self.sostavList.headerItem().setText(0, "1")
        self.groupBox_2 = QtWidgets.QGroupBox(Main_Form)
        self.groupBox_2.setGeometry(QtCore.QRect(240, 380, 391, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.saveButton = QtWidgets.QPushButton(self.groupBox_2)
        self.saveButton.setGeometry(QtCore.QRect(10, 30, 81, 31))
        self.saveButton.setObjectName("saveButton")
        self.updateButton = QtWidgets.QPushButton(self.groupBox_2)
        self.updateButton.setGeometry(QtCore.QRect(110, 30, 81, 31))
        self.updateButton.setObjectName("updateButton")
        self.exitButton = QtWidgets.QPushButton(self.groupBox_2)
        self.exitButton.setGeometry(QtCore.QRect(300, 30, 81, 31))
        self.exitButton.setObjectName("exitButton")
        self.sortButton = QtWidgets.QPushButton(self.groupBox_2)
        self.sortButton.setGeometry(QtCore.QRect(200, 30, 81, 31))
        self.sortButton.setObjectName("sortButton")
        self.groupBox_3 = QtWidgets.QGroupBox(Main_Form)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 221, 271))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(10, 20, 51, 21))
        self.label.setObjectName("label")
        self.rank = QtWidgets.QComboBox(self.groupBox_3)
        self.rank.setGeometry(QtCore.QRect(60, 20, 151, 22))
        self.rank.setObjectName("rank")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 47, 21))
        self.label_2.setObjectName("label_2")
        self.scores = QtWidgets.QLineEdit(self.groupBox_3)
        self.scores.setGeometry(QtCore.QRect(60, 50, 81, 20))
        self.scores.setText("")
        self.scores.setObjectName("scores")
        self.widget = QtWidgets.QWidget(self.groupBox_3)
        self.widget.setGeometry(QtCore.QRect(10, 80, 201, 191))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.exp = QtWidgets.QLabel(self.widget)
        self.exp.setObjectName("exp")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.exp)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.kills = QtWidgets.QLabel(self.widget)
        self.kills.setObjectName("kills")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.kills)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.dies = QtWidgets.QLabel(self.widget)
        self.dies.setObjectName("dies")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dies)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.kd = QtWidgets.QLabel(self.widget)
        self.kd.setObjectName("kd")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.kd)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.victories = QtWidgets.QLabel(self.widget)
        self.victories.setObjectName("victories")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.victories)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.fails = QtWidgets.QLabel(self.widget)
        self.fails.setObjectName("fails")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.fails)
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.matches = QtWidgets.QLabel(self.widget)
        self.matches.setObjectName("matches")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.matches)
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.winrate = QtWidgets.QLabel(self.widget)
        self.winrate.setObjectName("winrate")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.winrate)
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.avgExp = QtWidgets.QLabel(self.widget)
        self.avgExp.setObjectName("avgExp")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.avgExp)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lastUpdate = QtWidgets.QLabel(self.widget)
        self.lastUpdate.setObjectName("lastUpdate")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lastUpdate)
        self.groupBox_4 = QtWidgets.QGroupBox(Main_Form)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 290, 221, 81))
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
        self.groupBox_5 = QtWidgets.QGroupBox(Main_Form)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 380, 221, 81))
        self.groupBox_5.setObjectName("groupBox_5")
        self.rankCheckBox = QtWidgets.QCheckBox(self.groupBox_5)
        self.rankCheckBox.setGeometry(QtCore.QRect(100, 40, 70, 17))
        self.rankCheckBox.setObjectName("rankCheckBox")
        self.scoresCheckBox = QtWidgets.QCheckBox(self.groupBox_5)
        self.scoresCheckBox.setGeometry(QtCore.QRect(100, 20, 70, 17))
        self.scoresCheckBox.setTristate(False)
        self.scoresCheckBox.setObjectName("scoresCheckBox")
        self.levelCheckBox = QtWidgets.QCheckBox(self.groupBox_5)
        self.levelCheckBox.setGeometry(QtCore.QRect(100, 60, 70, 17))
        self.levelCheckBox.setObjectName("levelCheckBox")
        self.fileRadio = QtWidgets.QRadioButton(self.groupBox_5)
        self.fileRadio.setGeometry(QtCore.QRect(20, 20, 82, 17))
        self.fileRadio.setObjectName("fileRadio")
        self.buffRadio = QtWidgets.QRadioButton(self.groupBox_5)
        self.buffRadio.setGeometry(QtCore.QRect(20, 40, 82, 17))
        self.buffRadio.setObjectName("buffRadio")
        self.groupBox.raise_()
        self.groupBox_3.raise_()
        self.groupBox_4.raise_()
        self.groupBox_2.raise_()
        self.groupBox_5.raise_()

        self.retranslateUi(Main_Form)
        self.exitButton.clicked.connect(Main_Form.close)
        # new slots
        self.sostavList.itemSelectionChanged.connect(self.update_info)
        self.rank.currentTextChanged.connect(self.change_rank)
        self.scores.textEdited.connect(self.change_score)
        self.scoresAdd.textEdited.connect(self.change_add_score)
        self.plusScoresButton.clicked.connect(self.add_scores)
        self.plusScoresButton_2.clicked.connect(self.sub_scores)
        self.saveScoresButton.clicked.connect(self.save)
        self.cancelScoresButton.clicked.connect(self.cancel)
        self.saveButton.clicked.connect(self.export)
        self.sortButton.clicked.connect(self.fill_data)
        QtCore.QMetaObject.connectSlotsByName(Main_Form)

    def retranslateUi(self, Main_Form):
        _translate = QtCore.QCoreApplication.translate
        Main_Form.setWindowTitle(_translate("Main_Form", "Griffin Manager"))
        self.groupBox.setTitle(_translate("Main_Form", "Состав"))
        self.groupBox_2.setTitle(_translate("Main_Form", "Действия"))
        self.saveButton.setText(_translate("Main_Form", "Экспорт"))
        self.updateButton.setText(_translate("Main_Form", "Обновить"))
        self.exitButton.setText(_translate("Main_Form", "Выход"))
        self.sortButton.setText(_translate("Main_Form", "Сортировать"))
        self.groupBox_3.setTitle(_translate("Main_Form", "Информация"))
        self.label.setText(_translate("Main_Form", "Звание:"))
        self.label_2.setText(_translate("Main_Form", "Очки:"))
        self.label_4.setText(_translate("Main_Form", "Опыт:"))
        self.exp.setText(_translate("Main_Form", "701419"))
        self.label_5.setText(_translate("Main_Form", "Убийств:"))
        self.kills.setText(_translate("Main_Form", "23570"))
        self.label_6.setText(_translate("Main_Form", "Смертей:"))
        self.dies.setText(_translate("Main_Form", "22827"))
        self.label_7.setText(_translate("Main_Form", "У/C:"))
        self.kd.setText(_translate("Main_Form", "1.03"))
        self.label_8.setText(_translate("Main_Form", "Побед:"))
        self.victories.setText(_translate("Main_Form", "984"))
        self.label_9.setText(_translate("Main_Form", "Поражений:"))
        self.fails.setText(_translate("Main_Form", "1061"))
        self.label_10.setText(_translate("Main_Form", "Матчей:"))
        self.matches.setText(_translate("Main_Form", "2045"))
        self.label_11.setText(_translate("Main_Form", "Винрейт:"))
        self.winrate.setText(_translate("Main_Form", "48.12%"))
        self.label_12.setText(_translate("Main_Form", "Ср. счет:"))
        self.avgExp.setText(_translate("Main_Form", "20"))
        self.label_3.setText(_translate("Main_Form", "Заходил:"))
        self.lastUpdate.setText(_translate("Main_Form", "30.01.2017 03:08:16"))
        self.groupBox_4.setTitle(_translate("Main_Form", "Очки"))
        self.plusScoresButton.setText(_translate("Main_Form", "+"))
        self.plusScoresButton_2.setText(_translate("Main_Form", "-"))
        self.saveScoresButton.setText(_translate("Main_Form", "Сохранить"))
        self.cancelScoresButton.setText(_translate("Main_Form", "Отменить"))
        self.groupBox_5.setTitle(_translate("Main_Form", "Параметры экспорта"))
        self.rankCheckBox.setText(_translate("Main_Form", "Звание"))
        self.scoresCheckBox.setText(_translate("Main_Form", "Очки"))
        self.levelCheckBox.setText(_translate("Main_Form", "Уровень"))
        self.fileRadio.setText(_translate("Main_Form", "файл"))
        self.buffRadio.setText(_translate("Main_Form", "буфер"))

