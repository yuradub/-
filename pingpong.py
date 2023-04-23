from pygame import *
from random import *
from time import time as timer 


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, waight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (waight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.waight=waight
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_s] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_o] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_l] and self.rect.x < win_width - 80:
            self.rect.x += self.speed



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
Ball = GameSprite('6445042b4ac9a.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOse', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOse', True, (180, 0, 0))
speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        Racket1.reset()
        Racket2.reset()
        Ball.reset()

    display.update()
    clock.tick(FPS)
