#!usr/bin/python
# -*- coding:utf-8 -*-

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, my_settings, screen):
        super().__init__()
        self.screen = screen
        self.my_settings = my_settings

        self.image = pygame.image.load('images/alien_ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.my_settings.alien_speed * self.my_settings.fleet_direction)
        self.rect.y += self.my_settings.fleet_drop_speed
        self.rect.x = self.x
        self.rect.y = self.y