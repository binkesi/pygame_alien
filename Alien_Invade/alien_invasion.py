#!usr/bin/python
# -*- coding:utf-8 -*-
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button

def run_game():
    pygame.init()
    my_settings = Settings()
    screen = pygame.display.set_mode((my_settings.screen_width, my_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(my_settings, screen, "Play")
    stats = GameStats(my_settings)
    my_ship = Ship(my_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(my_settings, screen, my_ship, aliens)

    while True:
        #监听鼠标键盘事件
        gf.check_events(my_settings, screen, stats, play_button, my_ship, aliens, bullets)
        if stats.game_active:
            my_ship.update()
            gf.update_bullets(my_settings, screen, my_ship, aliens, bullets)
            gf.update_aliens(my_settings, stats, screen, my_ship, aliens, bullets)
        #填充背景色
        gf.update_screen(my_settings, screen, stats, my_ship, aliens, bullets, play_button)


def main():
    run_game()


if __name__ == '__main__':
    main()
