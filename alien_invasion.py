import sys

import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship

def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ui_settings = Settings()
    screen = pygame.display.set_mode(
        (ui_settings.screen_width, ui_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Make a ship
    ship = Ship(ui_settings, screen)
    # Make a group to store bullets in
    bullets = Group()

    # Start the main loop for the game
    while True:
        gf.check_events(ui_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        # Get rid of bullets that have disappeared
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        gf.update_screen(ui_settings, screen, ship, bullets)

run_game()