import pygame
from pygame.math import Vector2
from random import randint
width = 1366
height = 768
img_dir = "media/img/"
snd_dir = "media/snd/"
enemy_dir = img_dir + "enemy/"
class Player(pygame.sprite.Sprite):
    vel = 13
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_dir + "player.png")
        self.image = pygame.transform.scale(self.image,(220, 204))
        self.rect = self.image.get_rect()
        self.rect.y = height-300
        self.speed = 10
        self.jump_vel = self.vel
        self.gopher_jump = False
        self.hp = 100
        self.snd_lose = pygame.mixer.Sound(snd_dir + "lose.mp3")
    def update(self):
        key = pygame.key.get_pressed()
        if self.gopher_jump:
            self.jump()
        if key[pygame.K_SPACE] and not self.gopher_jump:
            self.gopher_jump = True
    def jump(self):
        if self.gopher_jump:
            self.rect.y -= self.jump_vel *4
            self.jump_vel -= 1
        if self.jump_vel < - self.vel:
            self.gopher_jump = False
            self.jump_vel = self.vel

class Bunch_1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(enemy_dir + "bush-1.png")
        self.image = pygame.transform.scale(self.image,(220, 204))
        self.rect = self.image.get_rect()
        self.rect.x = width+randint(100,2000)
        self.speed = randint(10, 15)
        self.rect.y = height-300
    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.rect.x = width+randint(1000,2000)
            self.speed = randint(10, 15)
            self.rect.y = height-300
class Bunch_2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(enemy_dir + "bush-2.png")
        self.image = pygame.transform.scale(self.image,(220, 204))
        self.rect = self.image.get_rect()
        self.rect.x = width+randint(100,2000)
        self.speed = randint(10, 12)
        self.rect.y = height-300
    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.rect.x = width+randint(100,2000)
            self.speed = randint(10, 12)
            self.rect.y = height-300
class Rock_1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(enemy_dir + "rock-1.png")
        self.image = pygame.transform.scale(self.image,(220, 204))
        self.rect = self.image.get_rect()
        self.rect.x = width+randint(100,500)
        self.speed = randint(10, 20)
        self.rect.y = height-300
    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.rect.x = width+randint(100,500)
            self.speed = randint(10, 20)
            self.rect.y = height-300
class Rock_2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(enemy_dir + "rock-2.png")
        self.image = pygame.transform.scale(self.image,(220, 204))
        self.rect = self.image.get_rect()
        self.rect.x = width+randint(1,500)
        self.speed = randint(10, 20)
        self.rect.y = height-300
    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.rect.x = width+randint(1,500)
            self.speed = randint(10, 20)
            self.rect.y = height-300

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_dir + "coin.png")
        self.image = pygame.transform.scale(self.image,(210, 214))
        self.rect = self.image.get_rect()
        self.rect.x = width+randint(4000, 6000)
        self.speed = randint(10, 20)
        self.rect.y = height-320
        self.copy = self.image
        self.position = Vector2(self.rect.center)
        self.direction = Vector2(0, -1)
        self.angle = 0
        self.snd_coin = pygame.mixer.Sound(snd_dir + "coin.mp3")
    def rotate(self, rotate_speed):
        self.direction.rotate_ip(-rotate_speed)
        self.angle += rotate_speed  # Изменяем угол поворота
        self.image = pygame.transform.rotate(self.copy, self.angle)  # Поворот картинки
        self.rect = self.image.get_rect(center=self.rect.center)  # Изменение рамки
    def update(self):
        self.rect.x -= self.speed
        self.rotate(10)
        if self.rect.x < 0:
            self.rect.x = width+randint(4000,6000)
            self.speed = randint(10, 20)
            self.rect.y = height-320