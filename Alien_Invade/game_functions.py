#!usr/bin/python
# -*- coding:utf-8 -*-
import sys
import pygame
from bullet import Bullet
from alien import Alien


def update_screen(my_settings, screen, ship, aliens, bullets):
    screen.fill(my_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()

def check_keydown_events(event, my_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(my_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(my_settings, screen, ship, bullets):
    if len(bullets) < my_settings.bullets_allowed:
        new_bullet = Bullet(my_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(my_settings, screen, ship, bullets):
    # 响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, my_settings, screen, ship, bullets)

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def get_number_aliens_x(my_settings, alien_width):
    available_space_x = my_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(my_settings, ship_height, alien_height):
    available_space_y = (my_settings.screen_height - (12 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(my_settings, screen, aliens, alien_number, row_number):
    alien = Alien(my_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(my_settings, screen, ship, aliens):
    alien = Alien(my_settings, screen)
    number_rows = get_number_rows(my_settings, ship.rect.height, alien.rect.height)
    number_aliens_x = get_number_aliens_x(my_settings, alien.rect.width)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(my_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(my_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(my_settings, aliens)
            break

def change_fleet_direction(my_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += my_settings.fleet_drop_speed
    my_settings.fleet_direction *= -1

def update_aliens(my_settings, aliens):
    check_fleet_edges(my_settings, aliens)
    aliens.update()
