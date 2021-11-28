import json
import os

from PySide2 import QtCore, QtGui, QtWidgets
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

with open('choose.json','r')as f:
    config=json.load(f)
nowchoose='Archer'
displaync=config['choose']
if displaync == 'Archer':
    displaync = ' 弓箭手 '
elif displaync == 'Knight':
    displaync = ' 騎士 '
elif displaync == 'Magician':
    displaync = ' 魔法師 '
elif displaync == 'Assassin':
    displaync = ' 刺客 '


class MainWindow_cc(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow_cc, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.now_choose.setText("您將以"+displaync+"進行遊戲")
        self.ui.cc1.clicked.connect(self.chooseArcher)
        self.ui.cc2.clicked.connect(self.chooseKnight)
        self.ui.cc3.clicked.connect(self.chooseMagician)
        self.ui.cc4.clicked.connect(self.chooseAssassin)
        self.ui.play.clicked.connect(self.play)

    def chooseArcher(self):
        self._extracted_from_chooseAssassin_2('Archer', "您將以 弓箭手 進行遊戲")

    def chooseKnight(self):
        self._extracted_from_chooseAssassin_2('Knight', "您將以 騎士 進行遊戲")

    def chooseMagician(self):
        self._extracted_from_chooseAssassin_2('Magician', "您將以 魔法師 進行遊戲")

    def chooseAssassin(self):
        self._extracted_from_chooseAssassin_2('Assassin', "您將以 刺客 進行遊戲")

    # TODO Rename this here and in `chooseArcher`, `chooseKnight`, `chooseMagician` and `chooseAssassin`
    def _extracted_from_chooseAssassin_2(self, arg0, arg1):
        nowchoose = arg0
        with open('choose.json', 'w') as f:
            data = {'choose': nowchoose}
            json.dump(data, f, indent=4)
        self.ui.now_choose.setText(arg1)

    def play(self):
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = MainWindow_cc()
    window.show()
    sys.exit(app.exec_())