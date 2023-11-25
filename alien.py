import pygame
from pygame.sprite import Sprite

#sub class

class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen 
        self.ai_settings = ai_settings

        # load the image of the alien, set it
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #set the alien at top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height 

        #store aliens position
        self.x = float(self.rect.x)
    
    def check_edges(self):
        #return true if alien is at the edge of the screem
        screen_rect = self.screen.get_react()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True 
    
    def update(self):
        #moving the alien to left/right 
        self.x += (self.ai_settings.alien_speed_factor *
                        self.ai_settings.fleet_direction)
        self.rect.x = self.x
    
    def blitme(self):
        # draw alien at its currenct position
        self.screen.blit(self.image, self.rect)