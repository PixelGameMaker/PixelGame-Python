# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'You_Lose.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(720, 270)
        Form.setMinimumSize(QSize(720, 270))
        Form.setMaximumSize(QSize(720, 270))
        font = QFont()
        font.setFamily(u"Unifont")
        font.setPointSize(22)
        Form.setFont(font)
        icon = QIcon()
        icon.addFile(u"Launcher Asset/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 10, 321, 71))
        font1 = QFont()
        font1.setFamily(u"Unifont")
        font1.setPointSize(32)
        self.label.setFont(font1)
        self.label.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 110, 720, 151))
        self.label_2.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamily(u"Unifont")
        font2.setPointSize(26)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Game Over", None))
        self.label.setText(
            QCoreApplication.translate("Form", u"<html><head/><body><p>Game Over</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Textlabel", None))
    # retranslateUi
