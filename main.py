# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 21:09:02 2021

@author: howard
"""
import json
import os
import subprocess
import sys
import traceback
from datetime import datetime

import game_loop


def CheckPyInstaller():
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        print(
            "[INFO] You are running from PyInstaller packed executable. Hopes there is no bug."
        )
        return True
    else:
        print("[INFO] You are running from normal Python source code.")
        return False


with open("Json/choose.json", "r") as f:
    choose = json.load(f)
    config = {"profession": str(choose["choose"])}

game = game_loop.gameEnv(config)

fo = open("assets/enemy.json", "r")
data = json.load(fo)
fo.close()
del fo

if not os.path.isfile("Json/save.json"):
    lvl = 0
else:
    with open("Json/save.json", "r") as s:
        save = json.load(s)
        lvl = int(save["level"]) - 1

try:
    while True:
        lvl += 1

        game.gameSettings(lvl, data)

        isPass, isSave = game.mainloop()

        if not isPass:
            print("Loss\n")
            import pygame

            pygame.quit()
            if isSave in ['SAVE_QUIT','SAVE_DEAD']:
                with open("Json/save.json", "w") as b:
                    save = {"level": lvl}
                    json.dump(save, b, indent=4)
                if isSave == 'SAVE_DEAD':
                    if not CheckPyInstaller():
                        subprocess.call(["python", "YouLose.py", "--lv", str(lvl)])
                    else:
                        subprocess.call(["release/YouLose.exe", "--lv", str(lvl)])
                else:
                    if not CheckPyInstaller():
                        subprocess.call(["python", "YouLose.py", "--lv", -1])
                    else:
                        subprocess.call(["release/YouLose.exe", "--lv", -1])
            break
        else:
            print("pass")

except:
    print("[ERROR] Unknown game error, please report to developer.")
    import pygame

    pygame.quit()
    error_data = traceback.format_exc()
    print(error_data)
    date = datetime.utcnow().strftime("%Y-%m-%d_%H.%M.%S")
    if not os.path.exists("ErrorLog"):
        os.mkdir("ErrorLog")
    with open("ErrorLog/traceback_{}_lv.{}.txt".format(date, lvl), "a") as f:
        f.write("Error Occurred on lv." + str(lvl) + "\n\n")
        f.write(error_data)
    with open("Json/save.json", "w") as b:
        save = {"level": lvl}
        json.dump(save, b, indent=4)
    if CheckPyInstaller():
        subprocess.call("release/ErrorWindow.exe")
    else:
        subprocess.call(["python", "ErrorWindow.py"])
