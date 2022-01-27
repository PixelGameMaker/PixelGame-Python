import json
import os

from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import QProcess, Qt
from PySide2.QtGui import QFontDatabase, QPixmap
from PySide2.QtWidgets import QSplashScreen

from start_ui import Ui_Form

with open("Json/save.json") as f:
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


def check_lang():
    # use module locale to check system language
    try:
        with open("Json/config.json", "r") as f:
            lang_config = json.load(f)
            lang = lang_config["lang"]
            print(f"[INFO] Language in config is {lang}")
            print("[INFO] Skipping system language detection")
            syslang = lang
    except:
        import locale

        syslang = locale.getdefaultlocale()[0].lower()
        del locale

    if syslang in ["zh_tw", "zh_hk", "zh_mo", "zh_hant"]:
        print("[INFO] System language is Chinese Traditional")
        return "zh-hant"
    elif syslang in ["zh_cn", "zh_sg", "zh_my", "zh_hans"]:
        print("[INFO] System language is Chinese Simplified")
        return "zh-hans"
    elif syslang in ["ja_jp", "ja"]:
        print("[INFO] System language is Japanese")
        return "ja"
    else:
        print("[INFO] System language current is not support, set to English")
        return "en"


return_lang = check_lang()
del check_lang


class mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainwindow, self).__init__(None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("Launcher Asset/unifont-14.0.01.ttf")
        text = (
            f"You have arrived the level {int(data['level'])} \n"
            "Do you want continue?"
        )
        self.ui.text.setText(text)
        from start_local import lang_module

        lang_module(self, return_lang, int(data["level"]))
        self.ui.play1.clicked.connect(self.play1)
        self.ui.play2.clicked.connect(self.play2)

    def play1(self):
        self.showMinimized()
        if CheckPyInstaller():
            if os.path.exists("realese/main.exe"):
                try:
                    self.p = QProcess()
                    self.p.setProcessChannelMode(QProcess.ForwardedChannels)
                    self.p.start("realese/main.exe")
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
            print("[ERROR] Unknown game error, please report to developer.")
        # self.showNormal()

    def play2(self):
        self.showMinimized()
        with open("Json/save.json", "w") as s:
            level = {"level": 0}
            json.dump(level, s, indent=4)

        if CheckPyInstaller():
            if os.path.exists("realese/main.exe"):
                try:
                    self.p = QProcess()
                    self.p.setProcessChannelMode(QProcess.ForwardedChannels)
                    self.p.start("realese/main.exe")
                except FileNotFoundError:
                    open_github_website()
        else:
            try:
                self.p = QProcess()
                self.p.setProcessChannelMode(QProcess.ForwardedChannels)
                self.p.start("python", ["main.py"])
            except FileNotFoundError:
                open_github_website()
        # self.showNormal()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication()
    pixmap = QPixmap("Launcher Asset/Logo_Splash.png")
    splash = QSplashScreen(pixmap)
    splashlabel = QtWidgets.QLabel(splash)
    splashgif = QtGui.QMovie("Launcher Asset/Logo_Splash.gif")
    splashlabel.setMovie(splashgif)
    splashgif.start()
    splash.show()
    splash.showMessage("Hope you have fun this time", Qt.AlignBottom, Qt.black)
    delayTime = 1.3
    timer = QtCore.QElapsedTimer()
    timer.start()
    while timer.elapsed() < delayTime * 1000:
        app.processEvents()
    window = mainwindow()
    window.show()
    splash.finish(window)
    sys.exit(app.exec_())
