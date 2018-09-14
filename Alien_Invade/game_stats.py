#!usr/bin/python
# -*- coding:utf-8 -*-

class GameStats():
    def __init__(self, my_settings):
        self.my_settings = my_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.my_settings.ship_limit