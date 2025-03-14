import pygame
from Paddle import Paddle
from ball import Ball
from bricks import Brick

pygame.init()

score = 0
lives = 3

all_sprites_list = pygame.sprite.Group()

paddle = Paddle()
paddle.rect.x = 350
paddle.rect.y = 560

ball = Ball()
ball.rect.x = 345
ball.rect.y = 195

all_bricks = pygame.sprite.Group()
for i in range(7):
    brick = Brick((255,0,0),80,30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick((255,100,0),80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick((255,255,0),80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)

all_sprites_list.add(paddle)
all_sprites_list.add(ball)

pause = False

keys = pygame.key.get_pressed()

def paused():
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


screen = pygame.display.set_mode(size=(800,600))
pygame.display.set_caption("Breakout Game")

game_clock = pygame.time.Clock()

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = True
                paused()
        if event.type == pygame.QUIT:
              game = False

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        paddle.moveLeft(5)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        paddle.moveRight(5)

    all_sprites_list.update()

    if ball.rect.x >= 790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, (255,255,255))
            screen.blit(text, (250,300))
            pygame.display.flip()
            pygame.time.wait(3000)
            game=False
    if ball.rect.y < 40:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, paddle):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.bounce()

    brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
    for brick in brick_collision_list:
        ball.bounce()
        score += 1
        brick.kill()
        if len(all_bricks) == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, (255,255,255))
            screen.blit(text, (200, 300))
            pygame.display.flip()
            pygame.time.wait(3000)
            game = False

    screen.fill((0,0,0))
    pygame.draw.line(screen,(255,255,255),[0,38],[800,38],2)

    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1,(255,255,255))
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, (255,255,255))
    screen.blit(text, (650,10))

    all_sprites_list.draw(screen)
    pygame.display.flip()
    game_clock.tick(60)

pygame.display.quit()
pygame.quit()