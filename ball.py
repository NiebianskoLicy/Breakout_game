import pygame
from random import randint

LIVES = 3
SCORE = 0

class Ball(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([10,10]) # pygame surface object with appearance setting
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))

        pygame.draw.rect(self.image, (255,255,255),[0,0,10,10])

        self.velocity = [randint(4,8),randint(-8, 8)]

        self.rect = self.image.get_rect() # creating ball on screen

    def update(self): # setting ball direction and moving ball
        self.rect.x += self.velocity[0] # setting object velocity
        self.rect.y += self.velocity[1]

    def bounce(self): # ball bouncing in opposing direction with a bit of randomness
        self.velocity[0] = -randint(4,8)
        self.velocity[1] = randint(-8,8)
        
    def ball_logic(self,screen,game): # ball bouncing of walls
        global LIVES
        if self.rect.x >= 790:
            self.velocity[0] = -self.velocity[0]
        if self.rect.x <= 0:
            self.velocity[0] = -self.velocity[0]
        if self.rect.y > 590:
            self.velocity[1] = -self.velocity[1]
            LIVES -= 1 # losing life for not bouncing on bottom wall
            if LIVES == 0:
                font = pygame.font.Font(None, 74)
                text = font.render("GAME OVER", 1, (255, 255, 255))
                screen.blit(text, (250, 300))
                pygame.display.flip()
                pygame.time.wait(3000)
                quit()
        if self.rect.y < 40:
            self.velocity[1] = -self.velocity[1]

    def check_collision(self, screen, game, ball, wall, paddle): # checking collision with bricks and paddle
        global SCORE
        brick_collision_list = pygame.sprite.spritecollide(ball, wall, False)
        if pygame.sprite.collide_mask(ball, paddle):  # bouncing ball on collision with paddle
            ball.rect.x -= ball.velocity[0]
            ball.rect.y -= ball.velocity[1]
            ball.bounce()
        for brick in brick_collision_list: # bouncing ball on collision with bricks
            ball.bounce()
            SCORE += 1
            brick.kill()
            if len(brick.generate_wall()) == 0: # win game after braking all bricks
                font = pygame.font.Font(None, 74)
                text = font.render("LEVEL COMPLETE", 1, (255, 255, 255))
                screen.blit(text, (200, 300))
                pygame.display.flip()
                pygame.time.wait(3000)
                quit()


    def show_lives(self):
        return LIVES

    def show_score(self):
        return SCORE