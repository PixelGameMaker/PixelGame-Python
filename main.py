# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 21:09:02 2021

@author: howard
"""

import game_loop
import json

with open('Json/choose.json','r')as f:
    choose=json.load(f)
    config = {'profession': str(choose['choose'])}

game = game_loop.gameEnv(config)

fo = open('assets/enemy.json', 'r')
data = json.load(fo)
fo.close()
del fo

lvl = 0

while True:
    lvl += 1
    
    game.gameSettings(lvl, data)
    
    isPass = game.mainloop()
    
    if not isPass :
        print('Loss\n')
        import pygame
        pygame.quit()
        break
    
    else:
        print('pass')


