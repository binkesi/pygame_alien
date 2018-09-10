#!usr/bin/python
# -*- coding:utf-8 -*-
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    my_settings = Settings()
    screen = pygame.display.set_mode((my_settings.screen_width, my_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    my_ship = Ship(my_settings, screen)
    bullets = Group()

    while True:
        #监听鼠标键盘事件
        gf.check_events(my_settings, screen, my_ship, bullets)
        my_ship.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        #填充背景色
        gf.update_screen(my_settings, screen, my_ship, bullets)


def main():
    run_game()


if __name__ == '__main__':
    main()
