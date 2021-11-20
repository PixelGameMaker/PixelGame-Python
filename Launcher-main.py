import sys
import json
import os
import time
from os.path import expanduser
from PySide2 import QtWidgets, QtCore, QtGui
import pyautogui

#WORKING DIR CHECK START

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
        print("Continue? (To exit, press Ctrl+C)")
        try:
            time.sleep(5)
        except KeyboardInterrupt:
            print("[WARN] Ctrl+C dected. Exiting...")
            quit()
        #print("Your current working directory is:", CurrentDir)
        
from Ui_Launcher import Ui_Main_Window

CheckWorkDir()

#WORKING DIR CHECK END

#JSON CHECK START

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
        #add resolution, music, windowed to json
        json.dump({"resolution": [screensize, "1280 x 720"], "music": "on", "windowed": "on", "fps": "15"}, f, indent=4)
        #add resolution 2k and 4k if screensize over 1920 x 1080
        if width > 1920 and height > 1080:
            with open("config.json", "r") as f:
                data = json.load(f)
                #data["resolution"].append("1920 x 1080")
                data["resolution"].append("2560 x 1440")
                json.dump(data, f)

#try json file is readable
try:
    with open("config.json", "r") as f:
        config = json.load(f)
        '''
        try:
            if config["screensize"] == screensize:
                pass
        except:
            print("[WARN] config.json corrupt.")
            with open("config.json", "w") as f:
                json.dump({"resolution": screensize, "music": "on", "windowed": "on"}, f)
        '''

        #print(f"[INFO] Your screen size is {config["resolution"]})

except:
    print("[WARN] config.json corrupt.")
    print("[WARN] retry creating new config.json.")
    #read screen biggest resolution
    width, height= pyautogui.size()
    screensize = (f"{width} x {height}")
    print(f"[INFO] Your screen size is {screensize}")
    '''
    screen = QtWidgets.QDesktopWidget().screenGeometry()
    '''
    with open("config.json", "w") as f:
        #add resolution, music, windowed to json
        json.dump({"resolution": [screensize, "1280 x 720"], "music": "on", "windowed": "on", "fps": "15"}, f, indent=4)
        if width > 1920 and height > 1080:
            with open("config.json", "r") as f:
                data = json.load(f)
                #data["resolution"].append("1920 x 1080")
                data["resolution"].append("2560 x 1440")
                json.dump(data, f)
finally:
    #convert resolution list to string and remove json characters and seprate each value to new line
    #config["resolution"] = str(config["resolution"]).replace("[", "").replace("]", "").replace("'", "").replace(",", "\n")
    #resolution = np.array(config["resolution"].split("\n"))
    print(f"[INFO] The resolution in config is {config['resolution']}")
    print(f"[INFO] The music in config is {config['music']}")
    print(f"[INFO] The windowed in config is {config['windowed']}")
    print(f"[INFO] The fps in config is {config['fps']}")
    print('[INFO] Starting launcher window')

#JSON CHECK END

#SYSTEM LANGUAGE CHECK START

def check_lang():
    #check if system language is chinese
    if sys.platform == "win32":
        import ctypes
        langid = ctypes.windll.kernel32.GetUserDefaultUILanguage()
        lang = langid & 0xFF
        if lang == 0x04:
            print("[INFO] System language is Chinese")
            return True
        else:
            print("[INFO] System language is not Chinese, set to English")
            return False
    '''
    else:
        print("[INFO] Something went wrong, set to English (Are you using Linux?)")
        return False
    '''
    
#SYSTEM LANGUAGE CHECK END

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Main_Window()
        self.ui.setupUi(self)
        #add combo box text from config.json
        self.ui.Resolution_Settings.addItems(config["resolution"])

        #localization
        if check_lang():
            self.ui.label_Music.setText("音樂：")
            self.ui.Windowed_Settings.setText("視窗化")
            self.ui.label_Resolution.setText("解析度：")
            self.ui.Button_Play.setText("開始遊戲")
            self.ui.Graphics_Settings.setTitle("顯示設定")
        if config["windowed"] == "on":
            self.ui.Windowed_Settings.setChecked(True)
        else:
            self.ui.Windowed_Settings.setChecked(False)
        if config["music"] == "on":
            self.ui.Music_On.setChecked(True)
            self.ui.Music_Off.setChecked(False)
        else:
            self.ui.Music_On.setChecked(False)
            self.ui.Music_Off.setChecked(True)
        self.ui.FPS_Settings.setValue(int(config["fps"]))



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())