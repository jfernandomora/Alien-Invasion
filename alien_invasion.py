import pygame
import game_functions as gf

from settings import Settings
from ship import Ship

def run_game():
    #Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_heigh))
    pygame.display.set_caption("Alien Invasion by Johnny")

    #Make a ship.
    ship = Ship(ai_settings, screen)

    #Start the main loop for the game.
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()
