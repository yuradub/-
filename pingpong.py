from pygame import *
from random import *
from time import time as timer 

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, weight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (weight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.weight=weight
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_o] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_l] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        




back = (200, 255, 255)
win_height = 500
win_width = 600
window = display.set_mode((700, 500))
window.fill(back)
display.set_caption('Shooter')

game = True
finish = False
clock = time.Clock()
FPS = 60

Racket1 = Player('644504262f3c1.png', 30, 200, 4, 50, 150)
Racket2 = Player('644504262f3c1.png', 520, 200, 4, 50, 150)
ball = Ball('6445042b4ac9a.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOse', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOse', True, (180, 0, 0))
speed_x = 3
speed_y = 3
all_sprites = sprite.Group()
Racket1 = Player('644504262f3c1.png', 30, 200, 4, 50, 150)
Racket2 = Player('644504262f3c1.png', 580, 200, 4, 50, 150)
ball = Ball('6445042b4ac9a.png', 200, 200, 4, 50, 50)
all_sprites.add(Racket1, Racket2, ball)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        Racket1.update_l()
        Racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(ball, Racket1) or sprite.collide_rect(ball, Racket2):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        #якщо м'яч відлетів далі ракетки, виводимо умову програшу для першого гравця
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        Racket1.reset()
        Racket2.reset()
        ball.reset()
        all_sprites.draw(window)
    display.update()
    clock.tick(FPS)
      
