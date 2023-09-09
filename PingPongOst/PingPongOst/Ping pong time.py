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
        if keys[K_DOWN] and self.rect.y <= 350:
            self.rect.y += self.speed
    def updateLeft(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <= 350:
            self.rect.y += self.speed

class ball(GameSprite):
    def startmove(self):
        startnum = randint(1, 4)
        if startnum == 1:
            self.xmove = 'right'
            self.ymove = 'up'
        if startnum == 2:
            self.xmove = 'right'
            self.ymove = 'down'
        if startnum == 3:
            self.xmove = 'left'
            self.ymove = 'down'
        if startnum == 4:
            self.xmove = 'left'
            self.ymove = 'up'
    
    def update(self):
        if self.xmove == 'right':
            self.rect.x += self.speed
        if self.xmove == 'left':
            self.rect.x -= self.speed
        if self.ymove == 'up':
            self.rect.y -= self.speed
        if self.ymove == 'down':
            self.rect.y += self.speed
        
        if self.rect.y >= 435:
            self.ymove = 'up'
        if self.rect.y <= 0:
            self.ymove = 'down'

pingball = ball('Tennis ball.png', 65, 65, 315, 210, 5)
pingball.startmove()

playerLeft = Player('PongPlayerOne.png', 25, 150, 10, 0, 5)
playerRight = Player('PongPlayerTwo.png', 25, 150, 665, 0, 5)

window = display.set_mode((700, 500))
display.set_caption('Ping Pong Time')
background = transform.scale(image.load("ping-pong-table.jpg"), (700, 500))

clock = time.Clock()
fps = 60

bonk = mixer.Sound('bonk.ogg')
lose = mixer.Sound('lose.ogg')

pong = 0
fontresult = font.SysFont('Arial', 60)
fontTXT = font.SysFont('Arial', 30)

finish = False
game = True
while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        playerLeft.updateLeft()
        playerLeft.reset()
        playerRight.updateRight()
        playerRight.reset()
        pingball.reset()
        pingball.update()

        if sprite.collide_rect(pingball, playerLeft):
            pingball.xmove = 'right'
            pingball.speed += 1
            bonk.play()
            pong += 1
        if sprite.collide_rect(pingball, playerRight):
            pingball.xmove = 'left'
            pingball.speed += 1
            bonk.play()
            pong += 1

        if pingball.rect.x <= 0:
            window.blit(fontresult.render('Правый игрок победил!',True,(0, 0, 0)), (85, 230))
            finish = True
            lose.play()
        if pingball.rect.x >= 635:
            window.blit(fontresult.render('Левый игрок победил!',True,(0, 0, 0)), (95, 230))
            finish = True
            lose.play()
        window.blit(fontTXT.render('Отбиваний: '+str(pong),True,(0, 0, 0)), (0, 0))

        clock.tick(fps)
        display.update()