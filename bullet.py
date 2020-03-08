import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #A Class to Manage Bullets Fired from the Ship

    def __init__(self, ai_settings, screen, ship):
        #Create a Bullet Object at the Current Position of the Ship
        super(Bullet, self).__init__()
        self.screen = screen

        #Create a Bullet Rect at (0, 0) and then Set the Correct Position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #Store the Position of the Bullet As a Decimal Value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        #Move the Bullet up the Screen
        #Update the Decimal Position of the Bullet
        self.y -= self.speed_factor
        #Update the Rect Position
        self.rect.y = self.y
    
    def draw_bullet(self):
        #Draw the Bullet to the Screen
        pygame.draw.rect(self.screen, self.color, self.rect)