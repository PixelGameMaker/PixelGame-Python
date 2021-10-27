# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 21:09:02 2021

@author: howar
"""

import game_loop

config = {'profession': 'Archer'}

game = game_loop.gameEnv(config)

lvl = 0

while True:
    lvl += 1
    
    game.gameSettings(lvl)
    
    isPass = game.mainloop()
    
    if not isPass :
        print('Loss')
        import pygame
        pygame.quit()
        break


