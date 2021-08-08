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

def surf_initialize():
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
    bullet_images = {'normal_bullet' : 'assets/image/bullet/normal_bullet.png'}
    
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
        self.surf = self.surf_dict['standing']
        self.rect = self.surf.get_rect()
        self.rect.centerx = displayInfo.current_w / 2
        self.rect.centery = displayInfo.current_h / 2
        
        #setting
        self.health = 100
        self.max_mp = 100
        self.mp = 100
        
        self.walking = False
        
        self.walking_cd = time.time()
        
        
    def update(self, direction):
        update_img(self, direction)
        if self.mp < self.max_mp:
            self.mp += 0.5
    
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
    def __init__(self, x, y, health):
        super(Enemy, self).__init__()
        
        self.images ={'now':'standing'}
        
        displayInfo = pygame.display.Info()
        
        self.size = (int(displayInfo.current_h / 10),
                     int(displayInfo.current_h / 10))
        
        self.surf_dict = {}
        for name, surf in player_surf.items():
            self.surf_dict[name] = surf.copy()
        self.surf = self.surf_dict['standing']
        self.rect = self.surf.get_rect()
        self.rect.move_ip(x, y)
        
        self.pos = [self.rect.x, self.rect.y]
        
        #setting
        self.health = health
        
        self.walking_cd = time.time()
    
    def update(self, player_rect, player_direction):
        direction = [player_rect.x - self.rect.x, player_rect.y - self.rect.y]
        #print(direction)
        
        direction = get_update_direction(direction)

        self.pos[0] += direction[0] - player_direction[0]*2
        self.pos[1] += direction[1] - player_direction[1]*2
        
        update_img(self, direction)
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        #print(player_direction)
        
    def hit(self, damage):
        self.health -= damage
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
        
        
    def update(self, player_direction):
        self.pos[0] += self.direction[0] * self.speed - player_direction[0]
        self.pos[1] += self.direction[1] * self.speed - player_direction[1]
        #print(self.pos)
        
        self.rect.centerx = self.pos[0]
        self.rect.centery = self.pos[1]
        
        
class Weapon(pygame.sprite.Sprite):
    def __init__(self):
        super(Weapon, self).__init__()
        
        file = 'assets/weapon.scg'
        fo = open(file, 'r')
        self.data = json.load(fo)
        fo.close()
        del fo
        self.weapon_list = list(self.data.keys())
        self.main_hand = 'mk14'
        self.inventory = []
        self.detail = self.data[self.main_hand]
        
    def switch_weapon(self, weapon):
        self.main_hand = weapon
        self.detail = self.data[weapon]
        
    def add_weapon(self, weapon):
        self.inventory.append(weapon)
        
    def next_weapon(self):
        index = self.weapon_list.index(self.main_hand)+1
        if index > len(self.weapon_list)-1:
            index -= len(self.weapon_list)
        self.main_hand = self.weapon_list[index]
        self.detail = self.data[self.main_hand]

class Text(pygame.sprite.Sprite):
    def __init__(self, font, text, pos):
        super(Text, self).__init__()
        self.font = font
        
        self.surf = self.font.render(text, True, (0, 0, 0))
        self.rect = self.surf.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        
    def update(self, text):
        self.surf = self.font.render(text, True, (0, 0, 0))
        
        
        
        
        
