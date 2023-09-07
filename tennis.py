import pygame
import random

#import os

#game_folder = os.path.dirname(__file__)
#img_folder = os.path.join(game_folder, 'image')
#ball_img = pygame.image.load(os.path.join(img_folder, 'ball_img.png'))

WIDTH = 800
HEIGHT = 650
FPS = 60

BLACK = (0,0,0)
WHITE = (255, 255, 255)
ORANGE = (233, 118, 25)
GREEN = (0, 255, 0)
start_speeds = [-4, -3, -2, 2, 3, 4]


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedx = random.choice(start_speeds)
        self.speedy = random.choice(start_speeds)
        
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT - 25:
            self.speedy = -1 * self.speedy
        if self.rect.bottom < 25:
            self.speedy = -1 * self.speedy
        
                
    def hits_paddle(self):
        self.speedx = -1* self.speedx
        if self.speedx > 0:
            self.speedx += 1
        if self.speedy > 0:
            self.speedy += 1
        if self.speedx < 0:
            self.speedx -= 1
        if self.speedy < 0:
            self.speedy -= 1
    
    def is_goal_right(self):
        if self.rect.left < 0:
            self.rect.center = (WIDTH / 2, HEIGHT / 2)
            self.speedx = random.choice(start_speeds)
            self.speedy = random.choice(start_speeds)
            return True
    def is_goal_left(self):
        if self.rect.right > WIDTH:
            self.rect.center = (WIDTH / 2, HEIGHT / 2)
            self.speedx = random.choice(start_speeds)
            self.speedy = random.choice(start_speeds)
            return True
            
class PaddleRight(pygame.sprite.Sprite):    
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((15, 100))
            self.image.fill(WHITE)
            self.rect = self.image.get_rect()
            self.rect.right = WIDTH - 50
            self.rect.top = HEIGHT / 2 - 100
            self.speedy = 0
        def update(self):
            self.speedy = 0
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_k]:
                self.speedy = 8
            if keystate[pygame.K_i]:
                self.speedy = -8
            self.rect.y += self.speedy
            if self.rect.top > HEIGHT - 100:
                self.rect.top = HEIGHT - 100
            if self.rect.bottom < 100:
                self.rect.bottom = 100        
            
            
                
                
class PaddleLeft(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 100))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.left = 50
        self.rect.top = HEIGHT / 2 - 100
        self.speedy = 0
    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_s]:
            self.speedy = 8
        if keystate[pygame.K_w]:
            self.speedy = -8
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT - 100:
            self.rect.top = HEIGHT - 100
        if self.rect.bottom < 100:
            self.rect.bottom = 100
    
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tennis Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
ball = Ball()
paddle_right = PaddleRight()
paddle_left = PaddleLeft()
all_sprites.add(ball)
all_sprites.add(paddle_right)
all_sprites.add(paddle_left)
font = pygame.font.SysFont('Calibri', 50, True, False)
score_left = 0
score_right = 0


running = True
while running:
    
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if pygame.sprite.collide_rect(ball, paddle_left) or pygame.sprite.collide_rect(paddle_right, ball):
        ball.hits_paddle()
    if ball.is_goal_right():
        score_right += 1
    elif ball.is_goal_left():
        score_left += 1
    if score_left > 5 or score_right > 5:
        pygame.quit()
    left_text = font.render(str(score_left), True, WHITE)
    right_text = font.render(str(score_right), True, WHITE)
    all_sprites.update()
    screen.fill(ORANGE)
    screen.blit(right_text, [500, 25])
    screen.blit(left_text, [300, 25])
    all_sprites.draw(screen)
    pygame.display.flip()
    
    
pygame.quit()