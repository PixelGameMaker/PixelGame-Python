import json
import os
import time


from PySide2 import QtWidgets
from PySide2.QtGui import QFontDatabase

from choose_character import Ui_Form


# PYINSTALLER CHECK START


def CheckPyInstaller():
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        print(
            "[INFO] You are running from PyInstaller packed executable. Hopes there is no bug."
        )
        return True
    else:
        print("[INFO] You are running from normal Python source code.")
        return False


# PYINSTALLER CHECK END


def open_github_website():
    print("[ERROR] Game not found. I suggest you re-download game file")
    import webbrowser

    webbrowser.open(
        "https://www.github.com/cytsai1008/PixelRPG-Python",
        new=0,
        autoraise=True,
    )
    del webbrowser


def json_reset():
    with open("Json/choose.json", "w") as f:
        data = {"choose": "Archer"}
        json.dump(data, f, indent=4)


if not os.path.isfile("Json/choose.json"):
    print("[WARN] choose.json not found.")
    print("[WARN] Creating new choose.json.")
    json_reset()

try:
    with open("Json/choose.json", "r") as f:
        data = json.load(f)
except:
    print("[WARN] choose.json is broken.")
    print("[WARN] Creating new choose.json.")
    json_reset()


def check_lang():
    # use module locale to check system language
    try:
        with open("Json/config.json", "r") as f:
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
        elif syslang in ["zh_cn", "zh_sg", "zh_my", "zh_hans"]:
            print("[INFO] System language is Chinese Simplified")
            del locale
            return "zh-hans"
        elif syslang in ["ja_jp", "ja"]:
            print("[INFO] System language is Japanese")
            del locale
            return "ja"
        else:
            print("[INFO] System language current is not support, set to English")
            del locale
            return "en"


return_lang = check_lang()


class MainWindow_cc(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow_cc, self).__init__(None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("Launcher Asset/unifont-14.0.01.ttf")
        self.ui.cc1.clicked.connect(self.chooseArcher)
        self.ui.cc2.clicked.connect(self.chooseKnight)
        self.ui.cc3.clicked.connect(self.chooseMagician)
        self.ui.cc4.clicked.connect(self.chooseAssassin)
        self.ui.play.clicked.connect(self.play)

        self.Archer = "You will play 'Archer' in game."
        self.Knight = "You will play 'Knight' in game."
        self.Magician = "You will play 'Magician' in game."
        self.Assassin = "You will play 'Assassin' in game."

        if return_lang == "zh-hant":
            from cc_main_localization import set_hant

            set_hant(self)
        elif return_lang == "zh-hans":
            from cc_main_localization import set_hans

            set_hans(self)
        elif return_lang == "ja":
            from cc_main_localization import set_ja

            set_ja(self)

        with open("Json/choose.json", "r") as f:
            config = json.load(f)
        self.a = config["choose"]
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
            data = {"choose": nowchoose}
            json.dump(data, f, indent=4)
        self.ui.now_choose.setText(arg1)

    def play(self):
        self.showMinimized()
        # start game
        print(f"[INFO] Trying to start the game with class {data['choose']}.")
        import subprocess

        if CheckPyInstaller():
            if os.path.exists("main.exe"):
                try:
                    subprocess.call(["main.exe"])
                except FileNotFoundError:
                    open_github_website()
                except:
                    print("[ERROR] Unknown game error, please report to developer.")
            else:
                open_github_website()
        elif os.path.exists("main.py"):
            try:
                subprocess.call(["python", "main.py"])
            except FileNotFoundError:
                open_github_website()
            """
            except Exception:
                print("[ERROR] Unknown game error, please report to developer.")
                error_data = traceback.format_exc()
                # print(error_data)
                date = datetime.utcnow().strftime("%Y-%m-%d_%H.%M.%S")
                if not os.path.exists("ErrorLog"):
                    os.mkdir("ErrorLog")
                with open('ErrorLog/traceback_{}.txt'.format(date), 'w') as f:
                    f.write(error_data)
                if CheckPyInstaller():
                    self.p = QProcess()
                    self.p.start("ErrorWindow.exe")
                else:
                    self.p = QProcess()
                    self.p.start("python", "ErrorWindow.py")
            """

        else:
            open_github_website()
        self.showNormal()
        time.sleep(1)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication()
    window = MainWindow_cc()
    window.show()
    sys.exit(app.exec_())
