from asyncio import subprocess
from re import sub
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import QProcess, Qt
from PySide2.QtGui import QFontDatabase, QPixmap
from PySide2.QtWidgets import QSplashScreen
import json
import os

from start_ui import Ui_Form

with open("Json/save.json")as f:
    data = json.load(f)

def CheckPyInstaller():
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        print("[INFO] You are running from PyInstaller packed executable.")
        return True
    else:
        print("[INFO] You are running from normal Python source code.")
        return False

def open_github_website():
    print(
        "[ERROR] Something went wrong while opening Select Class Window. I suggest you re-download game file"
    )
    import webbrowser

    webbrowser.open(
        "https://www.github.com/cytsai1008/PixelRPG-Python",
        new=0,
        autoraise=True,
    )
    del webbrowser

class mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainwindow,self).__init__(None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("Launcher Asset/unifont-14.0.01.ttf")
        text = "You have arrived the "+str(data["level"])+" level \n do you want continue?"
        self.ui.text.setText(text)
        self.ui.play1.clicked.connect(self.play1)
        self.ui.play2.clicked.connect(self.play2)
    def play1(self):
        self.showMinimized()
        if CheckPyInstaller():
            if os.path.exists("main.exe"):
                try:
                    self.p = QProcess()
                    self.p.setProcessChannelMode(QProcess.ForwardedChannels)
                    self.p.start("main.exe")
                except FileNotFoundError:
                    open_github_website()
                except:
                    print("[ERROR] Unknown game error, please report to developer.")
            else:
                open_github_website()
        elif os.path.exists("main.py"):
            try:
                self.p = QProcess()
                self.p.setProcessChannelMode(QProcess.ForwardedChannels)
                self.p.start("python", ["main.py"])
            except FileNotFoundError:
                open_github_website()
        else:
            open_github_website()
        # self.showNormal()
    def play2(self):
        self.showMinimized()
        with open("Json/save.json",'w') as s:
            level = {"level": 0 }
            json.dump(level,s,indent=4)
        if CheckPyInstaller():
            if os.path.exists("main.exe"):
                try:
                    self.p = QProcess()
                    self.p.setProcessChannelMode(QProcess.ForwardedChannels)
                    self.p.start("main.exe")
                except FileNotFoundError:
                    open_github_website()
                except:
                    print("[ERROR] Unknown game error, please report to developer.")
            else:
                open_github_website()
        elif os.path.exists("main.py"):
            try:
                self.p = QProcess()
                self.p.setProcessChannelMode(QProcess.ForwardedChannels)
                self.p.start("python", ["main.py"])
            except FileNotFoundError:
                open_github_website()
        else:
            open_github_website()
        # self.showNormal()

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication()
    window = mainwindow()
    window.show()
    sys.exit(app.exec_())