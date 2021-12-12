# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 16:01:18 2021

@author: 
"""

from Character import character_surf_initialize, get_update_direction
from Character import Player, Bullet, Enemy, Weapon, Text
from Background import background_surf_init, Floor, wallBysize
from BackGroundMusic import BackGroundMusic

import pygame.locals
import time
import random
import json

with open('Json/config.json') as f:
    data = json.load(f)

pygame.init()


displayInfo = pygame.display.Info()

screensize = data['preferresolution']
SCREEN_WIDTH = screensize[0:screensize.index('x')-1]
SCREEN_WIDTH = int(SCREEN_WIDTH)
SCREEN_HEIGHT = screensize[screensize.index('x')+2:]
SCREEN_HEIGHT = int(SCREEN_HEIGHT)
TITLE = 'lol RPG'




class gameEnv():
    def __init__(self, config):
        
        #self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), pygame.FULLSCREEN)
        if data['windowed']==True:
            self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), pygame.RESIZABLE)
            pygame.display.set_caption(TITLE)
        else:
            self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), pygame.FULLSCREEN)
            pygame.display.set_caption(TITLE)
        
        #print(data['windowed'])
        
        self.clock = pygame.time.Clock()
        pygame.font.init()
        self.font  = pygame.font.Font('assets/fonts/OCRAEXT.TTF', 16)
        self.music = BackGroundMusic('assets/music/backgroundMusic.mp3', -1)
        #self.fps = int(data['fps'])
        self.fps = 60
        
        character_surf_initialize()
        background_surf_init()
        
        self.bullet_cd = time.time() -10
        self.dps_clock = time.time()
        
        self.wall = pygame.sprite.Group()
        self.floor = pygame.sprite.Group()
        self.bullet = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        self.situation_text = pygame.sprite.Group()
        self.all_sprite = pygame.sprite.Group()
        
        for x in range(-SCREEN_WIDTH, SCREEN_WIDTH, SCREEN_WIDTH):
            for y in range(-SCREEN_HEIGHT, SCREEN_HEIGHT, SCREEN_HEIGHT):
                summon_floor = Floor([x, y])
                self.floor.add(summon_floor)
                self.all_sprite.add(summon_floor)
                
        self.player = Player()
        self.all_sprite.add(self.player)
        
        self.player.set_profession(config['profession'])
        
        self.weapon = Weapon()
        self.weapon.set_weapon(self.player.weapon)
        
        self.att_text = Text(self.font, 'att:', (5, 5))
        self.dps_text = Text(self.font, 'dps:', (5, 20))
        self.enemy_left_text = Text(self.font, 'Enemy Left:', (5, 35))
        self.resorution_text = Text(self.font, 'resorution:', (5, 50))
        self.fps_text = Text(self.font, 'fps:', (5, 65))
        
        self.situation_text.add(self.att_text)
        self.situation_text.add(self.dps_text)
        self.situation_text.add(self.enemy_left_text)
        self.situation_text.add(self.resorution_text)
        self.resorution_text.update('resorution:' + str(SCREEN_WIDTH) + 'x'+ str(SCREEN_HEIGHT))
        self.situation_text.add(self.fps_text)
        self.fps_text.update('fps:'+str(self.fps))
        
        #player_situation 
        self.player_text = Text(self.font, 'player:', (SCREEN_WIDTH -120, 5))
        self.player_mp_text = Text(self.font, 'mp:', (SCREEN_WIDTH -120, 20))
        self.player_hp_text = Text(self.font, 'hp:', (SCREEN_WIDTH -120, 35))
        self.player_weapon_text = Text(self.font, 'weapon:', (SCREEN_WIDTH -120, 50))
        
        self.situation_text.add(self.player_text)
        self.situation_text.add(self.player_mp_text)
        self.situation_text.add(self.player_hp_text)
        self.situation_text.add(self.player_weapon_text)
        
        self.groups = (self.all_sprite, self.wall)
        wallBysize(self.groups, (96, 68), (-1920, -1080))
        #wallGenerater('room', self.groups, (1000, 0))
        
        self.att=0
        self.dps={}
        
        #music.playMusic()
    
    def mainloop(self):
        
        #switch music mute by launcher
        if data['music']==True:
            self.music.playMusic()
        else:
            self.music.pauseMusic()
        
        while True:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    import sys
                    sys.exit(0)
                    
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_0:
                        detail = {'x':random.randint(0, displayInfo.current_w),
                                  'y':random.randint(0, displayInfo.current_h),
                                  'health' : 1000,
                                  'speed':6}
                        summon_enemy = Enemy(detail)
                        self.enemy.add(summon_enemy)
                        self.all_sprite.add(summon_enemy)
                        
                        #if events.key == pygame.K_1:
                        #    weapon.switch_weapon(1)
                        # 
                        #if events.key == pygame.K_2:
                        #    weapon.switch_weapon(2)
                        #    
                        #if events.key == pygame.K_3:
                        #    weapon.switch_weapon(3)
                        #
                        #if events.key == pygame.K_q:
                        #    weapon.next_weapon()
                    
                    if events.key == pygame.K_m:
                        if self.music.getBusy():
                            self.music.playMusic()
                        else:
                            self.music.pauseMusic()
                            
                    if events.key == pygame.K_ESCAPE:
                        pygame.quit()
                        del pygame.locals
                        return False
                        
            key_pressed = list(pygame.key.get_pressed())
        
        
        
            direction = [key_pressed[pygame.K_d] - key_pressed[pygame.K_a],
                         key_pressed[pygame.K_s] - key_pressed[pygame.K_w]]
                        
            
            #wall
            
            self.wall.update(self.player.speed, [direction[0], 0])
            if pygame.sprite.spritecollide(self.player, self.wall, False) != []:
                self.wall.update(self.player.speed, [-direction[0], 0])
                direction[0] =0
                
            self.wall.update(self.player.speed, [0, direction[1]])
            if pygame.sprite.spritecollide(self.player, self.wall, False) != []:
                self.wall.update(self.player.speed, [0, -direction[1]])
                direction[1] =0
                
            #floor
            
            for sprite in self.floor:
                #new_x = None
                #new_y = None
                if sprite.rect.x < -SCREEN_WIDTH:
                    sprite.rect.x += SCREEN_WIDTH *2
                if sprite.rect.x > SCREEN_WIDTH:
                    sprite.rect.x -= SCREEN_WIDTH *2
                if sprite.rect.y < -SCREEN_HEIGHT:
                    sprite.rect.y += SCREEN_HEIGHT *2
                if sprite.rect.y > SCREEN_HEIGHT:
                    sprite.rect.y -= SCREEN_HEIGHT *2
                    
            self.floor.update(self.player.speed, direction)
                
                
            #player
            if key_pressed[pygame.K_SPACE]:
                if time.time() - self.player.speedup_cd > 4:
                    self.player.speedup_cd = time.time()
                    self.player.speedup = 8
                    
                    
        
            self.player.update(direction)
            
            
            #print(direction)
            
            #enemy
            self.enemy.update(self.player.rect, direction, self.player.speed)
            
            #bullet
            if pygame.mouse.get_pressed()[0]:
                if time.time() - self.bullet_cd > 1 / self.weapon.detail['frequency']:
                    #print('summon')
                    self.bullet_cd = time.time()
                    mouse_pos = pygame.mouse.get_pos()
                    target_direction = [mouse_pos[0]-self.player.rect.centerx,
                                 mouse_pos[1]-self.player.rect.centery]
                    target_direction = get_update_direction(target_direction)
                    detail={'knockback':self.weapon.detail['knockback'],
                            'accuracy':self.weapon.detail['accuracy'],
                            'damage':self.weapon.detail['damage'],
                            'strike':self.weapon.detail['strike'],
                            'speed':self.weapon.detail['speed'],
                            'cost':self.weapon.detail['cost'],
                            'size':self.weapon.detail['size'],
                            'kind':self.weapon.detail['kind'],
                            'target':'enemy',
                            'direction':target_direction,
                            }
                    #print(direction)
                    
                    if self.player.cost_mp(detail['cost']):
                        summon_bullet = Bullet(self.player, detail)
                        self.bullet.add(summon_bullet)
                        self.all_sprite.add(summon_bullet)
                
            for entity in self.enemy:
                if time.time() - entity.bullet_cd > entity.attack_cd:
                    entity.bullet_cd = time.time()
                    target = entity.target
                    if target != None:
                        target_direction = [target.centerx -entity.rect.centerx,
                                            target.centery -entity.rect.centery]
                        target_direction = get_update_direction(target_direction)
                        detail={'knockback':self.weapon.detail['knockback'],
                                'accuracy':self.weapon.detail['accuracy'],
                                'damage':self.weapon.detail['damage'],
                                'strike':self.weapon.detail['strike'],
                                'speed':self.weapon.detail['speed'],
                                'cost':self.weapon.detail['cost'],
                                'size':self.weapon.detail['size'],
                                'kind':self.weapon.detail['kind'],
                                'target':'player',
                                'direction':target_direction,
                                }
                        summon_bullet = Bullet(entity, detail)
                        self.bullet.add(summon_bullet)
                        self.all_sprite.add(summon_bullet)
                
            self.bullet.update(direction, self.player.speed)
        
            #gun
            
            
            #text
            self.att = (self.weapon.detail['damage'] * (self.weapon.detail['accuracy'] * (1- self.weapon.detail['strike'])) +\
                        self.weapon.detail['damage'] *  self.weapon.detail['accuracy'] * self.weapon.detail['strike'] * 2 ) *\
                        self.weapon.detail['frequency']
            self.att_text.update('att:' + str(self.att))
            
            
            
            
            for current_time in list(self.dps.keys()):
                if time.time() - current_time > 1:
                    self.dps.pop(current_time)
            
            self.dps_text.update('dps:' + str(round(sum(self.dps.values()) / 1, 2)))
            self.enemy_left_text.update('Enemy Left:' + str(len(self.enemy)))
            
            self.player_text.update('Player:')
            self.player_hp_text.update('hp:' + str(self.player.health))
            self.player_mp_text.update('mp:' + str(self.player.mp))
            self.player_weapon_text.update('weapon:' + str(self.weapon.main_hand))
            
            
            #if dps != {} : print(dps)
            
            for entity in self.bullet:
                if entity.target == 'enemy':
                    collided_enemy = pygame.sprite.spritecollide(entity, self.enemy, False)
                
                elif entity.target == 'player':
                    group = pygame.sprite.Group()
                    group.add(self.player)
                    collided_enemy = pygame.sprite.spritecollide(entity, group, False)
                
                if  ((entity.rect.x -960) **2 + (entity.rect.y -540) **2) > self.weapon.detail['range'] **2:
                    print('yes')
                    print(entity.rect.x, entity.rect.y)
                    entity.kill()
                    self.bullet.remove(entity)
                    del entity
                    continue
                
                elif pygame.sprite.spritecollide(entity, self.wall, False) != []:
                    entity.kill()
                    self.bullet.remove(entity)
                    del entity
                    continue
            
                
                elif len(collided_enemy) > 0:
                    detail = {'damage':entity.damage,
                              'knockback':entity.knockback,
                              }
                    
                    for collided in collided_enemy:
                        collided.hit(detail, entity.rect)
                        if entity.target == 'enemy':
                            self.dps[time.time()] = detail['damage']
                        entity.kill()
                        #bullet.remove(entity)
                        print(collided.health)
                        if collided.health <= 0:
                            collided.kill()
                            self.enemy.remove(collided)
                            
                            del collided
                            print('del')
                    
                    del entity
            
            
            self.screen.fill((255, 255, 255))
            for entity in self.all_sprite:
                self.screen.blit(entity.surf, entity.rect)
            
            for entity in self.situation_text:
                self.screen.blit(entity.surf, entity.rect)
            
            if len(self.enemy) <= 0:
                return True #pass
            
            if self.player.health <= 0:
                return False #loss
            
            self.clock.tick(self.fps)
            pygame.display.flip()
            pygame.event.pump()
            
    def gameSettings(self, lvl, data):
        for i in range(lvl *1):
            index = random.choice(list(data.keys()))
            detail = {'x':random.randint(-displayInfo.current_w, displayInfo.current_w *2),
                      'y':random.randint(-displayInfo.current_h, displayInfo.current_h *2),
                      'health' : lvl *data[index]['health'],
                      'speed':lvl *data[index]['speed'],
                      'cd': 1 /lvl,
                      'stay_range': data[index]['stay_range'],
                      'att_range': data[index]['att_range']}
            summon_enemy = Enemy(detail)
            self.enemy.add(summon_enemy)
            self.all_sprite.add(summon_enemy)
        
        #summon background 
            
