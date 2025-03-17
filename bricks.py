import pygame

class Brick(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height]) # pygame surface object with appearance setting
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))

        pygame.draw.rect(self.image,color, [0,0, width, height])

        self.rect = self.image.get_rect() # creating brick on screen

    def generate_wall(self): # generating wall of bricks
        bricks = pygame.sprite.Group()
        for i in range(7): # 1 row
            brick = Brick((255, 0, 0), 80, 30)
            brick.rect.x = 60 + i * 100
            brick.rect.y = 60
            bricks.add(brick)
        for i in range(7): # 2 row
            brick = Brick((255, 100, 0), 80, 30)
            brick.rect.x = 60 + i * 100
            brick.rect.y = 100
            bricks.add(brick)
        for i in range(7): # 3 row
            brick = Brick((255, 255, 0), 80, 30)
            brick.rect.x = 60 + i * 100
            brick.rect.y = 140
            bricks.add(brick)
        return bricks