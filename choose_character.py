# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\choose_character.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(720, 500)
        Form.setMinimumSize(QSize(720, 500))
        Form.setMaximumSize(QSize(720, 500))
        font = QFont()
        font.setFamily("Unifont")
        font.setPointSize(13)
        Form.setFont(font)
        icon = QIcon()
        icon.addFile("Launcher Asset/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setGeometry(QRect(10, 40, 701, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.c1 = QLabel(self.gridLayoutWidget)
        self.c1.setObjectName("c1")
        self.c1.setPixmap(QPixmap("Launcher Asset/archer_standf a.png"))
        # self.c1.setScaledContents(True)
        self.c1.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.c1, 1, 0, 1, 1)
        self.c2 = QLabel(self.gridLayoutWidget)
        self.c2.setObjectName("c2")
        self.c2.setPixmap(QPixmap("Launcher Asset/knight_standf a.png"))
        # self.c2.setScaledContents(True)
        self.c2.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.c2, 1, 1, 1, 1)
        self.cc1 = QPushButton(self.gridLayoutWidget)
        font = QFont()
        font.setPointSize(11)
        self.cc1.setFont(font)
        self.cc1.setObjectName("cc1")
        self.gridLayout.addWidget(self.cc1, 2, 0, 1, 1)
        self.cc2 = QPushButton(self.gridLayoutWidget)
        font = QFont()
        font.setPointSize(11)
        self.cc2.setFont(font)
        self.cc2.setObjectName("cc2")
        self.gridLayout.addWidget(self.cc2, 2, 1, 1, 1)
        self.play = QPushButton(Form)
        self.play.setGeometry(QRect(490, 400, 221, 91))
        font = QFont()
        font.setPointSize(25)
        self.play.setFont(font)
        self.play.setObjectName("play")
        self.gridLayoutWidget_2 = QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QRect(10, 230, 701, 161))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.c3 = QLabel(self.gridLayoutWidget_2)
        self.c3.setObjectName("c3")
        self.c3.setPixmap(QPixmap("Launcher Asset/magician_standf a.png"))
        # self.c3.setScaledContents(True)
        self.c3.setAlignment(Qt.AlignCenter)
        self.gridLayout_2.addWidget(self.c3, 0, 0, 1, 1)
        self.c4 = QLabel(self.gridLayoutWidget_2)
        self.c4.setObjectName("c4")
        self.c4.setPixmap(QPixmap("Launcher Asset/assassin_standf a.png"))
        # self.c4.setScaledContents(True)
        self.c4.setAlignment(Qt.AlignCenter)
        self.gridLayout_2.addWidget(self.c4, 0, 1, 1, 1)
        self.cc3 = QPushButton(self.gridLayoutWidget_2)
        font = QFont()
        font.setPointSize(11)
        self.cc3.setFont(font)
        self.cc3.setObjectName("cc3")
        self.gridLayout_2.addWidget(self.cc3, 1, 0, 1, 1)
        self.cc4 = QPushButton(self.gridLayoutWidget_2)
        font = QFont()
        font.setPointSize(11)
        self.cc4.setFont(font)
        self.cc4.setObjectName("cc4")
        self.gridLayout_2.addWidget(self.cc4, 1, 1, 1, 1)
        self.Archer = QLabel(Form)
        self.Archer.setGeometry(QRect(10, 20, 347, 20))
        font = QFont()
        font.setPointSize(13)
        self.Archer.setFont(font)
        self.Archer.setObjectName("Archer")
        self.Knight = QLabel(Form)
        self.Knight.setGeometry(QRect(363, 20, 346, 20))
        font = QFont()
        font.setPointSize(13)
        self.Knight.setFont(font)
        self.Knight.setObjectName("Knight")
        self.Magician = QLabel(Form)
        self.Magician.setGeometry(QRect(10, 210, 347, 20))
        font = QFont()
        font.setPointSize(13)
        self.Magician.setFont(font)
        self.Magician.setObjectName("Magician")
        self.Assassin = QLabel(Form)
        self.Assassin.setGeometry(QRect(363, 210, 347, 20))
        self.Assassin.setObjectName("Assassin")
        self.now_choose = QLabel(Form)
        self.now_choose.setGeometry(QRect(10, 415, 450, 51))
        font = QFont()
        font.setPointSize(19)
        self.now_choose.setFont(font)
        self.now_choose.setObjectName("now_choose")

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Class Select"))
        # self.c1.setText(_translate("Form", "TextLabel"))
        # self.c2.setText(_translate("Form", "TextLabel"))
        self.cc1.setText(_translate("Form", "Choose this"))
        self.cc2.setText(_translate("Form", "Choose this"))
        self.play.setText(_translate("Form", "Play"))
        # self.c3.setText(_translate("Form", "TextLabel"))
        # self.c4.setText(_translate("Form", "TextLabel"))
        self.cc3.setText(_translate("Form", "Choose this"))
        self.cc4.setText(_translate("Form", "Choose this"))
        self.Archer.setText(_translate("Form", "Archer"))
        self.Knight.setText(_translate("Form", "Knight"))
        self.Magician.setText(_translate("Form", "Magician"))
        self.Assassin.setText(_translate("Form", "Assassin"))
        # self.now_choose.setText(_translate("Form", "TextLabel"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
