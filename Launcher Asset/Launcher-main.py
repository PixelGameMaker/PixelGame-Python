import sys
import json
import os
from os.path import expanduser
from PySide2 import QtWidgets, QtCore, QtGui
from Ui_Launcher import Ui_Main_Window

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