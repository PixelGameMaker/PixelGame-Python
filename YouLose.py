import argparse
import sys

from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import Qt
from PySide2.QtGui import QFontDatabase, QPixmap
from PySide2.QtWidgets import QSplashScreen

from You_Lose import Ui_Form

parser = argparse.ArgumentParser()
parser.add_argument("--lv", type=int, default=0)

args = parser.parse_args()

level = args.lv


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        QFontDatabase.addApplicationFont("Launcher Asset/unifont-14.0.01.ttf")
        if level == -1:
            self.ui.label_2.setText("Haha, you didn't save the file. :)\n"
                                    "Remember next time don't click the X button.")
        elif level >= 5:
            self.ui.label_2.setText(
                f"Wow! You are better than 99% of the players!\n"
                f"You died at Lv.{level}!"
            )
        elif level >= 0:
            self.ui.label_2.setText(f"You died at Lv.{level}!\n" f"Keep going!")
        else:
            self.ui.label_2.setText("You have quit the game.")

    def keyPressEvent(self, event):  # 設定鍵盤按鍵映射
        super(MainWindow, self)
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    pixmap = QPixmap("Launcher Asset/Logo_Splash.png")
    splash = QSplashScreen(pixmap)
    splashlabel = QtWidgets.QLabel(splash)
    splashgif = QtGui.QMovie("Launcher Asset/Logo_Splash.gif")
    splashlabel.setMovie(splashgif)
    splashgif.start()
    splash.show()
    splash.showMessage("Thanks for playing", Qt.AlignBottom, Qt.black)
    delayTime = 1.3
    timer = QtCore.QElapsedTimer()
    timer.start()
    while timer.elapsed() < delayTime * 1000:
        app.processEvents()
    window = MainWindow()
    window.show()
    splash.finish(window)
    sys.exit(app.exec_())
