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

    floor_image = {"floor": "assets/image/background/floor.png"}
    wall_image = {"wall": "assets/image/background/wall.png"}
    situation_UI = {
        "UI": "assets/image/ui/headover.png",
    }
    display_icon = {
        "hp": "assets/image/ui/hp.png",
        "mp": "assets/image/ui/mp.png",
        "exp": "assets/image/ui/exp.png",
    }

    for name, path in floor_image.items():
        surf = pygame.image.load(path).convert()
        surf = pygame.transform.smoothscale(
            surf, (displayInfo.current_w, displayInfo.current_h)
        )
        surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        background_surf[name] = surf

    size = (int(displayInfo.current_w / 32), int(displayInfo.current_h / 10.8))
    for name, path in wall_image.items():
        surf = pygame.image.load(path).convert()
        surf = pygame.transform.smoothscale(surf, size)
        background_surf[name] = surf

    size = (int(displayInfo.current_w / 5.4), int(displayInfo.current_h / 5.4))
    for name, path in situation_UI.items():
        surf = pygame.image.load(path).convert()
        surf = pygame.transform.smoothscale(surf, size)
        background_surf[name] = surf

    size = (int(displayInfo.current_h / 54), int(displayInfo.current_h / 54))
    for name, path in display_icon.items():
        surf = pygame.image.load(path).convert()
        surf = pygame.transform.smoothscale(surf, size)
        background_surf[name] = surf


class Floor(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Floor, self).__init__()

        self.surf = background_surf["floor"].copy()
        self.rect = self.surf.get_rect()

        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, player_speed, player_direction):
        direction = [
            -player_direction[0] * player_speed,
            -player_direction[1] * player_speed,
        ]

        self.rect.x += direction[0]
        self.rect.y += direction[1]


wall = {
    "room": [
        "111111111111111111111111111111111111111111111111",
        "100000000000000000000000000000000000000000000001",
        "100000000000000000000000000000000000000000000001",
        "100000000000000000000000000000000000000000000001",
        "100000000000000000000000000000000000000000000001",
        "100000000000000000000000000000000000000000000001",
        "100000000000000000000000000000000000000000000001",
        "100000000000000000000000000000000000000000000001",
        "100000000000000000000000000000000000000000000001",
        "100000000000000000000000000000000000000000000001",
        "100000000000000000000000000000000000000000000001",
        "100000000000000000000000000000000000000000000001",
        "100000000000000000000000000000000000000000000001",
        "100000000000000000000000000000000000000000000001",
        "100000000000000000000000000000000000000000000001",
        "100000000000000000000000000000000000000000000001",
        "100000000000000000000000000000000000000000000001",
        "100000000000000000000000000000000000000000000001",
        "100000000000000000000000000000000000000000000001",
        "111111111111111111111111111111111111111111111111",
    ],
    "aisle": [
        "1111111111111111",
        "0000000000000000",
        "0000000000000000",
        "1111111111111111",
    ],
}


class Wall(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Wall, self).__init__()

        self.surf = background_surf["wall"].copy()
        self.rect = self.surf.get_rect()

        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, player_speed, player_direction):
        direction = [
            -player_direction[0] * player_speed,
            -player_direction[1] * player_speed,
        ]

        self.rect.x += direction[0]
        self.rect.y += direction[1]


def wallGenerater(dtype, groups, pos):
    for x in range(len(wall[dtype])):
        for y in range(len(wall[dtype][x])):
            # print(x, y)
            if wall[dtype][x][y] == "1":
                pos_x = (x - len(wall[dtype]) / 2) * (displayInfo.current_w / 32) + pos[
                    0
                ]
                pos_y = (y - len(wall[dtype]) / 2) * (
                        displayInfo.current_h / 10.8
                ) + pos[1]
                summon_wall = Wall((pos_x, pos_y))
                for group in groups:
                    group.add(summon_wall)


def wallBysize(groups, size, pos):
    pos_x = pos[0]
    pos_y = pos[1]
    for x in range(size[0] - 1):
        summon_wall = Wall((pos_x, pos_y))
        for group in groups:
            group.add(summon_wall)
        pos_x += displayInfo.current_w / 32

    for y in range(size[1] - 1):
        pos_y += displayInfo.current_w / 48
        pos_x = pos[0]
        summon_wall = Wall((pos_x, pos_y))
        for group in groups:
            group.add(summon_wall)

        pos_x += (size[0] - 2) * displayInfo.current_w / 32
        summon_wall = Wall((pos_x, pos_y))
        for group in groups:
            group.add(summon_wall)

    pos_x = pos[0]
    for x in range(size[0] - 2):
        pos_x += displayInfo.current_w / 32
        summon_wall = Wall((pos_x, pos_y))
        for group in groups:
            group.add(summon_wall)


class Situation_display:
    class backGround(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()

            self.surf = background_surf["UI"]
            self.rect = self.surf.get_rect()
            self.rect.x = displayInfo.current_w - displayInfo.current_w / 5.4
            self.rect.y = 0

        # def update(self, detail):
        #    self.hp = detail["health"]
        #    self.mp = detail["magic point"]
        #    self.exp += detail["exp"]

    class hp(pygame.sprite.Sprite):
        def __init__(self, pos):
            super().__init__()

            self.surf = background_surf["hp"].copy()
            self.rect = self.surf.get_rect()
            self.rect.x = pos[0]
            self.rect.y = pos[1]

    class mp(pygame.sprite.Sprite):
        def __init__(self, pos):
            super().__init__()

            self.surf = background_surf["mp"].copy()
            self.rect = self.surf.get_rect()
            self.rect.x = pos[0]
            self.rect.y = pos[1]

    class exp(pygame.sprite.Sprite):
        def __init__(self, pos):
            super().__init__()

            self.surf = background_surf["exp"].copy()
            self.rect = self.surf.get_rect()
            self.rect.x = pos[0]
            self.rect.y = pos[1]
