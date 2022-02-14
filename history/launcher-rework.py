#2022/2/14
# import datetime
# import subprocess
import json
import os
import random
import sys
import time
import webbrowser
from datetime import datetime

import pyautogui
import requests
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import QProcess

import cc_main_localization
import launcher_localization
import start_local
from Ui_Launcher import Ui_Main_Window as launcher_window
from choose_character import Ui_Form as choose_character_window
from start_ui import Ui_Form as start_window

current_version = "0.1.0b"

# WORKING DIR CHECK START


def CheckWorkDir() -> None:
    # from os.path import expanduser

    HomeDir = os.path.expanduser("~")
    HomeDir = HomeDir.lower()
    CurrentDir = os.getcwd()
    CurrentDir = CurrentDir.lower()
    if CurrentDir in ["windows\\system32", HomeDir]:
        print("Error, Please change Work Dir.")
        os.system("pause")
        sys.exit()

    if CurrentDir.find("pixelrpg-python") == -1:
        print("[WARN] You are not in PixelRPG-Python Folder.")
        print("Continue? (To exit, press Ctrl+C)")
        try:
            # countdown for 5 seconds
            for i in range(5):
                print(str(5 - i) + "...")
                time.sleep(1)
        except KeyboardInterrupt:
            print("[WARN] Ctrl+C detected. Exiting...")
            sys.exit()
    del CurrentDir, HomeDir


CheckWorkDir()
del CheckWorkDir

# create Log folder if not exists
if not os.path.exists("Log"):
    os.makedirs("Log")

date = datetime.utcnow().strftime("%Y-%m-%d_%H.%M.%S")
# sys.stdout = open(f"Log/{date}_log.txt", "w")
# todo: https://stackoverflow.com/questions/19425736/how-to-redirect-stdout-and-stderr-to-logger-in-python

"""if not os.path.isfile("Json/save.json"):
    save_exists = False
    with open("Json/save.json", "w") as f:
        json.dump({"level": 0}, f, indent=4)
else:
    save_exists = True
"""


# TODO: rewrite print to logging

# WORKING DIR CHECK END

# PYINSTALLER CHECK START


def CheckPyInstaller() -> bool:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        print("[INFO] You are running from PyInstaller packed executable.")
        return True
    else:
        print("[INFO] You are running from normal Python source code.")
        return False


# PYINSTALLER CHECK END


def open_github_website() -> None:
    print(
        "[ERROR] Something went wrong while opening Select Class Window. I suggest you re-download game file"
    )

    webbrowser.open(
        "https://www.github.com/cytsai1008/PixelRPG-Python",
        new=0,
        autoraise=True,
    )
    sys.exit()


# JSON CHECK START


def json_dump() -> None:
    width, height = pyautogui.size()
    screensize = f"{width} x {height}"
    print(f"[INFO] Your screen size is {screensize}")
    with open("Json/config.json", "w") as g:
        # add resolution, music, windowed to json
        if width > 1920 and height > 1080:
            json.dump(
                {
                    "resolution": [screensize, "1920 x 1080", "1280 x 720"],
                    "preferresolution": screensize,
                    "music": True,
                    "windowed": False,
                    "fps": 60,
                },
                g,
                indent=4,
            )
        else:
            json.dump(
                {
                    "resolution": [screensize, "1280 x 720"],
                    "preferresolution": screensize,
                    "music": True,
                    "windowed": False,
                    "fps": 60,
                },
                g,
                indent=4,
            )
    del g, screensize, width, height
    # add resolution 2k and 4k if screensize over 1920 x 1080


if not os.path.isfile("Json/config.json"):
    print("[WARN] config.json not found.")
    print("[WARN] Creating new config.json.")
    # read screen biggest resolution
    json_dump()

