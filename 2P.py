import pygame
from paddles import Paddle
from ball import Ball
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
	
pygame.mixer.music.load("beep.mp3")
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong Game (2 Player)")
 
paddle1 = Paddle(WHITE, 10, 100)
paddle1.rect.x = 20
paddle1.rect.y = 200
 
paddle2 = Paddle(WHITE, 10, 100)
paddle2.rect.x = 670
paddle2.rect.y = 200

ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195

sprites_list = pygame.sprite.Group()

sprites_list.add(paddle1)
sprites_list.add(paddle2)
sprites_list.add(ball)

carryOn = True
 
clock = pygame.time.Clock()

score1 = 0
score2 = 0

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              carryOn = False
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x:
                     carryOn=False  
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.moveUp(5)
    if keys[pygame.K_s]:
        paddle1.moveDown(5)
    if keys[pygame.K_UP]:
        paddle2.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddle2.moveDown(5)
    sprites_list.update()
    if ball.rect.x>=690:
        pygame.mixer.music.play()
        score1 += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        pygame.mixer.music.play()
        score2 += 1
        ball.velocity[0] = -ball.velocity[0]

    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1] 
    if pygame.sprite.collide_mask(ball, paddle1) or pygame.sprite.collide_mask(ball, paddle2):
        ball.bounce()
    
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    sprites_list.draw(screen) 
    font = pygame.font.SysFont('courier', 74)
    text = font.render(str(score1), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(score2), 1, WHITE)
    screen.blit(text, (420,10))
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()