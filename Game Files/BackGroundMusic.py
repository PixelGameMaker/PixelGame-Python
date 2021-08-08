# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 21:23:21 2021

@author: howard
"""

import pygame
pygame.init()

class BackGroundMusic:
    def __init__(self, path, repeat):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(repeat)
        pygame.mixer.music.pause()
    
    def playMusic(self):
        pygame.mixer.music.unpause()
    
    def pauseMusic(self):
        pygame.mixer.music.pause()
    
    def getBusy(self):
        
        return pygame.mixer.music.get_busy()