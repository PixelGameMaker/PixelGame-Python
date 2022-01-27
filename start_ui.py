# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\start.ui',
# licensing of '.\start.ui' applies.
#
# Created: Thu Jan 27 12:33:13 2022
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        Form.setMinimumSize(QtCore.QSize(640, 480))
        Form.setMaximumSize(QtCore.QSize(640, 480))
        self.text = QtWidgets.QLabel(Form)
        self.text.setGeometry(QtCore.QRect(90, 50, 461, 101))
        font = QtGui.QFont()
        font.setFamily("Unifont")
        font.setPointSize(18)
        self.text.setFont(font)
        self.text.setObjectName("text")
        self.play1 = QtWidgets.QPushButton(Form)
        self.play1.setGeometry(QtCore.QRect(20, 310, 281, 131))
        font = QtGui.QFont()
        font.setFamily("Unifont")
        font.setPointSize(18)
        self.play1.setFont(font)
        self.play1.setObjectName("play1")
        self.play2 = QtWidgets.QPushButton(Form)
        self.play2.setGeometry(QtCore.QRect(340, 310, 281, 131))
        font = QtGui.QFont()
        font.setFamily("Unifont")
        font.setPointSize(18)
        self.play2.setFont(font)
        self.play2.setObjectName("play2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.text.setText(QtWidgets.QApplication.translate("Form", "TextLabel", None, -1))
        self.play1.setText(QtWidgets.QApplication.translate("Form", "Yes,let me continue.", None, -1))
        self.play2.setText(QtWidgets.QApplication.translate("Form", "No,let me \n"
        "start from beginning.", None, -1))

