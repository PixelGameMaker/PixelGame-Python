# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 11:09:40 2021

@author: howard
"""

import pygame
import time
import random
import json

pygame.init()

def character_surf_initialize():
    displayInfo = pygame.display.Info()
    
    global player_surf, enemy_surf, bullet_surf
    player_surf = {}
    enemy_surf = {}
    bullet_surf = {}
    
    player_images = {'standing' : 'assets/image/player/standing.png',
                     'walking_1': 'assets/image/player/walking_1.png',
                     'walking_2': 'assets/image/player/walking_2.png'
                     }
    enemy_images  = {'standing' : 'assets/image/enemy/standing.png',
                     'walking_1': 'assets/image/enemy/walking_1.png',
                     'walking_2': 'assets/image/enemy/walking_2.png'
                     }
    bullet_images = {'normal_bullet' : 'assets/image/bullet/normal_bullet.png',
                     'enemy_bullet'  : 'assets/image/bullet/enemy_bullet.png'}
    
    size = (int(displayInfo.current_h / 10),
            int(displayInfo.current_h / 10))
    for name, path in player_images.items():
        surf = pygame.image.load(path).convert()
        surf = pygame.transform.smoothscale(surf, size)
        surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        player_surf[name] = surf
        if 'walking' in name:
            surf = pygame.image.load(path).convert()
            surf = pygame.transform.flip(surf, 1, 0)
            surf = pygame.transform.smoothscale(surf, size)
            surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
            player_surf[name+'_reverse'] = surf
    
    size = (int(displayInfo.current_h / 10),
            int(displayInfo.current_h / 10))
    for name, path in enemy_images.items():
        surf = pygame.image.load(path).convert()
        surf = pygame.transform.smoothscale(surf, size)
        surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        enemy_surf[name] = surf
        if 'walking' in name:
            surf = pygame.image.load(path).convert()
            surf = pygame.transform.flip(surf, 1, 0)
            surf = pygame.transform.smoothscale(surf, size)
            surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
            enemy_surf[name+'_reverse'] = surf
    
    for name, path in bullet_images.items():
        surf = pygame.image.load(path).convert()
        surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        bullet_surf[name] = surf

def update_img(entity, direction):
    if (time.time() - entity.walking_cd) > 0.25:
        #print('updating')
        entity.walking_cd = time.time()
        if direction != [0, 0]:
            if entity.images['now'] == 'walking_1':
                #print('change to walking_2')
                entity.images['now'] = 'walking_2'
                if direction[0] > 0:
                    entity.surf = entity.surf_dict['walking_2']
                else:
                    entity.surf = entity.surf_dict['walking_2_reverse']
            else:
                entity.images['now'] = 'walking_1'
                #print('change to walking_1')
                if direction[0] > 0:
                    entity.surf = entity.surf_dict['walking_1']
                else:
                    entity.surf = entity.surf_dict['walking_1_reverse']
        else:
            entity.surf = entity.surf_dict['standing']
            entity.images['now'] = 'standing'

def get_update_direction(direction):
    if abs(direction[0]) > abs(direction[1]):
        direction[1] /= abs(direction[0])
        direction[0] /= abs(direction[0])
    elif abs(direction[0]) < abs(direction[1]):
        direction[0] /= abs(direction[1])
        direction[1] /= abs(direction[1])
    elif abs(direction[0]) == abs(direction[1]) and\
        abs(direction[0]) != 0:
            direction[0] /= abs(direction[1])
            direction[1] /= abs(direction[1])
    return direction


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        
        self.images = {'now':'standing'}
            
        displayInfo = pygame.display.Info()
        
        self.size = (int(displayInfo.current_h / 10),
                     int(displayInfo.current_h / 10))
        
        self.surf_dict = {}
        for name, surf in player_surf.items():
            self.surf_dict[name] = surf.copy()
        self.surf = self.surf_dict['standing'].copy()
        self.rect = self.surf.get_rect()
        self.rect.centerx = displayInfo.current_w / 2
        self.rect.centery = displayInfo.current_h / 2
        
        #setting
        self.health = 100
        self.max_mp = 100
        self.set_speed = 5
        self.speed = self.set_speed
        self.mp = 100
        
        self.walking = False
        self.speedup = 0
        
        self.walking_cd = time.time()
        self.speedup_cd = time.time()
        
        
    def update(self, direction):
        update_img(self, direction)
        if self.mp < self.max_mp:
            self.mp += 0.5
        
        self.speed = self.set_speed *(1 +self.speedup)
        if self.speedup:
            self.speedup -= 1
        
    
    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()
            
    def cost_mp(self, mp):
        if self.mp > mp:
            self.mp -= mp
            return True
        else:
            return False
            
class Enemy(pygame.sprite.Sprite):
    def __init__(self, detail):
        super(Enemy, self).__init__()
        
        self.images ={'now':'standing'}
        
        displayInfo = pygame.display.Info()
        
        self.size = (int(displayInfo.current_h / 10),
                     int(displayInfo.current_h / 10))
        
        self.surf_dict = {}
        for name, surf in player_surf.items():
            self.surf_dict[name] = surf.copy()
        self.surf = self.surf_dict['standing'].copy()
        self.rect = self.surf.get_rect()
        self.rect.move_ip(detail['x'], detail['y'])
        
        self.pos = [self.rect.x, self.rect.y]
        
        #setting
        self.health = detail['health']
        self.knockback = [0, 0]
        self.speed = detail['speed']
        
        self.walking_cd = time.time()
    
    def update(self, player_rect, player_direction, player_speed):
        direction = [player_rect.x - self.rect.x, player_rect.y - self.rect.y]
        #print(direction)
        
        direction = get_update_direction(direction)

        self.pos[0] += direction[0] *self.speed - player_direction[0] *player_speed - self.knockback[0]
        self.pos[1] += direction[1] *self.speed - player_direction[1] *player_speed - self.knockback[1]
        
        for i in range(len(self.knockback)):
            if abs(self.knockback[i]) < 0.5:
                self.knockback[i] = 0
            elif self.knockback[i] > 0:
                self.knockback[i] -= 0.5
            elif self.knockback[i] < 0:
                self.knockback[i] += 0.5
        
        
        update_img(self, direction)
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        #print(player_direction)
        
    def hit(self, detail, bullet_rect):
        self.health -= detail['damage']
        
        knockback = [0, 0]
        knockback[0] += (bullet_rect.centerx - self.rect.centerx)
        knockback[1] += (bullet_rect.centery - self.rect.centery)
        knockback = get_update_direction(knockback)
        
        self.knockback[0] += knockback[0] * detail['knockback']
        self.knockback[1] += knockback[1] * detail['knockback']
        #print(self.knockback)
        
        if self.health <= 0:
            self.kill()
            del self
            
class Bullet(pygame.sprite.Sprite):
    def __init__(self, player, detail):
        super(Bullet, self).__init__()
                
        displayInfo = pygame.display.Info()
        
        self.size = 0.01
        self.damage = 10
        self.speed = 5
        self.accuracy = 0.9
        self.strike = 0.05
        self.cost = 5
        self.direction = [0, 0]
        self.kind = 'normal_bullet'
        self.knockback = 5
        
        for key, value in detail.items():
            setattr(self, key, value)
        
        self.size = (int(displayInfo.current_h * self.size),
                     int(displayInfo.current_h * self.size))
            
        self.surf = bullet_surf[self.kind].copy()
        self.surf = pygame.transform.smoothscale(self.surf, self.size)
        self.rect = self.surf.get_rect()
        
        self.pos = [player.rect.centerx, player.rect.centery]
        self.rect.centerx = self.pos[0]
        self.rect.centery = self.pos[1]
        
        
        
        if random.uniform(0, 1.000) >  self.accuracy:
            self.damage = 0
        if random.uniform(0, 1.000) < self.strike:
            self.damage *= 2
        
        
    def update(self, player_direction, player_speed):
        self.pos[0] += self.direction[0] * self.speed - player_direction[0] *player_speed
        self.pos[1] += self.direction[1] * self.speed - player_direction[1] *player_speed
        #print(self.pos)
        
        self.rect.centerx = self.pos[0]
        self.rect.centery = self.pos[1]
        
        
class Weapon(pygame.sprite.Sprite):
    def __init__(self):
        super(Weapon, self).__init__()
        
        file = 'assets/weapon.json'
        fo = open(file, 'r')
        self.data = json.load(fo)
        fo.close()
        del fo
        self.weapon_list = list(self.data.keys())
        self.main_hand = 'mk14'
        self.inventory = []
        self.detail = self.data[self.main_hand]
        
    def switch_weapon(self, i):
        index = i -1
        if index > len(self.weapon_list)-1:
            return
        self.main_hand = self.weapon_list[index]
        self.detail = self.data[self.main_hand]
        
    def add_weapon(self, weapon):
        self.inventory.append(weapon)
        
    def next_weapon(self):
        index = self.weapon_list.index(self.main_hand)+1
        if index > len(self.weapon_list)-1:
            index -= len(self.weapon_list)
        self.main_hand = self.weapon_list[index]
        self.detail = self.data[self.main_hand]
        

class Text(pygame.sprite.Sprite):
    def __init__(self, font, text, pos, color=(0, 255, 0)):
        super(Text, self).__init__()
        self.font = font
        
        self.surf = self.font.render(text, True, color)
        self.rect = self.surf.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        
    def update(self, text, pos=None, color=(0, 255, 0)):
        if pos != None:
            self.rect.x = pos[0]
            self.rect.y = pos[1]
        self.surf = self.font.render(text, True, color)
        
        
