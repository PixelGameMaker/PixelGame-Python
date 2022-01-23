# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 21:31:56 2021

@author: howar
"""
from Background import Situation_display

import pygame
pygame.init()



class UI_display:
    def __init__(self, detail):
        
        self.display = Situation_display()
        
        self.background = self.display.backGround()
        
        self.max_hp = detail['hp']
        self.max_mp = detail['mp']
        
        self.hp = self.max_hp
        self.mp = self.max_mp
        self.exp = 0
        
        
    def update(self, detail):
        for key, value in detail.items():
            setattr(self, key, value)
        
        group = pygame.sprite.Group()
        group.add(self.background)
        
        for i in range(int(self.hp /self.max_hp*10)):
            hp = self.display.hp([i*25 + 1650, 33 ])
            group.add(hp)
        
        for i in range(int(self.mp /self.max_mp*10)):
            mp = self.display.mp([i*25 + 1650, 83])
            group.add(mp)
        
        for i in range(int(self.exp / 100*10)):
            exp = self.display.exp([i*25 + 1650, 133])
            group.add(exp)
        
        return group