import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([100, 10]) # pygame surface object with appearance setting
        self.image.fill((255,255,255))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()

        pygame.draw.rect(self.image, (255,255,255),[0,0,100,10])


        self.rect = self.image.get_rect() # creating paddle on screen


    def moveLeft(self, pixels): # move paddle to left
        self.rect.x -= pixels
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, pixels): # move paddle to right
        self.rect.x += pixels
        if self.rect.x > 700:
            self.rect.x = 700