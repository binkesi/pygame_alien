#!usr/bin/python
# -*- coding:utf-8 -*-

import pygame

class Ship():
    def __init__(self, my_settings, screen):
        self.screen = screen
        self.my_settings = my_settings

        # 加载飞船图像，获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放置在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


        # 存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.my_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.my_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= 2
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 2

        self.rect.centerx = self.center

    def center_ship(self):
        self.center = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)