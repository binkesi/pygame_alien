#!usr/bin/python
# -*- coding:utf-8 -*-
import sys
import pygame
from settings import Settings

def main():
    pygame.init()
    my_settings = Settings()
    screen = pygame.display.set_mode((my_settings.screen_width, my_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    while True:
        screen.fill(my_settings.bg_color)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)


if __name__ == '__main__':
    main()
