# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 21:09:02 2021

@author: howar
"""

import json
import game_loop

with open('choose.json','r')as f:
    choose=json.load(f)
    config = {'profession': str(choose['choose'])}

game = game_loop.gameEnv(config)

lvl = 0

while True:
    lvl += 1
    
    game.gameSettings(lvl)
    
    isPass = game.mainloop()
    
    if not isPass :
        print('Loss\n')
        import pygame
        pygame.quit()
        break


