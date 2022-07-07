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
            Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(720, 480)
        Form.setMinimumSize(QSize(720, 480))
        Form.setMaximumSize(QSize(720, 480))
        font = QFont()
        font.setFamily("Unifont")
        font.setPointSize(22)
        Form.setFont(font)
        icon = QIcon()
        icon.addFile("Launcher Asset/Logo_Died.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label = QLabel(Form)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(200, 10, 321, 71))
        font1 = QFont()
        font1.setFamily("Unifont")
        font1.setPointSize(18)
        self.label.setFont(font1)
        self.label.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QTextBrowser(Form)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(10, 100, 701, 371))
        font2 = QFont()
        font2.setFamily("Unifont")
        font2.setPointSize(12)
        self.label_2.setFont(font2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Game Error", None))
        self.label.setText(
            QCoreApplication.translate(
                "Form",
                "<html><head/><body><p>Unknown Error Occurred</p><p>Please Report to Developer</p></body></html>",
                None,
            )
        )
        self.label_2.setText(QCoreApplication.translate("Form", "TextLabel", None))

    # retranslateUi
