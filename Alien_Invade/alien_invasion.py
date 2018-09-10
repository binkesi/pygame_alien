#!usr/bin/python
# -*- coding:utf-8 -*-
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    my_settings = Settings()
    screen = pygame.display.set_mode((my_settings.screen_width, my_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    my_ship = Ship(my_settings, screen)

    while True:
        #监听鼠标键盘事件
        gf.check_events(my_ship)
        my_ship.update()

        #填充背景色
        gf.update_screen(my_settings, screen, my_ship)


def main():
    run_game()


if __name__ == '__main__':
    main()
