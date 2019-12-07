#Module for Functionality of the Game
import pygame

#Module to Import Settings
from settings import Settings

#Module to Import the Ship
from ship import Ship

#Module to Import the Functions of the Game
import game_functions as gf

def run_game():
    #Initialize a Game and Create a Screen Object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Armageddon!")

    #Set the Background Color
    bg_color = (0, 25, 51)

    #Make a Ship
    ship = Ship(screen)

    #Start the Main Loop for the Game
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
        
run_game()