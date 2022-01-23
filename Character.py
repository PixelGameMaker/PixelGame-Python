# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 11:09:40 2021

@author: howard
"""

import pygame
import time
import random
import json
import math

pygame.init()

def character_surf_initialize():
    with open('Json/config.json') as f:
        data=json.load(f)
    displayInfo = pygame.display.Info()
    screensize = data['preferresolution']
    SCREEN_WIDTH = screensize[0:screensize.index('x')-1]
    SCREEN_WIDTH = int(SCREEN_WIDTH)   

    with open('Json/choose.json') as c:
        config = json.load(c)
    choose_chara=config['choose']
    
    global player_surf, enemy_surf, bullet_surf, player_images
    player_surf = {}
    enemy_surf = {}
    bullet_surf = {}
    
    if str(choose_chara) == 'Archer':
        player_images = {'standing' : 'assets/image/player/Archer/standf.png',
                         'walking_1': 'assets/image/player/Archer/walkingf_1.png',
                         'walking_2': 'assets/image/player/Archer/walkingf_2.png'
                        }
    elif str(choose_chara) == 'Knight':
        player_images = {'standing' : 'assets/image/player/Knight/standf.png',
                         'walking_1': 'assets/image/player/Knight/walkingf_1.png',
                         'walking_2': 'assets/image/player/Knight/walkingf_2.png'
                        }
    elif str(choose_chara) == 'Magician':
        player_images = {'standing' : 'assets/image/player/Magician/standf.png',
                         'walking_1': 'assets/image/player/Magician/walkingf_1.png',
                         'walking_2': 'assets/image/player/Magician/walkingf_2.png'
                        }
    elif str(choose_chara) == 'Assassin':
        player_images = {'standing' : 'assets/image/player/Assassin/standf.png',
                         'walking_1': 'assets/image/player/Assassin/walkingf_1.png',
                         'walking_2': 'assets/image/player/Assassin/walkingf_2.png'
                        }
    enemy_images  = {'standing' : 'assets/image/enemy/standing.png',
                     'walking_1': 'assets/image/enemy/walking_1.png',
                     'walking_2': 'assets/image/enemy/walking_2.png',
                     'walking_3': 'assets/image/enemy/walking_3.png',
                     'walking_4': 'assets/image/enemy/walking_4.png'
                     }
    bullet_images = {'normal_bullet' : 'assets/image/bullet/normal_bullet.png', 
                     'enemy_bullet'  : 'assets/image/bullet/enemy_bullet.png',
                     'arrow'         : 'assets/image/bullet/arrow.png',
                     'wave'          : 'assets/image/bullet/wave.png',
                     'magic_particle': 'assets/image/bullet/magic_particle.png'}
    
    size = (int(SCREEN_WIDTH / 33),
            int(SCREEN_WIDTH / 22))
    for name, path in player_images.items():
        surf = pygame.image.load(path).convert_alpha()
        surf = pygame.transform.smoothscale(surf, size)
        surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        player_surf[name] = surf
        if 'walking' in name:
            surf = pygame.image.load(path).convert_alpha()
            #surf = pygame.transform.flip(surf, 1, 0)
            surf = pygame.transform.smoothscale(surf, size)
            surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
            player_surf[name+'_reverse'] = surf
    
    size = (int(displayInfo.current_h / 12),
            int(displayInfo.current_h / 12))
    for name, path in enemy_images.items():
        surf = pygame.image.load(path).convert_alpha()
        surf = pygame.transform.smoothscale(surf, size)
        surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        enemy_surf[name] = surf
        if 'walking' in name:
            surf = pygame.image.load(path).convert_alpha()
            surf = pygame.transform.flip(surf, 1, 0)
            surf = pygame.transform.smoothscale(surf, size)
            surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
            enemy_surf[name+'_reverse'] = surf
    
    for name, path in bullet_images.items():
        surf = pygame.image.load(path).convert()
        surf.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        bullet_surf[name] = surf

def update_img(entity, direction):
    if time.time() - entity.walking_cd <= 0.25:
        return
    #print('updating')
    entity.walking_cd = time.time()
    if direction == [0, 0]:
        entity.surf = entity.surf_dict['standing']
        entity.images['now'] = 'standing'

    elif entity.images['now'] == 'walking_1':
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

def update_enemy_img(entity, direction):
    if time.time() - entity.walking_cd <= 0.25:
        return
    #print('updating')
    entity.walking_cd = time.time()
    if direction == [0, 0]:
        entity.surf = entity.surf_dict['standing']
        entity.images['now'] = 'standing'

    elif entity.images['now'] == 'walking_1':
        #print('change to walking_2')
        entity.images['now'] = 'walking_2'
        if direction[0] > 0:
            entity.surf = entity.surf_dict['walking_2']
        else:
            entity.surf = entity.surf_dict['walking_2_reverse']
    elif entity.images['now'] == 'walking_2':
        #print('change to walking_3')
        entity.images['now'] = 'walking_3'
        if direction[0] > 0:
            entity.surf = entity.surf_dict['walking_3']
        else:
            entity.surf = entity.surf_dict['walking_3_reverse']
    elif entity.images['now'] == 'walking_3':
        #print('change to walking_4')
        entity.images['now'] = 'walking_4'
        if direction[0] > 0:
            entity.surf = entity.surf_dict['walking_4']
        else:
            entity.surf = entity.surf_dict['walking_4_reverse']
    else:
        entity.images['now'] = 'walking_1'
        #print('change to walking_1')
        if direction[0] > 0:
            entity.surf = entity.surf_dict['walking_1']
        else:
            entity.surf = entity.surf_dict['walking_1_reverse']


def update_bullet_image_direction(image, direction):
    if direction[0] == 0:
        direction[0] += 0.00000001
        
    angle = 180-math.degrees(math.atan(direction[1] /direction[0]))
     
    image = pygame.transform.rotate(image, angle)
    return image
    

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
        file = 'assets/profession.json'
        #self.profession = {'Archer',
        #                   'Knight',
        #                   'Magician',
        #                   'Assassin'
        #                   }
        
        fo = open(file, 'r')
        self.profession = json.load(fo)
        fo.close()
        del fo
        
        #self.health = 100
        #self.max_mp = 100
        #self.set_speed = 5
        #self.speed = self.set_speed
        #self.mp = 100
        
        self.walking = False
        self.speedup = 0
        self.knockback = [0, 0]
        
        self.walking_cd = time.time()
        self.speedup_cd = time.time()
        
            
    def set_profession(self, profession):
        self.health = self.profession[profession]['health']
        self.max_mp = self.profession[profession]['max_mp']
        self.set_speed = self.profession[profession]['speed']
        self.weapon = self.profession[profession]['weapon']
        
        self.mp = self.max_mp
        self.speed = self.set_speed
        
        
        
        
    
    def update(self, direction):
        update_img(self, direction)
        if self.mp < self.max_mp:
            self.mp += 0.5
        
        self.speed = self.set_speed *(1 +self.speedup)
        if self.speedup:
            self.speedup -= 1
        
    
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
        for name, surf in enemy_surf.items():
            self.surf_dict[name] = surf.copy()
        self.surf = self.surf_dict['standing'].copy()
        self.rect = self.surf.get_rect()
        self.rect.move_ip(detail['x'], detail['y'])
        
        self.pos = [self.rect.x, self.rect.y]
        
        #setting
        self.health = detail['health']
        self.knockback = [0, 0]
        self.speed = detail['speed']
        self.attack_range = detail['att_range']
        self.stay_range = detail['stay_range']
        self.attack_cd = detail['cd']
        self.bullet_cd = time.time()
        self.target = None
        
        self.walking_cd = time.time()
    
    def update(self, enemy_rect, enemy_direction, enemy_speed):
        direction = [enemy_rect.x - self.rect.x, enemy_rect.y - self.rect.y]
        #print(direction)
        
        direction = get_update_direction(direction)
        
        speed = self.speed
        if (self.pos[0] - enemy_rect.x) **2 + (self.pos[1] - enemy_rect.y) **2 <= self.stay_range **2:
            speed = - self.speed *0.5

        self.pos[0] += direction[0] *speed - enemy_direction[0] *enemy_speed - self.knockback[0]
        self.pos[1] += direction[1] *speed - enemy_direction[1] *enemy_speed - self.knockback[1]
        
        for i in range(len(self.knockback)):
            if abs(self.knockback[i]) < 0.5:
                self.knockback[i] = 0
            elif self.knockback[i] > 0:
                self.knockback[i] -= 0.5
            elif self.knockback[i] < 0:
                self.knockback[i] += 0.5
        
        
        update_enemy_img(self, direction)
        
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        
        if (self.pos[0] - enemy_rect.x) **2 + (self.pos[1] - enemy_rect.y) **2 <= self.attack_range **2:
            self.target = enemy_rect
        else:
            self.target = None
        
        #print(enemy_direction)
        
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
        self.range = 1
        self.target = 'enemy'
        
        for key, value in detail.items():
            setattr(self, key, value)
        
        self.size = (int(displayInfo.current_h * self.size *2.5),
                     int(displayInfo.current_h * self.size *2.5))
            
        self.surf = bullet_surf[self.kind].copy()
        self.surf = update_bullet_image_direction(self.surf, self.direction)
        self.surf = pygame.transform.smoothscale(self.surf, self.size)
        self.rect = self.surf.get_rect()
        
        self.pos = [player.rect.centerx, player.rect.centery]
        self.rect.centerx = self.pos[0]
        self.rect.centery = self.pos[1]
        
        
        
        
        if random.uniform(0, 1.000) >  self.accuracy:
            self.damage = 0
        if random.uniform(0, 1.000) < self.strike:
            self.damage *= 2
        
        
    def update(self, enemy_direction, enemy_speed):
        self.pos[0] += self.direction[0] * self.speed - enemy_direction[0] *enemy_speed
        self.pos[1] += self.direction[1] * self.speed - enemy_direction[1] *enemy_speed
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
        
    
    def set_weapon(self, weapon):
        self.main_hand = weapon
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
        
        
