import pygame

import sys

from bullet import Bullet

from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    #Respond to Keypresses
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    #Fire a Bullet if the Limit Has Not Been Reached
    #Create a New Bullet to Add to the Bullet Group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    #Respond to Key Releases
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    #Respond to Keypresses and Mouse Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
def update_screen(ai_settings, screen, ship, aliens, bullets):
    #Update Images on the Screen and Flip to the New Screen
    #Redraw the Screen during Each Pass through the Loop
    screen.fill(ai_settings.bg_color)
    #Redraw All Bullets behind Ship and Aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    #Make the Most Recently Drawn Screen Visible
    pygame.display.flip()

def update_bullets(bullets):
    #Update the Position of Bullets and Remove Older Bullets
    #Update the Position of Bullets
    bullets.update()
    
    #Remove Bullets that Disappear from the Top of the Screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def create_fleet(ai_settings, screen, aliens):
    #Create a Full Fleet of Aliens
    #Create an Alien and Determine the Number of Aliens in a Row
    #Space between Each Alien is Equal to the Width of One Alien
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    #Create the First Row of Aliens
    for alien_number in range(number_aliens_x):
        #Create an Alien and Place the Alien int the Row
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)