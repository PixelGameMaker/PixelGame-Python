# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Launcher.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Main_Window(object):
    def setupUi(self, Main_Window):
        if not Main_Window.objectName():
            Main_Window.setObjectName(u"Main_Window")
        Main_Window.resize(720, 480)
        Main_Window.setMinimumSize(QSize(720, 480))
        Main_Window.setMaximumSize(QSize(720, 480))
        font = QFont()
        font.setFamily(u"Unifont")
        font.setPointSize(12)
        Main_Window.setFont(font)
        icon = QIcon()
        icon.addFile(u"../../../Pictures/icons/explorer_ICO_MYCOMPUTER.ico", QSize(), QIcon.Normal, QIcon.Off)
        Main_Window.setWindowIcon(icon)
        Main_Window.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.Play_Button = QPushButton(Main_Window)
        self.Play_Button.setObjectName(u"Play_Button")
        self.Play_Button.setEnabled(True)
        self.Play_Button.setGeometry(QRect(510, 380, 201, 91))
        font1 = QFont()
        font1.setFamily(u"Unifont")
        font1.setPointSize(40)
        font1.setKerning(True)
        self.Play_Button.setFont(font1)
        self.Play_Button.setCheckable(False)
        self.Background = QLabel(Main_Window)
        self.Background.setObjectName(u"Background")
        self.Background.setGeometry(QRect(10, 11, 701, 351))
        self.Background.setPixmap(QPixmap(u"../../../Pictures/31251762_p0.jpg"))
        self.Graphics_Settings = QGroupBox(Main_Window)
        self.Graphics_Settings.setObjectName(u"Graphics_Settings")
        self.Graphics_Settings.setEnabled(True)
        self.Graphics_Settings.setGeometry(QRect(10, 380, 481, 91))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.Graphics_Settings.setFont(font2)
        self.Graphics_Settings.setMouseTracking(False)
        self.Graphics_Settings.setAcceptDrops(False)
        self.Graphics_Settings.setFlat(False)
        self.Graphics_Settings.setCheckable(False)
        self.Graphics_Settings.setChecked(False)
        self.label_Resolution = QLabel(self.Graphics_Settings)
        self.label_Resolution.setObjectName(u"label_Resolution")
        self.label_Resolution.setGeometry(QRect(20, 20, 81, 21))
        font3 = QFont()
        font3.setBold(False)
        font3.setWeight(50)
        self.label_Resolution.setFont(font3)
        self.comboBox_Resolution = QComboBox(self.Graphics_Settings)
        self.comboBox_Resolution.setObjectName(u"comboBox_Resolution")
        self.comboBox_Resolution.setGeometry(QRect(100, 20, 281, 22))
        self.checkBox_Windowed = QCheckBox(self.Graphics_Settings)
        self.checkBox_Windowed.setObjectName(u"checkBox_Windowed")
        self.checkBox_Windowed.setGeometry(QRect(390, 20, 91, 21))
        self.checkBox_Windowed.setCheckable(True)
        self.checkBox_Windowed.setChecked(False)
        self.label_FPS = QLabel(self.Graphics_Settings)
        self.label_FPS.setObjectName(u"label_FPS")
        self.label_FPS.setGeometry(QRect(20, 50, 81, 21))
        self.label_FPS.setLayoutDirection(Qt.LeftToRight)
        self.spinBox_FPS = QSpinBox(self.Graphics_Settings)
        self.spinBox_FPS.setObjectName(u"spinBox_FPS")
        self.spinBox_FPS.setGeometry(QRect(50, 50, 51, 22))
        self.spinBox_FPS.setMinimum(15)
        self.spinBox_FPS.setMaximum(200)
        self.buttonBox = QDialogButtonBox(self.Graphics_Settings)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(310, 60, 156, 23))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Reset|QDialogButtonBox.Save)

        self.retranslateUi(Main_Window)

        QMetaObject.connectSlotsByName(Main_Window)
    # setupUi

    def retranslateUi(self, Main_Window):
        Main_Window.setWindowTitle(QCoreApplication.translate("Main_Window", u"Howard Good", None))
        self.Play_Button.setText(QCoreApplication.translate("Main_Window", u"Play", None))
        self.Background.setText("")
        self.Graphics_Settings.setTitle(QCoreApplication.translate("Main_Window", u"Graphics Settings", None))
        self.label_Resolution.setText(QCoreApplication.translate("Main_Window", u"Resolution", None))
        self.checkBox_Windowed.setText(QCoreApplication.translate("Main_Window", u"Windowed", None))
        self.label_FPS.setText(QCoreApplication.translate("Main_Window", u"FPS", None))
    # retranslateUi

