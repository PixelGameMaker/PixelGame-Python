from Ui_Launcher import Ui_Main_Window
from PySide2 import QtWidgets

class Translate(object):
    def __init__(self):
        def set_hant(self):
            self.ui.label_Music.setText("音樂：")
            self.ui.Windowed_Settings.setText("視窗化")
            self.ui.label_Resolution.setText("解析度：")
            self.ui.Button_Play.setText("開始遊戲")
            self.ui.Graphics_Settings.setTitle("顯示設定")
            self.ui.Music_On.setText("開啟")
            self.ui.Music_Off.setText("關閉")

