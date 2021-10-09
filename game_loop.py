# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 16:01:18 2021

@author: howard
"""

from Character import character_surf_initialize, get_update_direction
from Character import Player, Bullet, Enemy, Weapon, Text
from Background import background_surf_init, Floor, wallGenerater
from BackGroundMusic import BackGroundMusic

import pygame.locals
import time
import random

pygame.init()

displayInfo = pygame.display.Info()

SCREEN_WIDTH = displayInfo.current_w
SCREEN_HEIGHT = displayInfo.current_h
TITLE = 'charater'
    


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()
font  = pygame.font.Font('assets/fonts/OCRAEXT.TTF', 16)
music = BackGroundMusic('assets/music/backgroundMusic.mp3', -1)
fps = 120


    
character_surf_initialize()
background_surf_init()
    
bullet_cd = time.time() -10
dps_clock = time.time()

wall = pygame.sprite.Group()
floor = pygame.sprite.Group()
bullet = pygame.sprite.Group()
enemy = pygame.sprite.Group()
situation_text = pygame.sprite.Group()
all_sprite = pygame.sprite.Group()

for x in range(-SCREEN_WIDTH, SCREEN_WIDTH, SCREEN_WIDTH):
    for y in range(-SCREEN_HEIGHT, SCREEN_HEIGHT, SCREEN_HEIGHT):
        summon_floor = Floor([x, y])
        floor.add(summon_floor)
        all_sprite.add(summon_floor)

player = Player()
all_sprite.add(player)

player.set_profession('Archer')

weapon = Weapon()
weapon.set_weapon(player.weapon)

att_text = Text(font, 'att:', (5, 5))
dps_text = Text(font, 'dps:', (5, 20))
enemy_left_text = Text(font, 'Enemy Left:', (5, 35))
all_sprite.add(att_text)
all_sprite.add(dps_text)
all_sprite.add(enemy_left_text)

#player_situation 
player_text = Text(font, 'player:', (SCREEN_WIDTH -120, 5))
player_mp_text = Text(font, 'mp:', (SCREEN_WIDTH -120, 20))
player_hp_text = Text(font, 'hp:', (SCREEN_WIDTH -120, 35))
player_weapon_text = Text(font, 'weapon:', (SCREEN_WIDTH -120, 50))
all_sprite.add(player_text)
all_sprite.add(player_mp_text)
all_sprite.add(player_hp_text)
all_sprite.add(player_weapon_text)

groups = (all_sprite, wall)
wallGenerater('room', groups, (0, 0))

att=0
dps={}
music.playMusic()


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
                    enemy.add(summon_enemy)
                    all_sprite.add(summon_enemy)
                
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
                    if music.getBusy():
                        music.pauseMusic()
                    else:
                        music.playMusic()
                    
                if events.key == pygame.K_ESCAPE:
                    pygame.quit()
                    import sys
                    sys.exit(0)
                    
        key_pressed = list(pygame.key.get_pressed())
        
        
        
        direction = [key_pressed[pygame.K_d] - key_pressed[pygame.K_a],
                     key_pressed[pygame.K_s] - key_pressed[pygame.K_w]]
                    
        
        #wall
        
        wall.update(player.speed, [direction[0], 0])
        if pygame.sprite.spritecollide(player, wall, False) != []:
            wall.update(player.speed, [-direction[0], 0])
            direction[0] =0
            
        wall.update(player.speed, [0, direction[1]])
        if pygame.sprite.spritecollide(player, wall, False) != []:
            wall.update(player.speed, [0, -direction[1]])
            direction[1] =0
        
        #floor
        
        for sprite in floor:
            new_x = None
            new_y = None
            if sprite.rect.x < -SCREEN_WIDTH:
                sprite.rect.x += SCREEN_WIDTH *2
            if sprite.rect.x > SCREEN_WIDTH:
                sprite.rect.x -= SCREEN_WIDTH *2
            if sprite.rect.y < -SCREEN_HEIGHT:
                sprite.rect.y += SCREEN_HEIGHT *2
            if sprite.rect.y > SCREEN_HEIGHT:
                sprite.rect.y -= SCREEN_HEIGHT *2
            
        floor.update(player.speed, direction)
        
        
        #player
        if key_pressed[pygame.K_SPACE]:
            if time.time() - player.speedup_cd > 4:
                player.speedup_cd = time.time()
                player.speedup = 8
        
        
        
        player.update(direction)
        
        
        #print(direction)
        
        #enemy
        enemy.update(player.rect, direction, player.speed)
        
        #bullet
        if pygame.mouse.get_pressed()[0]:
            if time.time() - bullet_cd > 1 / weapon.detail['frequency']:
                #print('summon')
                bullet_cd = time.time()
                mouse_pos = pygame.mouse.get_pos()
                direction = [mouse_pos[0]-player.rect.centerx,
                             mouse_pos[1]-player.rect.centery]
                direction = get_update_direction(direction)
                detail={'knockback':weapon.detail['knockback'],
                        'accuracy':weapon.detail['accuracy'],
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
        
        bullet.update(direction, player.speed)
        
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
            if  entity.rect.x > displayInfo.current_w *2 or\
                entity.rect.x < -displayInfo.current_w or\
                entity.rect.y > displayInfo.current_h *2 or\
                entity.rect.y < -displayInfo.current_h:
                    entity.kill()
                    bullet.remove(entity)
                    del entity
                    continue
            
            if pygame.sprite.spritecollide(entity, wall, False) != []:
                entity.kill()
                bullet.remove(entity)
                del entity
                continue
            
            collided_enemy = pygame.sprite.spritecollide(entity, enemy, False)
            if collided_enemy != []:
                for collided in collided_enemy:
                    detail = {'damage':entity.damage,
                              'knockback':entity.knockback}
                    collided.hit(detail, entity.rect)
                    dps[time.time()] = entity.damage
                entity.kill()
                #bullet.remove(entity)
                del entity
                
        
            
        screen.fill((255, 255, 255))
        for entity in all_sprite:
            screen.blit(entity.surf, entity.rect)
            
        
                           
        
        
        
        clock.tick(fps)
        pygame.display.flip()
            
