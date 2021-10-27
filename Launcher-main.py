import sys
import json
import os
from os.path import expanduser
from PySide2 import QtWidgets, QtCore, QtGui

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

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Main_Window()
        self.ui.setupUi(self)
        


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())