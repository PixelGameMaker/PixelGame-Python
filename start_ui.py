# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start.ui'
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
        Form.resize(640, 480)
        Form.setMinimumSize(QSize(640, 480))
        Form.setMaximumSize(QSize(640, 480))
        Form.setWindowTitle(u"Game Save Choose")
        icon = QIcon()
        icon.addFile(u"Launcher Asset/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.text = QLabel(Form)
        self.text.setObjectName(u"text")
        self.text.setGeometry(QRect(90, 50, 461, 101))
        self.text.setAlignment(Qt.AlignCenter)
        self.play1 = QPushButton(Form)
        self.play1.setObjectName(u"play1")
        self.play1.setGeometry(QRect(20, 310, 281, 131))
        font = QFont()
        font.setFamily(u"Unifont")
        font.setPointSize(18)
        # font.setStyleStrategy(QFont.NoAntialias)
        self.text.setFont(font)
        self.play1.setFont(font)
        self.play2 = QPushButton(Form)
        self.play2.setObjectName(u"play2")
        self.play2.setGeometry(QRect(340, 310, 281, 131))
        self.play2.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        self.text.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.play1.setText(
            QCoreApplication.translate("Form", u"Yes,let me continue.", None)
        )
        self.play2.setText(
            QCoreApplication.translate(
                "Form", u"No,let me \n" "start from beginning.", None
            )
        )

    # retranslateUi
