# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 21:23:21 2021

@author: howard
"""

import pygame
pygame.init()
pygame.mixer.init()

class BackGroundMusic:
    def __init__(self, path, repeat):
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(repeat)
        pygame.mixer.music.pause()
        self.isPause = True
    
    def playMusic(self):
        pygame.mixer.music.unpause()
        self.isPause = False
    
    def pauseMusic(self):
        pygame.mixer.music.pause()
        self.isPause = True
    
    def getBusy(self):
        
        return self.isPause
