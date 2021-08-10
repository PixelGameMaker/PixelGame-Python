# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 11:09:40 2021

@author: howard
"""

import pygame
import time
import random

pygame.init()

def surf_initialize():
    displayInfo = pygame.display.Info()
    
    global player_surf, enemy_surf, bullet_surf
    
    player_images = {'standing' : 'assets/image/player/standing.png',
                     'walking_1': 'assets/image/player/walking_1.png',
                     'walking_2': 'assets/image/player/walking_2.png'
                     }
    enemy_images  = {'standing' : 'assets/image/enemy/standing.png',
                     'walking_1': 'assets/image/enemy/walking_1.png',
                     'walking_2': 'assets/image/enemy/walking_2.png'
                     }
    bullet_images = {'normal_bullet' : 'assets/image/bullet/normal_bullet.png'}
    
    size = (int(displayInfo.current_w / 10),
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
    
    size = (int(displayInfo.current_w / 10),
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
                entity.surf = pygame.image.load(entity.images['walking_2']).convert()
                entity.images['now'] = 'walking_2'
                if direction[0] > 0:
                    pass
                else:
                    entity.surf = pygame.transform.flip(entity.surf, 1, 0)
            else:
                entity.surf = pygame.image.load(entity.images['walking_1']).convert()
                entity.images['now'] = 'walking_1'
                #print('change to walking_1')
                if direction[0] > 0:
                    pass
                else:
                    entity.surf = pygame.transform.flip(entity.surf, 1, 0)
                entity.images['now'] = 'walking_1'
        else:
            entity.surf = pygame.image.load(entity.images['standing']).convert()
            entity.images['now'] = 'standing'
        entity.surf = pygame.transform.smoothscale(entity.surf, entity.size)
        entity.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)

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
        
        self.images = {'standing' : 'assets/image/player/standing.png',
                       'walking_1': 'assets/image/player/walking_1.png',
                       'walking_2': 'assets/image/player/walking_2.png',
                       'now':'standing'}
            
        displayInfo = pygame.display.Info()
        
        self.size = (int(displayInfo.current_w / 10),
                     int(displayInfo.current_h / 10))
        
        self.surf = pygame.image.load(self.images['standing']).convert()
        self.surf = pygame.transform.smoothscale(self.surf, self.size)
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.centerx = displayInfo.current_w / 2
        self.rect.centery = displayInfo.current_h / 2
        
        #setting
        self.health = 100
        self.mp = 100
        
        self.walking = False
        
        self.walking_cd = time.time()
        
        
    def update(self, direction):
        update_img(self, direction)
        self.mp += 1
    
    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()
            
    def cost_mp(self, mp):
        self.mp -= mp
            
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        super(Enemy, self).__init__()
        
        self.images = {'standing' : 'assets/image/enemy/standing.png',
                       'walking_1': 'assets/image/enemy/walking_1.png',
                       'walking_2': 'assets/image/enemy/walking_2.png',
                       'now':'standing'}
        
        displayInfo = pygame.display.Info()
        
        self.size = (int(displayInfo.current_h / 10),
                     int(displayInfo.current_h / 10))
        
        self.surf = pygame.image.load(self.images['standing']).convert()
        self.surf = pygame.transform.smoothscale(self.surf, self.size)
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
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
    def __init__(self, detail):
        super(Bullet, self).__init__()
        
        self.images = {'normal_bullet' : 'assets/image/bullet/normal_bullet.png'}
        
        displayInfo = pygame.display.Info()
        
        self.size = 0.01
        self.damage = 10
        self.speed = 5
        self.accuracy = 0.9
        self.strike = 0.05
        self.cost = 5
        self.direction = [0, 0]
        
        for key, value in detail.items():
            setattr(self, key, value)
        
        self.size = (int(displayInfo.current_h * self.size),
                     int(displayInfo.current_h * self.size))
            
        self.surf = pygame.image.load(self.images['normal_bullet']).convert()
        self.surf = pygame.transform.smoothscale(self.surf, self.size)
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        
        self.pos = [player.rect.centerx, player.rect.centery]
        self.rect.centerx = self.pos[0]
        self.rect.centery = self.pos[1]
        
        player.cost_mp(self.cost)
        
        if random.randint(0, 1.000) >  self.accuracy:
            self.damage = 0
        if random.randint(0, 1.000) <= self.strike:
            self.damage *= 2
        
    def update(self):
        self.pos[0] += self.direction[0] * self.speed
        self.pos[1] += self.direction[1] * self.speed
        print(self.pos)
        
        self.rect.centerx = self.pos[0]
        self.rect.centery = self.pos[1]
        
        
        
        
if __name__ == '__main__':
    import pygame.locals
    
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    TITLE = 'test'
    
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    
    displayInfo = pygame.display.Info()
    
    bullet_cd = time.time()
    
    bullet = pygame.sprite.Group()
    enemy = pygame.sprite.Group()
    all_sprite = pygame.sprite.Group()
    
    player = Player()
    all_sprite.add(player)
    
    
    clock = pygame.time.Clock()
    
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                import sys
                sys.exit(0)
            
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_SPACE:
                    summon_enemy = Enemy(x=400, y=100, health=100)
                    enemy.add(summon_enemy)
                    all_sprite.add(summon_enemy)
                
        #player
        key_pressed = pygame.key.get_pressed()
        direction = [key_pressed[pygame.K_d]-key_pressed[pygame.K_a],
                     key_pressed[pygame.K_s] -key_pressed[pygame.K_w]]
        player.update(direction)
        #print(direction)
        
        
        #enemy
        enemy.update(player.rect, direction)
        
        #bullet
        if pygame.mouse.get_pressed()[0]:
            if time.time() - bullet_cd > 0.25:
                print('summon')
                bullet_cd = time.time()
                mouse_pos = pygame.mouse.get_pos()
                direction = [mouse_pos[0]-player.rect.centerx,
                             mouse_pos[1]-player.rect.centery]
                direction = get_update_direction(direction)
                detail={'damage':10,
                        'speed':5,
                        'accuracy':1,
                        'strike':0,
                        'cost':5,
                        'direction':direction,
                        'size':0.01
                        }
                print(direction)
                summon_bullet = Bullet(detail)
                bullet.add(summon_bullet)
                all_sprite.add(summon_bullet)
        
        bullet.update()
        
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
                entity.kill()
                bullet.remove(entity)
                del entity
                
        
            
        screen.fill((255, 255, 255))
        for entity in all_sprite:
            screen.blit(entity.surf, entity.rect)
        
        
        clock.tick(15)
        pygame.display.flip()
            
         
        