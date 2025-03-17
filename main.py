import pygame
from Paddle import Paddle
from ball import Ball
from bricks import Brick

pygame.init()
screen = pygame.display.set_mode(size=(800,600)) # changing window size and title
pygame.display.set_caption("Breakout Game")
game_clock = pygame.time.Clock() # method from pygame for adjusting fps

all_sprites_list = pygame.sprite.Group()  # method from pygame for petter grouping sprites(wall,ball,paddle)

paddle = Paddle() # paddle object and coordinates
paddle.rect.x = 350
paddle.rect.y = 560

ball = Ball() # ball object and coordinates
ball.rect.x = 345
ball.rect.y = 195

all_bricks = Brick((255, 0, 0), 80, 30) # generating bricks (here unnecessary arguments)
wall = all_bricks.generate_wall() # wall of bricks objects

all_sprites_list.add(paddle) # adding sprites to group
all_sprites_list.add(ball)
all_sprites_list.add(wall)

pause = False
game = True

def paused(): # function to pause game
    global pause
    font = pygame.font.Font(None, 74)
    text = font.render("PAUSE", 1, (255, 255, 255))
    screen.blit(text, (320, 300))
    pygame.display.flip()

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = False
            if event.type == pygame.QUIT:
                pause = False
                pygame.quit()
                quit()

while game:
    for event in pygame.event.get(): # recording user actions
        if event.type == pygame.KEYDOWN: # every clicked key from keyboard
            if event.key == pygame.K_SPACE:
                pause = True # pause game
                paused()
        if event.type == pygame.QUIT: # quit at closing window
              game = False

    keys = pygame.key.get_pressed() # method from pygame, for pressed keys

    if keys[pygame.K_LEFT] or keys[pygame.K_a]: # move left on "a" or "left"
        paddle.moveLeft(5)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]: # move right on "d" or "right"
        paddle.moveRight(5)

    all_sprites_list.update()

    ball.ball_logic(screen,game) # ball bouncing of walls and losing lives

    ball.check_collision(screen, game, ball, wall, paddle) # bouncing ball on collision with brick wall and paddle

    screen.fill((0, 0, 0)) # filling old record with black color
    pygame.draw.line(screen,(255,255,255),[0,38],[800,38],2) # line at bottom of the score and lives

    font = pygame.font.Font(None, 34) # viewing lives and score
    text = font.render("Score: " + str(ball.show_score()), 1,(255,255,255))
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(ball.show_lives()), 1, (255,255,255))
    screen.blit(text, (650,10))

    all_sprites_list.draw(screen) # drawing ball, wall and paddle
    pygame.display.flip() # updating entire screen
    game_clock.tick(60) # adjust fps to 60

pygame.display.quit() # quit game at the end
pygame.quit()