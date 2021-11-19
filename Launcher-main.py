import sys
import json
import os
from os.path import expanduser
from PySide2 import QtWidgets, QtCore, QtGui
import pyautogui

def CheckWorkDir():
    HomeDir = expanduser("~")
    HomeDir = HomeDir.lower()
    #HomeDir = HomeDir.replace("\\","\\\\")
    #print(HomeDir)
    CurrentDir = os.getcwd()
    CurrentDir = CurrentDir.lower()
    #print(CurrentDir)
    if CurrentDir in ["c:\\windows\\system32", HomeDir]:
        print("Error, Please change Work Dir.")
        os.system("pause")
        quit()

    if CurrentDir.find("pixelrpg-python") == -1:
        print("[WARN] You are not in PixelRPG-Python Folder.")
        #print("Your current working directory is:", CurrentDir)
        
from Ui_Launcher import Ui_Main_Window

CheckWorkDir()

#check if config.json exsists
if not os.path.isfile("config.json"):
    print("[WARN] config.json not found.")
    print("[WARN] Creating new config.json.")
    #read screen biggest resolution
    width, height= pyautogui.size()
    screensize = (f"{width} x {height}")
    print(f"[INFO] Your screen size is {screensize}")
    '''
    screen = QtWidgets.QDesktopWidget().screenGeometry()
    '''
    with open("config.json", "w") as f:
        json.dump({"Fullscreen Resolution": "{screensize}", "Music": "On", "Windowed" : "True"}, f)
#read json file
with open("config.json") as json_file:
    config = json.load(json_file)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Main_Window()
        self.ui.setupUi(self)
        #add combo box text from config.json
        '''
        self.ui.Resolution_Settings.addItem(config["Width"] + "x" + config["Height"])
        '''


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())