if __name__ == '__main__':
    import pygame.locals
    
    SCREEN_WIDTH = 1440
    SCREEN_HEIGHT = 810
    TITLE = 'charater'
    
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption(TITLE)
    
    clock = pygame.time.Clock()
    font  = pygame.font.Font('C:/WINDOWS/FONTS/OCRAEXT.TTF', 16)
    
    displayInfo = pygame.display.Info()
    
    surf_initialize()
    
    bullet_cd = time.time()
    dps_clock = time.time()
    
    bullet = pygame.sprite.Group()
    enemy = pygame.sprite.Group()
    situation_text = pygame.sprite.Group()
    all_sprite = pygame.sprite.Group()
    
    player = Player()
    all_sprite.add(player)
    
    weapon = Weapon()
    
    att_text = Text(font, 'att:', (5, 5))
    dps_text = Text(font, 'dps:', (5, 20))
    enemy_left_text = Text(font, 'Enemy Left:', (5, 35))
    all_sprite.add(att_text)
    all_sprite.add(dps_text)
    all_sprite.add(enemy_left_text)
    
    #player_situation 
    player_text = Text(font, 'player:', (1320, 5))
    player_mp_text = Text(font, 'mp:', (1320, 20))
    player_hp_text = Text(font, 'hp:', (1320, 35))
    player_weapon_text = Text(font, 'weapon:', (1320, 50))
    all_sprite.add(player_text)
    all_sprite.add(player_mp_text)
    all_sprite.add(player_hp_text)
    all_sprite.add(player_weapon_text)
    
    
    att=0
    dps={}
    
    
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                import sys
                sys.exit(0)
            
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_SPACE:
                    summon_enemy = Enemy(x=random.randint(0, displayInfo.current_w),
                                         y=random.randint(0, displayInfo.current_h),
                                         health=100)
                    enemy.add(summon_enemy)
                    all_sprite.add(summon_enemy)
            
                if events.key == pygame.K_q:
                    weapon.next_weapon()
                    
                if events.key == pygame.K_l:
                    pygame.quit()
                    import sys
                    sys.exit(0)
                
        #player
        key_pressed = pygame.key.get_pressed()
        direction = [key_pressed[pygame.K_d] - key_pressed[pygame.K_a],
                     key_pressed[pygame.K_s] - key_pressed[pygame.K_w]]
        player.update(direction)
        #print(direction)
        
        
        #enemy
        enemy.update(player.rect, direction)
        
        #bullet
        if pygame.mouse.get_pressed()[0]:
            if time.time() - bullet_cd > 1 / weapon.detail['frequency']:
                #print('summon')
                bullet_cd = time.time()
                mouse_pos = pygame.mouse.get_pos()
                direction = [mouse_pos[0]-player.rect.centerx,
                             mouse_pos[1]-player.rect.centery]
                direction = get_update_direction(direction)
                detail={'accuracy':weapon.detail['accuracy'],
                        'damage':weapon.detail['damage'],
                        'strike':weapon.detail['strike'],
                        'speed':weapon.detail['speed'],
                        'cost':weapon.detail['cost'],
                        'size':weapon.detail['size'],
                        'kind':weapon.detail['kind'],
                        'direction':direction,
                        }
                #print(direction)
                
                if player.cost_mp(detail['cost']):
                    summon_bullet = Bullet(player, detail)
                    bullet.add(summon_bullet)
                    all_sprite.add(summon_bullet)
        
        bullet.update(direction)
        
        #gun
        
        
        #text
        att = (weapon.detail['damage'] * (weapon.detail['accuracy'] * (1- weapon.detail['strike'])) +\
               weapon.detail['damage'] *  weapon.detail['accuracy'] * weapon.detail['strike'] * 2 ) *\
               weapon.detail['frequency']
        att_text.update('att:' + str(att))
        
        
        for current_time in list(dps.keys()):
            if time.time() - current_time > 1:
                dps.pop(current_time)
            
        dps_text.update('dps:' + str(round(sum(dps.values()) / 1, 2)))
        enemy_left_text.update('Enemy Left:' + str(len(enemy)))
        
        player_text.update('Player:')
        player_hp_text.update('hp:' + str(player.health))
        player_mp_text.update('mp:' + str(player.mp))
        player_weapon_text.update('weapon:' + str(weapon.main_hand))
        
        
        #if dps != {} : print(dps)
        
        for entity in bullet:
            if  entity.rect.x > displayInfo.current_w or\
                entity.rect.x < 0 or\
                entity.rect.y > displayInfo.current_h or\
                entity.rect.y < 0:
                    entity.kill()
                    bullet.remove(entity)
                    del entity
                    continue
            
            collided_enemy = pygame.sprite.spritecollide(entity, enemy, False)
            if collided_enemy != []:
                for collided in collided_enemy:
                    collided.hit(entity.damage)
                    dps[time.time()] = entity.damage
                entity.kill()
                bullet.remove(entity)
                del entity
                
        
            
        screen.fill((255, 255, 255))
        for entity in all_sprite:
            screen.blit(entity.surf, entity.rect)
            
        
                           
        
        
        
        clock.tick(30)
        pygame.display.flip()
            
         
        