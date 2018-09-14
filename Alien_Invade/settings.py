#!usr/bin/python
# -*- coding:utf-8 -*-

class Settings():
    """存储《外星人入侵》所有设置的类"""

    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (91, 155, 221)
        #self.ship_speed_factor = 3
        self.ship_limit = 3

        # 子弹设置
        #self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = 250, 50, 50
        self.bullets_allowed = 3

        # 外星人设置
        #self.alien_speed = 1.5
        self.fleet_drop_speed = 0.2
        #self.fleet_direction = 1

        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 3
        self.bullet_speed = 2
        self.alien_speed = 1.5

        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

