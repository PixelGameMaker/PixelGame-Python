import json
import os
import sys
import time
from os.path import expanduser

import pyautogui

from PySide2 import QtWidgets

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


CheckWorkDir()

# WORKING DIR CHECK END

# JSON CHECK START


def json_dump():
    width, height = pyautogui.size()
    screensize = (f"{width} x {height}")
    print(f"[INFO] Your screen size is {screensize}")
    with open("config.json", "w") as f:
        # add resolution, music, windowed to json
        json.dump({"resolution": [screensize, "1280 x 720"], "preferresolution": screensize,
                  "music": "true", "windowed": "true", "fps": "60"}, f, indent=4)
        # add resolution 2k and 4k if screensize over 1920 x 1080
        if width > 1920 and height > 1080:
            with open("config.json", "r") as f:
                data = json.load(f)
                data["resolution"].append("1920 x 1080")
                data["resolution"].append("2560 x 1440")
                json.dump(data, f)


if not os.path.isfile("config.json"):
    print("[WARN] config.json not found.")
    print("[WARN] Creating new config.json.")
    # read screen biggest resolution
    json_dump()

# try json file is readable
try:
    with open("config.json", "r") as f:
        config = json.load(f)
        resolution = config["resolution"]
        preferresolution = config["preferresolution"]
        music = config["music"]
        windowed = config["windowed"]
        fps = config["fps"]

except:
    print("[WARN] config.json corrupt.")
    print("[WARN] retry creating new config.json.")
    # read screen biggest resolution
    json_dump()
finally:
    with open("config.json", "r") as f:
        config = json.load(f)
    print(f"[INFO] The resolution in config is {config['resolution']}")
    print(f"[INFO] The music in config is {config['music']}")
    print(f"[INFO] The windowed in config is {config['windowed']}")
    print(f"[INFO] The fps in config is {config['fps']}")
    print('[INFO] Starting launcher window')

# JSON CHECK END

# SYSTEM LANGUAGE CHECK START


def check_lang():
    # use module locale to check system language
    try:
        with open("config.json", "r") as f:
            lang_config = json.load(f)
            lang = lang_config["lang"]
            print(f"[INFO] Language in config is {lang}")
            print("[INFO] Skipping system language detection")
            return lang
    except:
        import locale
        syslang = locale.getdefaultlocale()[0].lower()
        if syslang in ["zh_tw", "zh_hk", "zh_mo", "zh_hant"]:
            print("[INFO] System language is Chinese Traditional")
            del locale
            return "zh-hant"
        elif syslang in ["zh_cn", "zh_sg", "zh-my", "zh_hans"]:
            print("[INFO] System language is Chinese Simplified")
            del locale
            return "zh-hans"
        else:
            print("[INFO] System language current is not support, set to English")
            del locale
            return "en"


return_lang = check_lang()
# SYSTEM LANGUAGE CHECK END


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Main_Window()
        self.ui.setupUi(self)
        # add combo box text from config.json
        self.ui.Resolution_Settings.addItems(config["resolution"])
        # set combo box text from config.json if preferresolution exist
        self.ui.Resolution_Settings.setCurrentText(config["preferresolution"])
        print(f"[INFO] Preffer resolution is {config['preferresolution']}")

        # localization
        def set_hant():
            self.ui.label_Music.setText("音樂：")
            self.ui.Windowed_Settings.setText("視窗化")
            self.ui.label_Resolution.setText("解析度：")
            self.ui.Button_Play.setText("開始遊戲")
            self.ui.Graphics_Settings.setTitle("顯示設定")
            self.ui.Music_On.setText("開啟")
            self.ui.Music_Off.setText("關閉")

        def set_hans():
            self.ui.label_Music.setText("音乐：")
            self.ui.Windowed_Settings.setText("窗口化")
            self.ui.label_Resolution.setText("分辨率：")
            self.ui.Button_Play.setText("开始游戏")
            self.ui.Graphics_Settings.setTitle("显示设置")
            self.ui.Music_On.setText("开启")
            self.ui.Music_Off.setText("关闭")

        if return_lang == "zh-hant":
            set_hant()
        elif return_lang == "zh-hans":
            set_hans()

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
        # play button click
        self.ui.Button_Play.clicked.connect(self.Play)

    def Play(self):
        print("[INFO] Starting game and saving settings data")
        self.showMinimized()
        # get resolution from combo box
        preferresolution = self.ui.Resolution_Settings.currentText()
        # get windowed from check box
        windowed = self.ui.Windowed_Settings.isChecked()
        # get music from check box
        music = self.ui.Music_On.isChecked()
        # get fps from spin box
        fps = self.ui.FPS_Settings.value()
        # write to config.json
        with open("config.json", "w") as f:
            # add dict
            data = {"resolution": config['resolution'], "preferresolution": preferresolution,
                    "music": music, "windowed": windowed, "fps": fps}
            json.dump(data, f, indent=4)
        print(
            f"[INFO] Starting up the game with the resolution is {data['preferresolution']} with windowded {data['windowed']}, music is {data['music']}, fps is {data['fps']}\n")
        # start game
        # os.system("clear")
        #import pygame.locals
        try:
            exec(open("main.py").read())
        except FileNotFoundError:
            print("[ERROR] main.py not found. Are you release?")
            try:
                import subprocess
                subprocess.call(["main.exe"])
            except FileNotFoundError:
                print("[ERROR] No game file found. Please retry download.")
        finally:
            self.showNormal()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
