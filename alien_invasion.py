#importing stuff so the program will run well

import pygame 
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats 
from ship import Ship 
import game_functions as gf 

def run_game():
    #for pygame, settings and its screen object 
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai-settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #This is to store the gam stats
    stats = GameStats(ai_settings)

    #setting up the background color
    bg_color = (230, 230, 230)

    #Making the ship, bullets and aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, bullets)

    #starting the loop for game 
    while True :
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()