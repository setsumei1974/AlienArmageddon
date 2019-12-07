import pygame

class Ship():

    def __init__(self, screen):
        #Initialize the Ship and Set Its Starting Position
        self.screen = screen

        #Load the Ship Image and Get Its Rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start Each New Ship at the Bottom Center of the Screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Movement Flag
        self.moving_right = False

    def update(self):
        #Update the Position of the Ship Based on the Movement Flag
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        #Draw the Ship at Its Current Location
        self.screen.blit(self.image, self.rect)