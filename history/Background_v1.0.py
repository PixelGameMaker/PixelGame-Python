# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 16:08:27 2021

@author: howard
"""
import pygame

pygame.init()

def background_surf_init():
    global background_surf
    background_surf = {}
    
    background_image = {'floor':'assets/image/background/floor.png'}
    
    for name, path in background_image.items():
        surf = pygame.image.load(path).convert()
        surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        background_surf[name] = surf

class Floor(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Floor, self).__init__()
        
        self.surf = background_surf['floor'].copy()
        self.rect = self.surf.get_rect()
        
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        
    def update(self, player_speed, player_direction):
        direction = [-player_direction[0] *player_speed,
                     -player_direction[1] *player_speed]
        
        self.rect.x += direction[0]
        self.rect.y += direction[1]