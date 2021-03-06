import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #A Class that Represents a Single Alien of the Fleet

    def __init__(self, ai_settings, screen):
        #Initialize an Alien and Set a Starting Position
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load an Image of an Alien and set its Rect Attribute
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        #Start Each Alien at the Upper Left of the Screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the Exact Position of the Alien
        self.x = float(self.rect.x)
    
    def blitme(self):
        #Draw the Alien at its Current Location
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        #Return True if an Alien is at the Edge of the Screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        #Move the Alien to the Right or the Left
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x