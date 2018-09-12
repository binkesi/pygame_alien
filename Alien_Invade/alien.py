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

    def blitme(self):
        self.screen.blit(self.image, self.rect)