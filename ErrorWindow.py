import glob
import os
import sys

from PySide2 import QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtGui import QFontDatabase, QPixmap
from PySide2.QtWidgets import QSplashScreen

from Error_Window import Ui_Form

list_of_files = glob.glob(
    "ErrorLog/*"
)  # * means all if need specific format then *.csv
traceback = max(list_of_files, key=os.path.getctime)
print(traceback)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("Launcher Asset/unifont-14.0.01.ttf")
        self.ui.label_2.setText(open(traceback).read())


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    pixmap = QPixmap("Launcher Asset/Logo_Died.png")
    splash = QSplashScreen(pixmap)
    splash.show()
    splash.showMessage("Oops! Something went wrong...", Qt.AlignBottom, Qt.black)
    app.processEvents()
    window = MainWindow()
    window.show()
    splash.finish(window)
    sys.exit(app.exec_())