# try json file is readable
try:
    with open("Json/config.json", "r") as f:
        config = json.load(f)
        resolution = config["resolution"]
        preferresolution = config["preferresolution"]
        music = config["music"]
        windowed = config["windowed"]
        fps = config["fps"]
    del config, f, resolution, preferresolution, music, windowed, fps

except:
    print("[WARN] config.json corrupt.")
    print("[WARN] retry creating new config.json.")
    # read screen biggest resolution
    json_dump()
finally:
    with open("Json/config.json", "r") as f:
        config = json.load(f)
    print(f"[INFO] The resolution in config is {config['resolution']}")
    print(f"[INFO] The music in config is {config['music']}")
    print(f"[INFO] The windowed in config is {config['windowed']}")
    print(f"[INFO] The fps in config is {config['fps']}")
    print("[INFO] Starting launcher window")
    del f


def json_reset() -> None:
    with open("Json/choose.json", "w") as f:
        choose_data = {"choose": "Archer"}
        json.dump(choose_data, f, indent=4)
    del f, choose_data


if not os.path.isfile("Json/choose.json"):
    print("[WARN] choose.json not found.")
    print("[WARN] Creating new choose.json.")
    json_reset()

try:
    with open("Json/choose.json", "r") as f:
        choose_data = json.load(f)
    del f
except:
    print("[WARN] choose.json is broken.")
    print("[WARN] Creating new choose.json.")
    json_reset()


# JSON CHECK END

# SYSTEM LANGUAGE CHECK START


def check_lang() -> str:
    # use module locale to check system language
    try:
        with open("Json/config.json", "r") as f:
            lang_config = json.load(f)
            lang = lang_config["lang"]
            print(f"[INFO] Language in config is {lang}")
            print("[INFO] Skipping system language detection")
            syslang = lang
            del lang, f, lang_config
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


# SYSTEM LANGUAGE CHECK END


def json_save(self) -> None:
    # get resolution from combo box
    preferresolution = self.ui.Resolution_Settings.currentText()
    # get windowed from check box
    windowed = self.ui.Windowed_Settings.isChecked()
    # get music from check box
    music = self.ui.Music_On.isChecked()
    # get fps from spin box
    fps = self.ui.FPS_Settings.value()
    # write to config.json
    with open("Json/config.json", "r") as f:
        a = json.load(f)
    del f
    with open("Json/config.json", "w") as f:
        # add dict
        try:
            json_lang = a["lang"]
            choose_data = {
                "resolution": a["resolution"],
                "preferresolution": preferresolution,
                "music": music,
                "windowed": windowed,
                "fps": fps,
                "lang": json_lang,
            }
        except:
            choose_data = {
                "resolution": a["resolution"],
                "preferresolution": preferresolution,
                "music": music,
                "windowed": windowed,
                "fps": fps,
            }
        json.dump(choose_data, f, indent=4)
    del a, choose_data, f, preferresolution, music, windowed, fps


try:
    update_check = requests.get(
        "https://api.github.com/repos/cytsai1008/PixelRPG-Python/tags"
    ).json()
    if update_check[0]["name"] != current_version:
        print("[INFO] New version available.")
        print(
            f"[INFO] Current version is {current_version}, Newest version is {update_check[0]['name']}"
        )
        updateable = True
    else:
        print("[INFO] No new version available.")
        updateable = False
except:
    print("[WARN] Can't check update.")
    updateable = False
finally:
    del update_check, current_version


