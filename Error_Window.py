# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Error_Window.ui'
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
        Form.resize(640, 480)
        Form.setMinimumSize(QSize(640, 480))
        Form.setMaximumSize(QSize(640, 480))
        font = QFont()
        font.setFamily(u"Unifont")
        font.setPointSize(22)
        Form.setFont(font)
        Form.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 10, 271, 71))
        font1 = QFont()
        font1.setFamily(u"Unifont")
        font1.setPointSize(18)
        self.label.setFont(font1)
        self.label.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 110, 621, 361))
        font2 = QFont()
        font2.setFamily(u"Unifont")
        font2.setPointSize(9)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Error Report", None))
        self.label.setText(QCoreApplication.translate("Form", u"Unknown Error Occurred", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi
