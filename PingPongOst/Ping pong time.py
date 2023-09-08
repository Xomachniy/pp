from pygame import *
from random import randint
init()
mixer.init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, playerWidght, playerHeight, playerX, playerY, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (playerWidght, playerHeight))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = playerX
        self.rect.y = playerY
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def updateRight(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <= 400:
            self.rect.y += self.speed
    def updateLeft(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <= 400:
            self.rect.y += self.speed

class ball(GameSprite):
    def move(self):
        pass

pingball = ball('Tennis ball.png', 65, 65, 315, 210, 5)

playerLeft = Player('PongPlayerOne.png', 25, 200, 10, 0, 5)
playerRight = Player('PongPlayerTwo.png', 25, 200, 665, 0, 5)

window = display.set_mode((700, 500))
display.set_caption('Ping Pong Time')
background = transform.scale(image.load("ping-pong-table.jpg"), (700, 500))

clock = time.Clock()
fps = 60

game = True
while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0, 0))
    playerLeft.updateLeft()
    playerLeft.reset()
    playerRight.updateRight()
    playerRight.reset()
    pingball.reset()

    clock.tick(fps)
    display.update()