class Launcher_Window(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(Launcher_Window, self).__init__(None)
        self.cc = Choose_Character_Window()
        self.ui = launcher_window()
        self.ui.setupUi(self)
        # setup font
        QtGui.QFontDatabase.addApplicationFont("Launcher Asset/unifont-14.0.01.ttf")
        # add combo box text from config.json
        launcher_localization.lang_module(self, return_lang)
        # localization
        if updateable:
            update_text = launcher_localization.update_word(return_lang)
            if QtWidgets.QMessageBox.Yes == QtWidgets.QMessageBox.information(
                    self,
                    "Update Available",
                    update_text,
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                    QtWidgets.QMessageBox.No,
            ):
                open_github_website()
                # sys.exit()

        self.ui.Resolution_Settings.addItems(config["resolution"])
        # set combo box text from config.json if preferresolution exist
        self.ui.Resolution_Settings.setCurrentText(config["preferresolution"])
        print(f"[INFO] Prefer resolution is {config['preferresolution']}")

        # setting up environment

        if config["windowed"]:
            # Always remember to change Ui_Launcher file while re-compiling
            self.ui.Windowed_Settings.setChecked(True)
        else:
            self.ui.Windowed_Settings.setChecked(False)

        if config["music"]:
            # Always remember to change Ui_Launcher file while re-compiling
            self.ui.Music_On.setChecked(True)
            self.ui.Music_Off.setChecked(False)
        else:
            self.ui.Music_On.setChecked(False)
            self.ui.Music_Off.setChecked(True)

        self.ui.FPS_Settings.setValue(int(config["fps"]))
        self.ui.FPS_Settings.setReadOnly(True)
        self.ui.FPS_Settings.setEnabled(False)
        self.ui.label_FPS.setEnabled(False)
        # play button click
        self.ui.Button_Play.clicked.connect(self.Play)
        # save button click
        self.ui.Button_Save.clicked.connect(self.json_save)
        self.ui.Button_Reset.clicked.connect(self.json_reset)
        self.ui.Background.mousePressEvent = self.background_click

    def background_click(self, event) -> None:
        import random

        rick = random.randint(1, 20)
        if rick == 10:
            import webbrowser

            print("[INFO] Rick Astley is coming")
            QtWidgets.QMessageBox.information(
                self, "Look what have you done!", "Never Gonna Give You Up :)"
            )
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            sys.exit(0)

    def json_reset(self) -> None:
        json_dump()
        print("[INFO] Reset config.json")
        with open("Json/config.json", "r") as f:
            config = json.load(f)
        del f
        self.ui.Windowed_Settings.setChecked(False)
        self.ui.Music_On.setChecked(True)
        self.ui.Music_Off.setChecked(False)
        width, height = pyautogui.size()
        screensize = f"{width} x {height}"
        self.ui.Resolution_Settings.clear()
        self.ui.Resolution_Settings.addItems(config["resolution"])
        self.ui.Resolution_Settings.setCurrentText(screensize)
        self.ui.FPS_Settings.setValue(60)
        del screensize, width, height, config

    def json_save(self) -> None:
        # get resolution from combo box
        preferresolution = self.ui.Resolution_Settings.currentText()
        # get windowed from check box
        windowed = self.ui.Windowed_Settings.isChecked()
        # get music from check box
        music = self.ui.Music_On.isChecked()
        # get fps from spin box
        fps = self.ui.FPS_Settings.value()
        # write to config.json
        with open("Json/config.json", "w") as f:
            # add dict
            data = {
                "resolution": config["resolution"],
                "preferresolution": preferresolution,
                "music": music,
                "windowed": windowed,
                "fps": fps,
            }
            json.dump(data, f, indent=4)
        print("[INFO] Save config.json")
        del preferresolution, windowed, music, fps, data, f

    def Play(self) -> None:
        print("[INFO] Starting game and saving settings data")
        # self.showMinimized()
        json_save(self)
        with open("Json/config.json", "r") as f:
            data = json.load(f)
        print(
            f"[INFO] Starting up the game with the resolution is {data['preferresolution']} \n"
            f"with windowed {data['windowed']}, \n"
            f"music is {data['music']}, \n"
            f"fps is {data['fps']}\n"
        )
        del data, f
        # self.cc = Choose_Character_Window()
        self.cc.show()
        self.cc.showNormal()


class Choose_Character_Window(QtWidgets.QWidget):
    def __init__(self):
        super(Choose_Character_Window, self).__init__(None)
        self.start = None
        self.ui = choose_character_window()
        self.ui.setupUi(self)
        QtGui.QFontDatabase.addApplicationFont("Launcher Asset/unifont-14.0.01.ttf")
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.ui.cc1.clicked.connect(self.chooseArcher)
        self.ui.cc2.clicked.connect(self.chooseKnight)
        self.ui.cc3.clicked.connect(self.chooseMagician)
        self.ui.cc4.clicked.connect(self.chooseAssassin)
        self.ui.play.clicked.connect(self.play)
        # self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)

        self.Archer = "You will play 'Archer' in game."
        self.Knight = "You will play 'Knight' in game."
        self.Magician = "You will play 'Magician' in game."
        self.Assassin = "You will play 'Assassin' in game."

        if return_lang == "zh-hant":
            cc_main_localization.set_hant(self)

        elif return_lang == "zh-hans":
            cc_main_localization.set_hans(self)
        elif return_lang == "ja":
            cc_main_localization.set_ja(self)

        with open("Json/choose.json", "r") as f:
            choose_config = json.load(f)
        del f
        self.a = choose_config["choose"]
        if self.a == "Archer":
            self.ui.now_choose.setText(self.Archer)
        elif self.a == "Knight":
            self.ui.now_choose.setText(self.Knight)
        elif self.a == "Magician":
            self.ui.now_choose.setText(self.Magician)
        elif self.a == "Assassin":
            self.ui.now_choose.setText(self.Assassin)

    def chooseArcher(self):
        self.chooseCharacter("Archer", self.Archer)

    def chooseKnight(self):
        self.chooseCharacter("Knight", self.Knight)

    def chooseMagician(self):
        self.chooseCharacter("Magician", self.Magician)

    def chooseAssassin(self):
        self.chooseCharacter("Assassin", self.Assassin)

    def chooseCharacter(self, arg0, arg1):
        nowchoose = arg0
        with open("Json/choose.json", "w") as f:
            choose_data = {"choose": nowchoose}
            json.dump(choose_data, f, indent=4)
        self.ui.now_choose.setText(arg1)
        del f, choose_data

    def play(self):
        # self.showMinimized()
        # start game
        print(f"[INFO] Trying to start the game with class {choose_data['choose']}.")
        # import subprocess
        if os.path.exists("Json/save.json"):
            print("The save.json exist")

            self.start = Start_Window()
            self.start.show()
            self.start.showNormal()
            # self.showNormal()
        else:
            print("The save.json doesn't exist")
            if CheckPyInstaller() and os.path.exists("release/main.exe"):
                try:
                    self.p = QProcess()
                    self.p.setProcessChannelMode(QProcess.ForwardedChannels)
                    self.p.start("release/main.exe")
                except FileNotFoundError:
                    QtWidgets.QMessageBox.warning(
                        self,
                        "Error",
                        "Game file corrupt, please retry download it.",
                    )
                    open_github_website()
                except:
                    print("[ERROR] Unknown game error, please report to developer.")
            elif (
                    CheckPyInstaller()
                    and not os.path.exists("release/main.exe")
                    or not CheckPyInstaller()
                    and not os.path.exists("main.py")
            ):
                QtWidgets.QMessageBox.warning(
                    self, "Error", "Game file corrupt, please retry download it."
                )
                open_github_website()
            else:
                try:
                    self.p = QProcess()
                    self.p.setProcessChannelMode(QProcess.ForwardedChannels)
                    self.p.start("python", ["main.py"])
                except FileNotFoundError:
                    QtWidgets.QMessageBox.warning(
                        self, "Error", "Game file corrupt, please retry download it."
                    )
                    open_github_website()


class Start_Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Start_Window, self).__init__(None)
        self.p = None
        self.ui = start_window()
        self.ui.setupUi(self)
        QtGui.QFontDatabase.addApplicationFont("Launcher Asset/unifont-14.0.01.ttf")
        if os.path.exists("Json/save.json"):
            with open("Json/save.json", "r") as f:
                save = json.load(f)
            del f
        else:
            save = {"level": 0}

        text = (
            f"You have arrived the level {int(save['level'])} \n"
            "Do you want continue?"
        )
        self.ui.text.setText(text)

        start_local.lang_module(self, return_lang, int(save["level"]))
        self.ui.play1.clicked.connect(self.play1)
        self.ui.play2.clicked.connect(self.play2)

    def play1(self):
        # self.showMinimized()
        if CheckPyInstaller():
            if os.path.exists("release/main.exe"):
                try:
                    self.p = QProcess()
                    self.p.setProcessChannelMode(QProcess.ForwardedChannels)
                    self.p.start("release/main.exe")
                except FileNotFoundError:
                    QtWidgets.QMessageBox.warning(
                        self, "Error", "Game file corrupt, please retry download it."
                    )
                    open_github_website()
                except:
                    print("[ERROR] Unknown game error, please report to developer.")
            else:
                QtWidgets.QMessageBox.warning(
                    self, "Error", "Game file corrupt, please retry download it."
                )
                open_github_website()
        elif os.path.exists("main.py"):
            try:
                self.p = QProcess()
                self.p.setProcessChannelMode(QProcess.ForwardedChannels)
                self.p.start("python", ["main.py"])
            except FileNotFoundError:
                QtWidgets.QMessageBox.warning(
                    self, "Error", "Game file corrupt, please retry download it."
                )
                open_github_website()

        else:
            QtWidgets.QMessageBox.warning(
                self, "Error", "Game file corrupt, please retry download it."
            )
            print("[ERROR] Unknown game error, please report to developer.")
            open_github_website()
        # self.showNormal()
        self.close()

    def play2(self):
        # self.showMinimized()
        with open("Json/save.json", "w") as s:
            level = {"level": 0}
            json.dump(level, s, indent=4)
        del s, level

        if CheckPyInstaller():
            try:
                self.p = QProcess()
                self.p.setProcessChannelMode(QProcess.ForwardedChannels)
                self.p.start("release/main.exe")
            except FileNotFoundError:
                QtWidgets.QMessageBox.warning(
                    self, "Error", "Game file corrupt, please retry download it."
                )
                open_github_website()
        else:
            try:
                self.p = QProcess()
                self.p.setProcessChannelMode(QProcess.ForwardedChannels)
                self.p.start("python", ["main.py"])
            except FileNotFoundError:
                QtWidgets.QMessageBox.warning(
                    self, "Error", "Game file corrupt, please retry download it."
                )
                open_github_website()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    pixmap = QtGui.QPixmap("Launcher Asset/Logo_Splash.png")
    splash = QtWidgets.QSplashScreen(pixmap)
    splashlabel = QtWidgets.QLabel(splash)
    splashgif = QtGui.QMovie("Launcher Asset/Logo_Splash.gif")
    splashlabel.setMovie(splashgif)
    splashgif.start()
    splash.show()
    # QtGui.QFontDatabase.addApplicationFont("Launcher Asset/unifont-14.0.01.ttf")
    secret_message = random.randint(1, 1000)
    if secret_message == 34:
        splash_message = "You can be Rick Rolled by press the image"
    elif secret_message == 615:
        splash_message = "Tetora is my husband"
    else:
        splash_message = "Loading..."
    # splash.setFont(u"Unifont")
    splash.showMessage(splash_message, QtCore.Qt.AlignBottom, QtCore.Qt.black)
    delayTime = 1.5
    timer = QtCore.QElapsedTimer()
    timer.start()
    while timer.elapsed() < delayTime * 1000:
        app.processEvents()
    window = Launcher_Window()
    window.show()
    splash.finish(window)
    sys.exit(app.exec_())
