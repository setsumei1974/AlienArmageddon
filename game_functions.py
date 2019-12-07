import pygame

import sys

def check_events(ship):
    #Respond to Keypresses and Mouse Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False

def update_screen(ai_settings, screen, ship):
    #Update Images on the Screen and Flip to the New Screen
    #Redraw the Screen during Each Pass through the Loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #Make the Most Recently Drawn Screen Visible
    pygame.display.flip()