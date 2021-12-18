import json
import os
import sys
import time
from os.path import expanduser
import logging

import pyautogui

from PySide2 import QtWidgets
from PySide2.QtCore import QProcess
from PySide2.QtGui import QFontDatabase


from Ui_Launcher import Ui_Main_Window

# WORKING DIR CHECK START


def CheckWorkDir():
    HomeDir = expanduser("~")
    HomeDir = HomeDir.lower()
    CurrentDir = os.getcwd()
    CurrentDir = CurrentDir.lower()
    if CurrentDir in ["c:\\windows\\system32", HomeDir]:
        print("Error, Please change Work Dir.")
        os.system("pause")
        quit()

    if CurrentDir.find("pixelrpg-python") == -1:
        print("[WARN] You are not in PixelRPG-Python Folder.")
        print("Continue? (To exit, press Ctrl+C)")
        try:
            # countdown for 5 seconds
            for i in range(5):
                print(str(5 - i) + "...")
                time.sleep(1)
        except KeyboardInterrupt:
            print("[WARN] Ctrl+C dected. Exiting...")
            quit()
    del CurrentDir, HomeDir


CheckWorkDir()
del expanduser

# create Log folder if not exsist
if not os.path.exists("Log"):
    os.makedirs("Log")

# TODO: rewirte print to logging

# WORKING DIR CHECK END

# JSON CHECK START


def json_dump():
    width, height = pyautogui.size()
    screensize = f"{width} x {height}"
    print(f"[INFO] Your screen size is {screensize}")
    with open("Json/config.json", "w") as f:
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
                f,
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
                f,
                indent=4,
            )
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
    del config

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

# JSON CHECK END

# SYSTEM LANGUAGE CHECK START


def check_lang():
    # use module locale to check system language
    try:
        with open("Json/config.json", "r") as f:
            lang_config = json.load(f)
            lang = lang_config["lang"]
            print(f"[INFO] Language in config is {lang}")
            print("[INFO] Skipping system language detection")
            del lang_config
            return lang
    except:
        import locale

        syslang = locale.getdefaultlocale()[0].lower()
        if syslang in ["zh_tw", "zh_hk", "zh_mo", "zh_hant"]:
            print("[INFO] System language is Chinese Traditional")
            return "zh-hant"
        elif syslang in ["zh_cn", "zh_sg", "zh-my", "zh_hans"]:
            print("[INFO] System language is Chinese Simplified")
            return "zh-hans"
        elif syslang in ["ja_jp", "ja"]:
            print("[INFO] System language is Japanese")
            return "ja"
        else:
            print("[INFO] System language current is not support, set to English")
            return "en"
    finally:
        try:
            del lang
        except:
            del locale
            del syslang


return_lang = check_lang()
# SYSTEM LANGUAGE CHECK END


def json_save(self):
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
    with open("Json/config.json", "w") as f:
        # add dict
        try:
            json_lang = a["lang"]
            data = {
                "resolution": a["resolution"],
                "preferresolution": preferresolution,
                "music": music,
                "windowed": windowed,
                "fps": fps,
                "lang": json_lang,
            }
        except:
            data = {
                "resolution": a["resolution"],
                "preferresolution": preferresolution,
                "music": music,
                "windowed": windowed,
                "fps": fps,
            }
        json.dump(data, f, indent=4)
    del a, data


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Main_Window()
        self.ui.setupUi(self)
        # setup font
        QFontDatabase.addApplicationFont("Launcher Asset/unifont-14.0.01.ttf")
        # add combo box text from config.json
        self.ui.Resolution_Settings.addItems(config["resolution"])
        # set combo box text from config.json if preferresolution exist
        self.ui.Resolution_Settings.setCurrentText(config["preferresolution"])
        print(f"[INFO] Preffer resolution is {config['preferresolution']}")

        # localization
        from launcher_localization import lang_module

        lang_module(self, return_lang)
        # setting up environment

        if config["windowed"] == True:
            # Always remember to change Ui_Launcher file while re-compiling
            self.ui.Windowed_Settings.setChecked(True)
        else:
            self.ui.Windowed_Settings.setChecked(False)

        if config["music"] == True:
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

    def json_reset(self):
        json_dump()
        print("[INFO] Reset config.json")
        with open("Json/config.json", "r") as f:
            config = json.load(f)
        self.ui.Windowed_Settings.setChecked(False)
        self.ui.Music_On.setChecked(True)
        self.ui.Music_Off.setChecked(False)
        width, height = pyautogui.size()
        screensize = f"{width} x {height}"
        self.ui.Resolution_Settings.clear()
        self.ui.Resolution_Settings.addItems(config["resolution"])
        self.ui.Resolution_Settings.setCurrentText(screensize)
        self.ui.FPS_Settings.setValue(60)

    def json_save(self):
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
        del preferresolution, windowed, music, fps, data

    def Play(self):
        print("[INFO] Starting game and saving settings data")
        self.showMinimized()
        json_save(self)
        with open("Json/config.json", "r") as f:
            data = json.load(f)
        print(
            f"[INFO] Starting up the game with the resolution is {data['preferresolution']} with windowded {data['windowed']}, music is {data['music']}, fps is {data['fps']}\n"
        )

        def Run_cc(self, method, ProcName):
            self.p = QProcess()
            self.p.setProcessChannelMode(QProcess.ForwardedChannels)
            self.p.start(method, [ProcName])
            print("[INFO] Play Button clicked, please select character to play")

        def Run_cc2(self, ProcName):
            self.p = QProcess()
            self.p.setProcessChannelMode(QProcess.ForwardedChannels)
            self.p.start(ProcName)

        try:
            open("cc_main.py", "r")
            Run_cc(self, "python", "cc_main.py")
        except:
            print(
                "[ERROR] cc_main.py not found. Hope there is no bugs in the release version"
            )
            try:
                open("cc_main.exe", "r")
                Run_cc2(self, "cc_main.exe")
            except:
                print(
                    "[ERROR] cc_main.exe not found. I suggest you re-download game file"
                )
                import webbrowser

                webbrowser.open(
                    "https://www.github.com/cytsai1008/PixelRPG-Python",
                    new=0,
                    autoraise=True,
                )
                del webbrowser


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
