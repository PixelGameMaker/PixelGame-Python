# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 16:08:27 2021

@author: howard
"""
import pygame

pygame.init()

displayInfo = pygame.display.Info()

def background_surf_init():
    global background_surf
    background_surf = {}
    
    floor_image = {'floor':'assets/image/background/floor.png',
                        }
    wall_image = {'wall' :'assets/image/background/wall.png'}
    
    
    for name, path in floor_image.items():
        surf = pygame.image.load(path).convert()
        surf = pygame.transform.smoothscale(surf, (displayInfo.current_w, displayInfo.current_h))
        surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        background_surf[name] = surf
        
    size = (int(displayInfo.current_w /32), int(displayInfo.current_h /10.8))
    for name, path in wall_image.items():
        surf = pygame.image.load(path).convert()
        surf = pygame.transform.smoothscale(surf, size)
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
        

wall = {'room' :['1111110000111111',
                 '1000000000000001',
                 '1000000000000001',
                 '1000000000000001',
                 '0000000000000000',
                 '0000000000000000',
                 '1000000000000001',
                 '1000000000000001',
                 '1000000000000001',
                 '1111110000111111'],
        'aisle':['1111111111111111',
                 '0000000000000000',
                 '0000000000000000',
                 '1111111111111111']}
class Wall(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Wall, self).__init__()
        
        self.surf = background_surf['wall'].copy()
        self.rect = self.surf.get_rect()
        
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        
        
    def update(self, player_speed, player_direction):
        direction = [-player_direction[0] *player_speed,
                     -player_direction[1] *player_speed]
        
        self.rect.x += direction[0]
        self.rect.y += direction[1]
    

def wallGenerater(dtype, groups, pos):
    for x in range(len(wall[dtype])):
        for y in range(len(wall[dtype][x])):
            #print(x, y)
            if wall[dtype][x][y] == '1':
                pos_x = (x - len(wall[dtype]) /2) *(displayInfo.current_w /32)
                pos_y = (y - len(wall[dtype]) /2) *(displayInfo.current_h /27)
                summon_wall = Wall((pos_x, pos_y))
                for group in groups:
                    group.add(summon_wall)
    
    
