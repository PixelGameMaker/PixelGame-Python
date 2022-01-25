# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 21:09:02 2021

@author: howard
"""
import os
import subprocess
import sys
from datetime import datetime
import traceback

import game_loop
import json


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

lvl = 0

try:
    while True:
        lvl += 1

        game.gameSettings(lvl, data)

        isPass = game.mainloop()

        if not isPass:
            print("Loss\n")
            import pygame

            pygame.quit()
            lvls = str(lvl)
            if not CheckPyInstaller():
                subprocess.call(["python", "YouLose.py", "--lv", lvls])
            else:
                subprocess.call(["YouLose.exe", "--lv", lvls])
            break

        else:
            print("pass")

except Exception:
    print("[ERROR] Unknown game error, please report to developer.")
    import pygame

    pygame.quit()
    error_data = traceback.format_exc()
    print(error_data)
    date = datetime.utcnow().strftime("%Y-%m-%d_%H.%M.%S")
    if not os.path.exists("ErrorLog"):
        os.mkdir("ErrorLog")
    with open("ErrorLog/traceback_{}.txt".format(date), "w") as f:
        f.write(error_data)
    if CheckPyInstaller():
        subprocess.call("ErrorWindow.exe")
    else:
        subprocess.call(["python", "ErrorWindow.py"])
