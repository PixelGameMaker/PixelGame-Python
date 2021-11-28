import json
import os

from PySide2 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from choose_character import Ui_Form

def json_dump():
    with open('choose.json','w')as f:
        data={"choose": nowchoose}
        json.dump(data,f,indent=4)
        
def json_reset():
    with open("choose.json","w") as f:
        data={"choose": "Archer"}
        json.dump(data,f,indent=4)

if not os.path.isfile("choose.json"):
    print("[WARN] choose.json not found.")
    print("[WARN] Creating new choose.json.")
    json_reset()
        
try:
    with open("choose.json","r") as f:
        data=json.load(f)
except:
    print("[WARN] choose.json is broken.")
    print("[WARN] Creating new choose.json.")
    json_reset()

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
        super(MainWindow_cc, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.cc1.clicked.connect(self.chooseArcher)
        self.ui.cc2.clicked.connect(self.chooseKnight)
        self.ui.cc3.clicked.connect(self.chooseMagician)
        self.ui.cc4.clicked.connect(self.chooseAssassin)
        self.ui.play.clicked.connect(self.play)

        self.Archer="You will play 'Archer' in game."
        self.Knight="You will play 'Knight' in game."
        self.Magician="You will play 'Magician' in game."
        self.Assassin="You will play 'Assassin' in game."

        if return_lang == "zh-hant":
            from cc_main_localization import set_hant
            set_hant(self)
        elif return_lang == "zh-hans":
            from cc_main_localization import set_hans
            set_hans(self)
        elif return_lang == "ja":
            from cc_main_localization import set_ja
            set_ja(self)

        with open('choose.json','r')as f:
            config=json.load(f)
        self.a= config['choose']
        if self.a == 'Archer':
            self.ui.now_choose.setText(self.Archer)
        elif self.a == 'Knight':
            self.ui.now_choose.setText(self.Knight)
        elif self.a == 'Magician':
            self.ui.now_choose.setText(self.Magician)
        elif self.a == 'Assassin':
            self.ui.now_choose.setText(self.Assassin)
        
    def chooseArcher(self):
        self._extracted_from_chooseAssassin_2('Archer', self.Archer)

    def chooseKnight(self):
        self._extracted_from_chooseAssassin_2('Knight', self.Knight)

    def chooseMagician(self):
        self._extracted_from_chooseAssassin_2('Magician', self.Magician)

    def chooseAssassin(self):
        self._extracted_from_chooseAssassin_2('Assassin', self.Assassin)

    # TODO Rename this here and in `chooseArcher`, `chooseKnight`, `chooseMagician` and `chooseAssassin`
    def _extracted_from_chooseAssassin_2(self, arg0, arg1):
        nowchoose = arg0
        with open('choose.json', 'w') as f:
            data = {'choose': nowchoose}
            json.dump(data, f, indent=4)
        self.ui.now_choose.setText(arg1)

    def play(self):
        # start game
        try:
            print('start game now')
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
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = MainWindow_cc()
    window.show()
    sys.exit(app.exec_())